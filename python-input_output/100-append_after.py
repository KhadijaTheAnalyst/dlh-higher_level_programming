#!/usr/bin/python3
"""Module for appending text to files"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string"""
    with open(filename, 'r', encoding='utf-8') as f:           # 1. OPEN & READ
        lines = f.readlines()

    new_lines = []                           # 2. CREATE EMPTY LIST
    for line in lines:                       # 3. LOOP
        new_lines.append(line)               # 4a. ADD ORIGINAL
        if search_string in line:            # 4b. CHECK MATCH
            new_lines.append(new_string)  # 4c. ADD NEW

    with open(filename, 'w', encoding='utf-8') as f:           # 5. WRITE
        f.writelines(new_lines)
