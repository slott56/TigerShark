import os
from distutils.core import setup
from distutils.command.build_py import build_py
import fnmatch
import logging
import zipfile

from tigershark import __version__


class GenerateParsers(build_py):
    def run(self):
        build_py.run(self)
        from tigershark.tools import convertPyX12

        def convert(filename):
            data_ele_file = zipf.open("pyx12-1.5.0/map/dataele.xml")
            codes_file = zipf.open("pyx12-1.5.0/map/codes.xml")
            fname = "M%s.py" % filename.rsplit('/', 1)[1].rsplit('.', 1)[0].\
                        replace(".", "_")
            dest_fname = os.path.join(self.build_lib, "tigershark", "parsers",
                    fname)
            parser_name = "parsed_%s" % \
                    filename.rsplit('/', 1)[1].split('.', 1)[0]
            convertPyX12.writeFile(dest_fname, parser_name,
                convertPyX12.convertFile(zipf.open(filename), data_ele_file,
                    codes_file))
            # ZipFile file-like objects don't support seek, so we have to
            # close and re-open them every time :\
            data_ele_file.close()
            codes_file.close()

        zipf = zipfile.ZipFile("Downloads/pyx12-1.5.0.zip")

        filenames = [f for f in zipf.namelist() if "map" in f and "xml" in f]
        for filename in filenames:
            if fnmatch.fnmatch(filename.rsplit('/', 1)[1],
                    "[0-9][0-9][0-9]*.4010.X*.xml"):
                print(filename)
                try:
                    convert(filename)
                except Exception as e:
                    raise e
                    print(e)
                    logging.error(e)


setup(
    name='TigerShark',
    version=__version__,
    description='TigerShark: An X12 file parser.',
    long_description='TigerShark is an X12 EDI message parser that can be '\
            'tailored to a specific partner in the health care payment '\
            'ecosystem.',
    author='Steven Buss & Steven Lott',
    author_email='steven.buss@gmail.com',
    download_url='https://github.com/sbuss/TigerShark/tarball/v%s' % \
            __version__,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
    ],
    packages=[
        'tigershark',
        'tigershark.extras',
        'tigershark.facade',
        'tigershark.parsers',
        'tigershark.tests',
        'tigershark.tools',
        'tigershark.X12',
        'tigershark.X12.map',
        'tigershark.X12.message',
    ],
    scripts=[
        'tigershark/tools/convertPyX12.py',
    ],
    package_data={'tigershark': ['tests/*.txt', 'tests/*.xml', 'tests/*.csv']},
    cmdclass={"build_py": GenerateParsers},
)
