from distutils.core import setup

from tigershark import __version__


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
        'tigershark.facade.enums',
        'tigershark.parsers',
        'tigershark.tools',
        'tigershark.X12',
        'tigershark.X12.map',
        'tigershark.X12.message',
    ],
    scripts=[
        'tigershark/tools/convertPyX12.py',
        'tigershark/tools/generate_all_parsers.py',
    ],
    package_data={'tigershark': ['tests/*.txt', 'tests/*.xml', 'tests/*.csv']},
)
