"""
x12
====

The bulk of this package is defined by extraction from other sources.
Specifically the :py:mod:`tools.xml_extract` module.

The message definition all rely on the :py:mod:`x12.base`
and :py:mod:`x12.annotations` modules.

The tools build an :py:mod:`x12.common` module.
Each message is parsed by a separate module.
"""

from .base import Source
