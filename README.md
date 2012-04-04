TigerShark is an X12 EDI message parser that can be tailored to
a specific partner in the health care payment ecosystem.

It contains a test directory, tools and a demo web application that does
a little bit of claim display and edit.

This does not (currently) have a proper Python ``setup.py`` script for installation,
since this is such a random mixture of components.

It's probably best to include a ``.pth`` file in your ``lib/site-packages``
that references this working directory.

State of the Project
====================

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

First, set up your path. Put the path to this directory in a tigershark.pth file
in your site-packages directory. Eg:

    cd /home/me/envs/my_project_virtual_env/lib/python2.7/site-packages
    echo "/home/me/envs/my_project_virtual_env/src/tigershark" > tigershark.pth

In order to process X12 files you first need to generate a parser from the xml
or cf that describes the file format. The PyX12 package includes xml files for
several common file formats, which is included in the Download directory:

    cd Downloads/
    unzip pyx12-1.5.0.zip
    cd ..

Generating a Parser
===================

After extracting the xml files, you can create the related parser objects
using the utlities:

    cd parsers
    python ../tools/convertPyX12.py 835.4010.X091.A1.xml M835_4010_X091_A1.py -b ../Downloads/pyx12-1.5.0/map/ -n parsed_835

This will generate a M835_4010_X091_A1.py file in your parsers directory.

Use it as follows:

    import M835_4010_X091_A1
    m = M835_4010_X091_A1.parsed_835
    with open('/Users/sbuss/remits/95567.63695.20120314.150150528.ERA.835.edi', 'r') as f:
        parsed = m.unmarshall(f.read().strip())

Building a Facade
=================

Once you have parsed an X12 file, you can build a Facade around it:

    from facade.f835 import f835_4010
    f = F835_4010(parsed)

Now you can access the segments of the X12 file in an easy and pythonic way

    >>> print(f.payee.zip)
    94066
    >>> print(f.payer.name)
    United Healthcare
    >>> print(len(f.claims))
    150
