#!/usr/bin/env python
"""Claim File Processing Utilities.

There are a number of convenience functions in this module.

..  autofunction:: genClaims

"""

import logging

def genClaims( aFile, segSep="~", eltSep="*" ):
    """Generator for individual claims from a file.
    This will gracefully read either "Expanded" claims or "Compact" claims,
    and generate "Compact" format messages.
    An expanded claim has :samp:`\\n` after each segment separator.
    A claim always begins with :samp:`ISA` followed by the element separator character,
    usually :samp:`*`.

    :param aFile: the name of the file to open, read and close.
    :param segSep: the expected segment separator, by default :samp:`~`.
    :param eltSep: the expected element separator, by default :samp:`*`.
    """
    log= logging.getLogger( "X12.file.genClaims" )
    log.info( "Reading %s", aFile )
    src= open(aFile,"r")
    claimSoFar= []
    for line in src:
        clean= line.strip()
        if len(clean) == 0:
            continue
        if clean[:4] == "ISA" + eltSep:
            if len(claimSoFar) > 0:
                yield "".join( claimSoFar )
                claimSoFar= []
        claimSoFar.append( clean )
    if len(claimSoFar) > 0:
        yield "".join( claimSoFar )
    src.close()
