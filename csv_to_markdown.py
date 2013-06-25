#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Export the list of movies from CSV format to Markdown.

Usage: csv_to_markdown.py showing_history.csv
    The output will be written into README.md
"""

# Copyright © 2013 Qiaoyong Zhong <solary.sh@gmail.com>
# Last modified: Jun 25, 2013

import csv, sys, datetime

def main():
    """The main function.
    """
    if len(sys.argv) < 2:
        print('Usage: {} file.csv'.format(sys.argv[0]))
        return

    outfile = open('README.md', 'w')
    outfile.write('''\
# Friday Cinema

Here is the list of movies shown by *Friday Cinema* in PICB:

''')

    with open(sys.argv[1], newline='') as f:
        year = 0
        reader = csv.reader(f)
        for row in reader:
            current_year = datetime.datetime.strptime(row[0], '%Y-%m-%d').year
            if current_year != year:
                year = current_year
                outfile.write('- **Year {:d}**\n'.format(year))
            if len(row) >= 2: # Emphasize the English name
                row[1] = '*{}*'.format(row[1])
            if len(row) >= 4: # Parenthesize the year
                row[3] = '({})'.format(row[3])
            outfile.write('    - {}\n'.format(' '.join(row)))

    outfile.close()

if __name__ == "__main__":
    main()
