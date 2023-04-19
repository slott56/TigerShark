######################
Using TigerShark
######################

There are several things you can do.

1.  `Create a Python class`_. This converts the XML version of a .SEF file to a Python subclass of :py:class:`x12.base.Message` to parse exchange format messages or create JSON Schema.

2.  `Emit a JSON Schema`_. The extracts JSON Schema from a subclass of :py:class:`x12.base.Message`.

3.  `Parse X12 Exchange-formatted messages`_. This uses the subclass of :py:class:`x12.base.Message` to create Plain Old Python Objects from the message.

4.  `Emit a parsed X12 message a variety of formats`_. This includes "segments" format, JSON format, or even a Python expression to rebuild the message.

We'll look at each of these in some detail

Create a Python class
=====================

The :mod:`tools.xml_extract` application parses an XML
file and writes a Python module from the XML.
This module will have a subclass of :py:class:`x12.base.Message`
that can parse messages or emit a schema.

..  important:: SEF files preferred

    Ideally, a version of this could work with the source .SEF
    files.

It works like this.

1.  Git Checkout the `PyX12 <https://github.com/azoner/pyx12>`_ project.

2.  Tweak the :mod:`tools.xml_extract` module to point to the checked-out files
    and the target directory.

3.  Run the tool to build the x12 package.

::

    python tools/xml_extract.py

Gather sample messages and build test cases before doing
anything else.

Emit a JSON Schema
==================

Each generated class has a :meth:`schema` method to emit
a dictionary that can be converted to JSON
notation.

A script might look like this:

::

    from x12 import msg_270_4010_X092_A1
    import json

    schema = msg_270_4010_X092_A1.MSG270.schema()
    print(json.dumps(schema, indent=2))

This will emit a JSON Schema file that can be
shared with non-Python applications.

The :mod:`tools.xml_extract` application parses an XML
file and **can** write a JSON Schema directly from the XML.
It seems, however, best to work directly with the Python
definitions.

Parse X12 Exchange-formatted messages
=====================================

A script can look like the following:

::

    from x12 import msg_270_4010_X092_A1
    from pathlib import Path

    source = Path("/path") / "to" / "file.txt"
    document = Source(source.read_text())
    msg = message_class.parse(document)

This will create an object, ``msg`` with
attributes for the various components (loops, segments, composites, and elements) of the message.

Emit a parsed X12 message a variety of formats
===============================================

Given a message, ``msg``, parsed by the :meth:`x12.base.Message.parse` method.
it can be emitted in a number of formats:

1.  `Sequence of segments output`_.
    This is a list of segments, similar to the exchange format,
    except it's in Python notation: a list of lists.

2.  `JSON output`_.
    This is a representation of the message/loop/segment/composite/element structure
    with some additional ``_kind`` and ``_name`` fields added.

3.  `Python output`_.
    This is an expression that can rebuild the Plain-Old Python Object.
    The reconstruction requires a ``from msg... import *`` import to
    provide all the required names for loops, segments, composites, and elements.

Sequence of segments output
---------------------------

Use the :meth:`x12.base.Message.segment_iter` method
of a message to get the segments.
The built-in :meth:`__str__` provides the list of strings output for each segment.

::

    print(list(msg.segment_iter()))


JSON output
-----------

Use the :meth:`x12.base.Message.json` method
of a message to get the JSON string.

::

    print(msg.json())

The :meth:`x12.base.Message.json` method accepts
an ``indent`` parameter to provide nicely indented output.

The alternative is to use the  :meth:`x12.base.Message.json` method
of a message to get a JSON-friendly dictionary.

::

    print(json.dumps(msg.asdict()))

This permits more flexibility in using
the features of :func:`json.dumps`.

Python output
-------------

Use the built-in :func:`__repr__` function
to emit Python.

::

    print(repr(msg))
