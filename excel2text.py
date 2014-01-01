#! /usr/bin/python
# excel2text.py
# A simple program to convert Excel files to text with user-defined delimiters.
#
# Copyright (C) 2013 copyright Jacob Malcom, jacob.malcom@utexas.edu

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import os
import sys
import xlrd

def main():
    """
    Convert Excel files to text.

    USAGE:
        excel2text <infile> <delimiter>
    ARGS:
        infile, an Excel workbook of .xls or .xlsx format
        delimiter, one of 'tab', 'comma', or 'space'
    RETURNS:
        One text file per worksheet in the infile
    COMMENTS:
        Writes one output file per worksheet (tab) with user-defined field
        delimiters, with file base name from the worksheet name. The file suffix
        is .csv (delimiter= 'comma'), .tab (= 'tab'), or .txt (= 'space').
    """
    delim, suffix = get_suffix_delim()
    outbase = infile.split(".")[0] + "_files/"
    if not os.path.exists(outbase):
        os.mkdir(outbase)
    process_file(suffix, delim, outbase)

def process_file(suffix, delim, outbase):
    """Read Excel row-by-row and write each sheet to file."""
    fil = xlrd.open_workbook(infile)
    for sheet in fil.sheet_names():
        cur_sheet = fil.sheet_by_name(sheet)
        new_fil = outbase + sheet + suffix
        with open(new_fil, 'wb') as out:
            for j in range(cur_sheet.nrows):
                to_write = []
                for k in range(len(cur_sheet.row(j))):
                    to_write.append(cur_sheet.cell_value(j,k))
                to_write = [str(x) for x in to_write]
                out.write(delim.join(to_write) + "\n")

def get_suffix_delim():
    """Return outfile suffix give delimiter from argv."""
    if delimiter == "tab":
        return "\t", ".tab"
    elif delimiter == "comma":
        return ",", ".csv"
    elif delimiter == "space":
        return " ", ".txt"
    else:
        print "Please use 'tab', 'comma' or 'space' as delimiters."
        sys.exit(2)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print main.__doc__
        sys.exit()
    infile = sys.argv[1]
    delimiter = str(sys.argv[2])
    main()
