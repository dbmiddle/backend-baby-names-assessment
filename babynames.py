#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract the year and print it
 - Extract the names and rank numbers and just print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a single list starting
    with the year string followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    names = []
    with open(filename) as f:
        names_dict = {}
        contents = f.read()
        year = re.search(r'Popularity\s*in\s*(\d\d\d\d)', contents)
        names.append(year.group(1))
        # print(names)
        rank_and_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', contents)
        # print(rank_and_names)
        for name_data in rank_and_names:
            for name in name_data[1:]:
                if name not in names_dict:
                    names_dict[name] = name_data[0]
                    names.append('{} {}'.format(name, name_data[0]))
        names = sorted(names)
        # print(names)
        # print(names_dict)
    return names


def summarize(filename):
    with open(filename + '.summary', 'w') as f:
        text = '\n'.join(extract_names(filename)) + '\n'
        f.write(text)


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser(description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # extract_names('baby1994.html')
    # Create a command-line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command-line arguments into a NAMESPACE called 'ns'
    ns = parser.parse_args(args)
    file_list = ns.files
    file_list = ''.join(file_list)
    summary = ns.summaryfile

    if not ns:
        parser.print_usage()
        sys.exit(1)
    elif summary:
        summarize(file_list)
    else:
        print(extract_names(file_list))

    # # option flag
    # create_summary = ns.summaryfile

    # # For each filename, call `extract_names` with that single file.
    # # Format the resulting list a vertical list (separated by newline \n)
    # # Use the create_summary flag to decide whether to print the list,
    # # or to write the list to a summary file e.g. `baby1990.html.summary`

    # # +++your code here+++


if __name__ == '__main__':
    main(sys.argv[1:])
