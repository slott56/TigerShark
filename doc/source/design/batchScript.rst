################################
Design Note: Batch Script Design
################################

:ref:`architecture`

Problem
=======

How do we leverage the Django settings file to provide run-time configuration?
We want to import Django models without complications or real work.

Forces
======

Django supports the ``DJANGO_SETTINGS_MODULE`` environment variable.  This is
ideal in most respects.

We can make the case that we might want an option instead of an environment
variable.  That's how ``django-admin.py`` works.  To do this correctly, we'd
need to make use of ``django.core.management`` which has a convenience function
named ``setup_environ``.

Once we've set the environment, we can then import the model.  Or, we can exec
the entire script, which leads off with model import.

Solution
========

Stick with the ``DJANGO_SETTINGS_MODULE`` environment variable.

Consequences
=============

Few, actually.
