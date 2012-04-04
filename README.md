TigerShark is an X12 EDI message parser that can be tailored to
a specific partner in the health care payment ecosystem.

It contains a test directory, tools and a demo web application that does
a little bit of claim display and edit.

This does not (currently) have a proper Python ``setup.py`` script for installation,
since this is such a random mixture of components.

It's probably best to include a ``.pth`` file in your ``lib/site-packages``
that references this working directory.

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
