#####################################
Creating New Modules with Annotations
#####################################

There are two strategies for defining
the annotations.

-   Build the Annotations as internal data structures
    using the ``typing`` module constructs.
    Serialize this object in Python notation to the Python module.

-   Build text source code for the Annotations.

Building ``Annotation`` objects
and *seems* sensible because the :py:func:`str`
for an ``Annotation`` is a source-code string.
However, it doesn't work out well.

::

    this = Annotated[base_type]
    this = Annotated[this, SomeAnnotation()]

This is elegant-looking code, but, has limitations
around things like the following:

::

    this = Annotated[base_type]
    this = Union[this, None]

In ordinary Python syntax, we'd write this:

::

    some_object: Annotated[some_type, SomeAnotation()] | None

The underlying type definition is hard to build from primitive class definitions
in the ``typing`` module. It's much easier to write as pure source text.

Building text seems indirect, and -- potentially --
frought with problems. However, annotation objects
aren't meant to be built by code.
They're meant to be written by people and parsed into annotation objects.

This means the code generator can use code like this to write Python code:

::

    params = ", ".join([base] + modifiers)
    type = f"Annotated[{params}]"

Since the ``xml_extract`` tool writes text files,
this works out well enough.

Nesting
=======

It appears that deeply-nested annotations are not a good idea.

For example::

    attr_name = Annotated[list[Annotated[str, ...]], MaxItems(1)]

This seem to wind up with some internal structural issues.
It's difficult to get a ``match`` statement with proper ``case``
clauses.

This needs to be done as follows:

::

    ItemAttr_Name: TypeAlias = Annotated[str, ...]
    attr_name = Annotated[list[ItemAttr_Name], MaxItems(1)]
