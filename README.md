TigerShark is an X12 EDI message parser that can be tailored to
a specific partner in the health care payment ecosystem.

About Tiger Shark
=================

TigerShark is used to transform X12 schema definitions into Plain old Python class definitions.
The class definitions are used by an application to process an X12 data stream.

TigerShark's generated code can parse X12 messages, providing Python objects that
can be used in a variety of ways. A web application can be built using any Python
framework. A Juypter Lab notebook can be built to do analysis work on claim data.
Python-based middleware can be written to process claim files.

The X12 message definitions from from the PyX12 project, see https://github.com/azoner/pyx12.

About X12 EDI
=============

See https://x12.org/products. 

The X12 syntax defines a complex more-or-less hierarchical structure
of files that have messages. Messages have Loops (that can repeat), Segments,
and individual Data Elements.

The core idea is that a Segment is a group of related Data Elements. A segment
has an identifier, making it possible to identify repeating loops 
and any omitted segments.

The segments are often terminated with a `~` and data elements terminated with `*` or `|`.
A complete schema is required, including details of fields that are optional.

See https://docs.informatica.com/data-integration/b2b-data-transformation/10-1/libraries-guide/descriptions-of-the-libraries/hipaa-library/hipaa-message-structure.html

Dependencies
============

We rely on https://github.com/azoner/pyx12 for the definition of the message.

(Ideally, we'd go to the source documents, including
the X12 standard and Implementation Guides. We don't know where to find these.)

Building the Message Classes
============================

1. Clone and check out  https://github.com/azoner/pyx12.
2. `cd tigershark3/tools`.
3. Put `tigershark` on the `PYTHONPATH` environment variable.
4. Run the `xml_extract.py` application to build the message classes.
   All of the parameters are in the `__name__ == "__main__"` block.

```shell
cd tigershar3/tools
PYTHONPATH=.. python xml_extract.py
```

Testing
=======

Complete test:

```shell
tox
```

Run marked tests with detailed logging.
Very handy for debugging.

```shell
PYTHONPATH=tigershark3 pytest -m x12parser --log-cli-level=DEBUG tests
```

Dependencies
============

This project uses [pip-tools](https://pypi.org/project/pip-tools/)
to create a detailed `requirements-dev.txt` 
from the `pyproject.toml`

```shell
pip-compile --extra=dev --extra=test -o requirements-dev.txt
```



State of the Project
====================

Version 3.0
-----------

A foundational rewrite. This uses Python type annotations to define message structure.
The ``tools/xml_extract.py`` tool converts PyX12 XML message definitions into
pure Python classes simply and directly.

It can emit a JSON Schema description of messages, also.
This permits transforming raw data to JSON for analysis and processing.


Version 0.2.5
-------------
**Lots** of 271 bugfixes! Several tests for 271 files have been added. A few
parsing bugs have been fixed.

A nice change is that the parser no longer crashes if there is an invalid code
in an X12 element. This was causing me nothing but grief so I disabled it.
Valid codes are only checked when there is a single valid code for a segment,
since this is important in determining loop boundaries for 271 files.

ParseErrors return a more helpful error message so tracking down a bad line
is much easier.

Important bugfix that prevents an early parser exit if an optional segment
isn't found, but later optional segments are present.

PyX12, which this project depends on, changed its project layout (in version
2.0.0), so the parser generation scripts have been updated to look in the new
directory.

Version 0.2.4
-------------
I discovered a bug that caused deductible/co-insurance/co-payments from being
summed if they occurred at the claims-level rather than the adjustments level.
This resulted in underreporting the *actual* amounts. This has been fixed and
unit tests have been added for this case.

I also made adjustments to the directory structure. Tests have been moved up
and the latest version of PyX12 was used to generate the parsers. An old PyX12
tarball is no longer included in this distribution, so instructions were
added to get PyX12 and set it up for parser generation.

Version 0.2.3
-------------
Initial support for reading 270/271 files. I'm not sure when I'll add support
for creating X12 files, since I have yet to need to do so. I haven't even
tested creating them.

SegmentAccess, SegmentSequenceAccess, and X12SegmentBridge now all work pretty
well. I didn't really like how the 835 facade was implemented so I spent more
time trying to figure out nicer ways of structuring the 270/271 facades. This
meant understanding and fixing the Segment[Sequence]Access classes. I was able
to avoid a bunch of ugly multiple inheritance tricks and mostly freed myself
from setting properties in __init__ (though not entirely, and I'm not sure
if I even want to totally remove this). I may clean up the 835 facade later,
but I didn't want to introduce any breaking changes in this version.

I am understanding TigerShark more and more as I continue implementing
things that S. Lott didn't get to, however this also means that I'm being
bitten by the complexity of the project more often. There are a lot of good
ideas in this project, and I keep encountering things I didn't expect
(non-sequential hierarchical level grouping in 271 files, wtf??). TigerShark
can handle most of these weird cases with minor bugfixes (which makes me more
confident that this design was right from the start), but I don't think
TigerShark can fully support 270/271 files due to their weird structuring.
I intend to re-write a good portion of TigerShark after implementing several
more formats, since I'll have a clear idea of the kind of requirements have
to be met.

Version 0.2.2a
-------------
Nothing big, just a bugfix to ElementSequenceAccess (so it actually works)
and moved two large enum types to an enums module.

Edit: Followup fix to allow unknown values in the enum x12 type, since it's
possible that an insurance company returns an outdated remark code.

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

What you see in version 0.1 is a series of hacks to get TigerShark working.
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

```sh
python setup.py install
```

Manually Generating the Parsers
-------------------------------

The `setup.py` script will install default parsers, but you might want to
generate your own, or you're fixing the generation script and need to test.
You can either convert all of the 4010 xml files in `Downloads/pyx12-1.5.0.zip`
or convert a file individually (which gives you more control over the result).

### Generating All Parsers From PyX12 archive ###

If you just want to generate all of the parsers, you can use the
`generate_all_parsers` script:

```sh
git clone https://github.com/azoner/pyx12.git
cd pyx12
python setup.py sdist --formats=gztar,zip
cd ../
python tools/generate_all_parsers.py pyx12/dist/pyx12-*.zip -d parsers
```

This will generate all parsers in a directory called `parsers`.

### Generating A Single Parser ###

You can also just create a single parser from an unzipped pyx12 source:

```sh
git clone https://github.com/azoner/pyx12.git
cd parsers
python ../tools/convertPyX12.py 835.4010.X091.A1.xml M835_4010_X091_A1.py -b ../pyx12/pyx12/map/ -n parsed_835
```

This will generate a `M835_4010_X091_A1.py` parser in your current directory.

Usage
=====

Using a Parser
--------------

```python
from tigershark.parsers import M835_4010_X091_A1
m = M835_4010_X091_A1.parsed_835
with open('/Users/sbuss/remits/95567.63695.20120314.150150528.ERA.835.edi', 'r') as f:
    parsed = m.unmarshall(f.read().strip())
```

Using a Facade
-----------------

Once you have parsed an X12 file, you can build a Facade around it:

```python
from tigershark.facade.f835 import f835_4010
f = F835_4010(parsed)
```

Now you can access the segments of the X12 file in an easy and pythonic way

```python
>>> print(f.payee.zip)
94066
>>> print(f.payer.name)
United Healthcare
>>> print(len(f.claims))
150
```

Tests
-----

If you are kind enough to create a facade, *please* add unit tests. To run
the tests that currently exist, run the following in the current directory.

```sh
python -m unittest discover
```

Note that if you first `cd tests` and then run the unit tests, they will fail
because the tests expect certain files to be in certain paths.
