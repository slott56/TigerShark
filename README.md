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

After extracting the xml files, you can create the related parser objects
using the utlities:

    mkdir parsers
    touch parsers/__init__.py
    cd parsers
    python ../web/make837.py -p M835_4010_X091_A1.py -b ../Downloads/pyx12-1.5.0/map name=835.4010.X091.A1.xml

This will generate a M835_4010_X091_A1.py file in your parsers directory.

Use it as follows:

    import M835_4010_X091_A1
    from X12.parse import Properties
    p = Properties(eltPunct="|", compPunc="^")
    m = M835_4010_X091_A1.name
    with open('/Users/sbuss/remits/95567.63695.20120314.150150528.ERA.835.edi', 'r') as f:
        parsed = m.unmarshall(f.read(), p)
    
Unfortunately, this is throwing the following error:

    TypeError                                 Traceback (most recent call last)
    /Users/sbuss/envs/tigershark/src/TigerShark/parsers/<ipython-input-5-ba4da6e5b7b4> in <module>()
          1 with open('/Users/sbuss/remits/95567.63695.20120314.150150528.ERA.835.edi', 'r') as f:
    ----> 2     parsed = m.unmarshall(f.read(), p)
          3 

    /Users/sbuss/envs/tigershark/src/TigerShark/X12/parse.py in unmarshall(self, message, factory)
        811             )
        812             raise ex
    --> 813         theMssg= self.factory.makeMessage( self.name )
        814         self.getParts( self.segmentTokens, theMssg )
        815         if len(self.segmentTokens) != 0:

    TypeError: 'NoneType' object is not callable

so the Factory isn't getting created/set properly.
