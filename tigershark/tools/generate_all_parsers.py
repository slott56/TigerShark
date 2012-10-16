#!/usr/bin/python
"""
Generate all parsers from PyX12-1.5.0.zip

Example Usage:
    python generate_all_parsers.py ../../Downloads/pyx12-1.5.0.zip
"""
import argparse
import fnmatch
import logging
import os
import sys
import zipfile

from tigershark.tools import convertPyX12


def convert_from_zip(zip_file_path, dest_path, structure):
    """ Convert all of the xml files in a zip. """
    zipf = zipfile.ZipFile(zip_file_path)

    filenames = [f for f in zipf.namelist() if "map" in f and "xml" in f]
    pyx12_version_str = filenames[0].split("/", 1)[0]
    for filename in filenames:
        if fnmatch.fnmatch(filename.rsplit('/', 1)[1],
                "[0-9][0-9][0-9]*.4010.X*.xml"):
            try:
                data_ele_file = zipf.open("{pyx12}/pyx12/map/dataele.xml".format(
                    pyx12=pyx12_version_str))
                codes_file = zipf.open("{pyx12}/pyx12/map/codes.xml".format(
                    pyx12=pyx12_version_str))
                spec_file = zipf.open(filename)
                dest_fname = os.path.join(dest_path, "M%s.py") % \
                        filename.rsplit('/', 1)[1].rsplit('.', 1)[0].\
                        replace(".", "_")
                parser_name = "parsed_%s" % \
                        filename.rsplit('/', 1)[1].split('.', 1)[0]

                logging.info("Converting file: {filename} to {dest}".format(
                    filename=filename, dest=dest_fname))
                convertPyX12.writeFile(dest_fname, parser_name,
                    convertPyX12.convertFile(spec_file, data_ele_file,
                        codes_file),
                    structure=structure)
                # ZipFile file-like objects don't support seek, so we have to
                # close and re-open them every time :\
                spec_file.close()
                data_ele_file.close()
                codes_file.close()
            except Exception as e:
                raise e
                logging.error(e)

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    parser = argparse.ArgumentParser(
        description="Convert all PyX12 XML files to python modules.")
    parser.add_argument('zip_file_path', help="The path to the zip file "\
            "containing the pyX12 X12 spec files to convert")
    parser.add_argument('-d', '--destination_path', default="parsers",
            help="The destination path. Defaults to './parsers/'.")
    parser.add_argument('-s', '--structure', choices=['flat', 'nested'],
            default="flat", help="The structure of the resulting python "\
                    "class. Nested is easier to read, but may not compile "\
                    "due to too many object instantiations in a single "\
                    "call.")
    args = parser.parse_args()
    try:
        os.makedirs(args.destination_path)
    except:
        pass
    convert_from_zip(args.zip_file_path, args.destination_path, args.structure)
