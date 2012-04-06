#!/usr/bin/env python
"""The X12.map package contains **Visitors** that can traverse the :mod:`X12.parse`
structure to transform it from Python objects to some other form.

Often, a parser is built from some non-Python metadata.  There are a number of
conversion tools in :mod:`tools` that produce an :mod:`X12.parse` structure from other
source data.

The :mod:`X12.parse` structure defines the structure of a message type.  It can also
unmarshall text to create a message instance.

Additionally the parser structure can be used for meta-level processing.
Generally this examines the structure of the message, rather than work with
a specific message instance.  The are several meta-level transformations:

    - Emit Source (in Python, usually)

    - Emit a Data Model (in SQL, as well as the Django ORM)

The :mod:`X12.map.source` package emits Python source in one of two forms.

    -   A single, big constuctor expression for the parser.  This will rarely
        compile.

    -   A flattened definition made up of a number of Loop-level constructors.

The :mod:`X12.map.SQL` package emits SQL DDL for the Message structure.  This isn't
terribly useful, but it does build a minimal database design that
is specific to a message type.

The :mod:`X12.map.dj` package emits Django ORM class definitions for the
various kinds of Segments found within message structure definitions.

XXX - Future Expansion: :mod:`X12.map.sa` package can emit SQLAlchemy definitions
for the various kinds of Segments found within message structure definitions.

Django
=========

..  automodule:: X12.map.dj

Source
===========

..  automodule:: X12.map.source

SQL
==========

..  automodule:: X12.map.SQL

"""
