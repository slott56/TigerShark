TigerShark is an X12 EDI message parser that can be tailored to
a specific partner in the health care payment ecosystem.

It contains a test directory, tools and a demo web application that does
a little bit of claim display and edit.

State of the Project
====================

Version 0.2.2
-------------
Nothing big, just a bugfix to ElementSequenceAccess (so it actually works)
and moved two large enum types to an enums module.

Version 0.2.1
-------------
I realized that a single EOB file can contain multiple EOBs. This means that
the f835 facade now has a list of all of its individual EOBs as a `facades`
property.

I also fixed a few typos, added a ClaimAdjustments common X12LoopBridge with
the corresponding claim adjustment reasons as an enum x12type, and improved
the tests for 835 files.

This package is now being used in production, and the 835 facade can be
considered somewhat stable.

Version 0.2
-----------
I've added a setup.py script and organized the files a bit more. I'm
considering this a major version bump because the inclusion of setup.py and
pregenerated parsers makes this a *lot* closer to a fully usable package. I
make no claim that any parser other than the 835 works as expected, since I
have only dealt with 835 files so far.

Development will probably slow down now that things are mostly working. In the
pipeline are auto-generated facades, or facades for 270/271 files, whichever
I need to do first.

If this sort of thing interests you, the awesome biotech startup where I
work is hiring. I can't say much about it other than it involves genes, real
science, and we are currently saving lives and improving the future of
humanity. Do drop me a line.

(Insurance billing is a painful but necessary step in this process.)

Version 0.1
-----------

TigerShark was initially developed by [S. Lott](https://github.com/slott56),
et. al. The code was recently released at my request, after I stumbled on a
few blog posts about the project:

  1. [Python as Config Language - Forget XML and INI files (Jan 12, 2008)](http://www.itmaybeahack.com/homepage/iblog/C465799452/E20080111205451.html)
  2. [Two Python Config-File Design Patterns (Jan 19, 2008)](http://www.itmaybeahack.com/homepage/iblog/C465799452/E20080119082306.html)
  3. [Configuration File Scalability - Who Knew? (Revised) (Jan 26, 2008)](http://www.itmaybeahack.com/homepage/iblog/C465799452/E20080126181253.html)
  4. [Python as Configuration Language - More Good Ideas (March 28, 2008)](http://www.itmaybeahack.com/homepage/iblog/C465799452/E20080328172746.html)
  5. [Synchronicity and Document Object Models. (March 31, 2008)](http://www.itmaybeahack.com/homepage/iblog/C465799452/E20080331113231.html)
  6. [POPO and GOPS - Plain Old Python Objects and Good Old Python Syntax (April 1, 2008)](http://www.itmaybeahack.com/homepage/iblog/C412398194/E20080401060105.html)

By the time I found those posts I had been struggling with X12 files for
about two weeks, dealing with broken parsers and PDFs that cost thousands of
dollars that describe the spec over 750 pages in human - but not, or only
barely, machine - readable format. (How the healthcare industry gets away with
getting the government to mandate a proprietary file format which you have to
pay to read is the subject of another rant...).

I was struck by the amount of good, deep thought that went into the decisions
S. Lott made, especially as compared to everything else I had seen. If you
want to contribute to this project, I highly encourage you to go read those
posts first.

What you see in verion 0.1 is a series of hacks to get TigerShark working.
I fixed a few bugs, added a facade for 835 files, and added setup instructions
to the readme. The facade code is a mess (I didn't have enough time to fully
understand the descriptor pattern and all of the underlying data structures
Steven used), and I'll have to come back and make it nicer. Ultimately the
facade should be able to be generated straight from the xml files which are
used to build the parser. I removed a bunch of files that didn't appear to
be used anywhere. I didn't try to get the demo django site working, and I'll
either remove it or add instructions for it in a later version.

Many thanks to [S. Lott](https://github.com/slott56) for releasing the code
and answering my questions, and to [John Holland](https://github.com/azoner)
for providing the xml files in his package [pyX12](https://github.com/azoner/pyx12).

Installation
============

    python setup.py install

Manually Generating the Parsers
-------------------------------

The `setup.py` script will install default parsers, but you might want to
generate your own, or you're fixing the generation script and need to test.
You can either convert all of the 4010 xml files in `Downloads/pyx12-1.5.0.zip`
or convert a file individually (which gives you more control over the result).

### Generating All Parsers From PyX12 archive ###

If you just want to generate all of the parsers, you can use the
`generate_all_parsers` script:

    python tools/generate_all_parsers.py ../Downloads/pyx12-1.5.0.zip -p parsers

This will generate all parsers in a directory called `parsers`.

### Generating A Single Parser ###

After extracting the xml files, you can create the related parser objects
using the tools:

    cd Downloads/
    unzip pyx12-1.5.0.zip
    cd ../tigershark/parsers
    python ../tools/convertPyX12.py 835.4010.X091.A1.xml M835_4010_X091_A1.py -b ../../Downloads/pyx12-1.5.0/map/ -n parsed_835

This will generate a `M835_4010_X091_A1.py` parser in your current directory.

Usage
=====

Using a Parser
--------------

    from tigershark.parsers import M835_4010_X091_A1
    m = M835_4010_X091_A1.parsed_835
    with open('/Users/sbuss/remits/95567.63695.20120314.150150528.ERA.835.edi', 'r') as f:
        parsed = m.unmarshall(f.read().strip())

Using a Facade
-----------------

Once you have parsed an X12 file, you can build a Facade around it:

    from tigershark.facade.f835 import f835_4010
    f = F835_4010(parsed)

Now you can access the segments of the X12 file in an easy and pythonic way

    >>> print(f.payee.zip)
    94066
    >>> print(f.payer.name)
    United Healthcare
    >>> print(len(f.claims))
    150
