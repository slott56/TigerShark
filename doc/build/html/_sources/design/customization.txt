################################################
Design Note: Customization of Message Structures
################################################

:ref:`architecture`

Problem
=======

Since we have a number of customers, each with a unique Implementation Guide,
we have to adjust the data model for each customer.  We want to permit each
customer as a simple extension module to a core application design.

Forces
======

On one hand, it's easiest to use "copy and paste" customization of the
application, making it difficult to make across-the-board changes.

On the other hand, there are 57 or so distinct Segment types, making customization
challenging.

Solution
========

A set of tools and design patterns are required.

We use the following design patterns.

-   Generic Parser ("unmarshalling") class hierarchy.  A core class hierchy
    defines the essential parser technology.  A message-specific parser object is built
    from these classes.  This parser includes customer-specific extensions.

-   A **Factory**-based parser.  The parser object uses a **Factory** object
    which generates a specific implementation's segment types.

-   Meta-data driven customizations.  A ``tools`` package to include a number
    of conversions from various kinds of metadata to our application programs.

Consequence
============

We have to bind the generic parser to a specific message implementation.
This is a **Factory** object that emits
the proper objects and handles customer-specific extensions.

The Factory cannot shared by all classes in the ``X12.parse`` structure;
that is relatively "global" among the various classes.  We can't easily
fiddle this in at Construction time when XML is translated to Python.
It has to come in later.
Each ``X12.parse`` object must acquire a Factory when it executes.

Further, it's not the ``X12.parse`` package.  The Factory must be injected
into a
separate package, with a name like ``some_project.claims-837.model``.

This can be handled a number of ways:

    -   a Configuration **Singleton** that each parser locates at run time.

    -   a Configuration object given to the Message parser, and then provided
        to each subsidiary object.

Since all of the various Parser classes are proper subclasses of ``X12.parse.Parser``,
we can provide a property in the top-level class which propagates the selected
Factory down to each element.

Further, since Parsing is a translation from one form to another, we can easily
make the ``unmarshall`` method accept the Factory as a parameter.
