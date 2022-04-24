##########################################################
Design Note: Reconciling "Bare" Python Classes with Django
##########################################################

:ref:`architecture`

Problem
=======

Django's ``django.db.models.Model`` class must be root class of all persistent
objects.  This imposes certain implicit structure rules, and the associated methods
and attribiutes.  It also defeats ordinary Python class definition
techniques, specifically limiting inheritance.

See :ref:`Recursive Structures` for the root-cause issue.  When we define the Python
objects, we can use ordinary containers which are part of a simple inheritance
hierarchy to represent the hierarchical message structures in a strongly-typed
object structure.

When we switch from Python to Django, however, we loose inheritance, but gain a different
kind of strongly typed record definition.

We have to consider how best to define structures that permit us to
have arbitrary Python class definitions as well as the more-constrained Django ORM.

Also, see :ref:`Key Generation` for the consequent issue of how best to generate
keys in the Django implementation so that it doesn't depend on database saves.

Forces
======

There are a number of alternatives.

-   Use SQLAlchemy instead of Django's built-in models.  Since the Django
    views and templates are not tightly bound to the model, this certainly will
    work.  SQLAlchemy mappings can be used to bridge between the original
    Python classes and the database model, minimizing the impact on existing
    code.  However, Django's built-in Admin interface won't work with this external
    model definition.

-   Rewrite ``X12.parse`` to use the Django model.  This is relatively small, since
    ``X12.parse`` makes limited references to the ``X12.message`` package.  This
    tends to bind X12 parse to Django persistence even if we're doing other
    kinds of X12 message processing.

-   Rewrite ``X12.parse`` to use the formal
    **Factory** design pattern.  The Django application model module
    and the ``X12.message`` modules would all provide the necessary factory function
    to emit proper objects for use by ``X12.parse``.  Since there are relatively
    few distinct classes in ``X12.message``, this **Factory** is not terribly
    complex.

-   Assure that the various modules have precisely the same API, eliminating
    the need for a formal **Factory** object.  Since Django provides the most
    built-in functionality, ``X12.message`` modules would have to emulate
    the Django model API.

Solution
========

Use a formal **Factory** design pattern for utilities outside the Django application
framework.

Consequences
============

Some minor complex with the indirect creation of message objects in ``X12.parse``.
However, this is the only place where the indirection occurs.  All other
modules either use ``X12.parse`` or the Django web app.
