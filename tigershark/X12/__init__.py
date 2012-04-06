#!/usr/bin/env python
"""Defines several modules with classes for X12 message processing.

We have to disentangle two separate concepts.

    -   **Message Type**.  This is the structure of the message.
        The structure is defined by an :class:`X12.parse.Message` object.  In addition
        to defining the structure, a parser can also unmarshall a block of text.
        It can also be used for meta-level processing like emitting DB designs.

    -   **Message Instance**.  This a specific message's data; a collection of
        Segments which can be interpreted as a Message with Loops.  (The Loops
        are not stated, only the Segments.)  A message instance can be built
        by unmarshalling a block of text, or it can be built "manually" using
        object constructors.  A message instance can unmarshall itself, returning
        a block of text.

The :mod:`X12.parse` package defines the classes which are used to build an X12 message
parser (or "unmarshaller").  The classes are generic, and don't recognize any
specific X12 message structure.

A parser for a given message type can be built from the :mod:`X12.parse` classes manually or
by a conversion tool.
The manual construction involves writing a bunch of object constructors to build parsers
for the Message, the Loops within the Message, the Segments within the Loops,
and the Composites and Elements within the Segments.

A conversion tool usually reads some other meta-data version of the message structure,
and builds an :mod:`X12.parse` structure.  There is a conversion tool for :file:`.xml` files.  Both of these conversion tools
build the complete :mod:`X12.parse` object, which can either be used to parse messages,
or can be used for other meta-level processing.

The :mod:`X12.map` package supports meta-level processing.  This includes subclasses
of :class:`X12.parse.StructureVisitor` that can traverse an :mod:`X12.parse` object to
report on its structure.
This is used by the conversion tools to traverse the definitions
and emit the source code, Django class definitions or raw SQL definitions
for the message that the parser recognizes.

The :mod:`X12.message` package defines a message instance.

``map`` sub-package
====================

..  automodule:: X12.map

``message`` sub-package
========================

..  automodule:: X12.message


``file`` module
====================

..  automodule:: X12.file


``parse`` module
====================

..  automodule:: X12.parse
"""
