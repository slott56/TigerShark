#####################################
Creating New Modules with Annotations
#####################################

There are two strategies for defining
the annotations.

-   Build the Annotations. Write them to the Python module.

-   Build text source code for the Annotations.

Building ``Annotation`` objects
and *seems* sensible because the :py:func`str`
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

The underlying type definition is hard to build from primitives.

Building text seems indirect, and -- potentially --
frought with problems. However, annotation objects
aren't meant to be built by code.
They're meant to be written by people and parsed into annotation objects.

This means the code generator can use this:

::

    params = ", ".join([base] + modifiers)
    type = f"Annotated[{params}]"

Since the ``xml_extract`` tool writes text files,
this works out well enough.

Nesting
=======

It appears that nested annotations is not a good idea.

For example::

    attr_name = Annotated[list[Annotated[str, ...]], MaxItems(1)]

Seems to wind up with some internal structural issues.
This needs to be done as follows:

::

    ItemAttr_Name: TypeAlias = Annotated[str, ...]
    attr_name = Annotated[list[ItemAttr_Name], MaxItems(1)]
