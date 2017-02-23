#!/usr/bin/env python3
# Created by VVVFO on Feb 20 2017

import os

# prompting for the number of rows and columns
mattype = (input("Type of matrix (default: bmatrix): ") or "bmatrix")
rows = int(input("Rows: ") or "3")
cols = int(input("Columns: ") or "3")

if mattype == "augmented":
    # if we are creating an augmented matrix (then use array)
    dividing_position = int(input("Dividing position (starts from 0): ") or "{:d}".format(cols-1))
    intro = "\\left[\\begin{{array}}{{{}|{}}}\n".format("c" * (dividing_position), "c" * (cols - dividing_position))
    outro = "\\end{array}\\right]"
elif mattype == "small":
    # if we are creating a small matrix
    left_bracket = input("Enter left bracket (\"[\"): ") or "["
    right_bracket = input("Enter right bracket (\"]\"): ") or "]"
    intro = "{}\\begin{{smallmatrix}}\n".format(left_bracket)
    outro = "\\end{{smallmatrix}}{}".format(right_bracket)
else:
    # constructing the opening and ending text for default matrices
    intro = "\\begin{{{}}}\n".format(mattype)
    outro = "\\end{{{}}}".format(mattype)

# create an empty string for storing the main text body
body = ""

# main looping part, as the last entry doesn't need the ampersand, and the last line does not need \\, they are taken separately
for r in range(rows - 1):
    body = body + "    "
    for c in range(cols - 1):
        body = body + (input("({}, {}): ".format(r+1,c+1)) or "0") + " & "
    body = body + (input("({}, {}): ".format(r+1, cols)) or "0")
    body = body + "\\\\\n"
body = body + "    " # indent the body part
for c in range(cols - 1):
    body = body + (input("({}, {}): ".format(rows,c+1)) or "0") + " & "
body = body + (input("({}, {}): ".format(rows, cols)) or "0")
body = body + "\n"

output = "{}{}{}".format(intro,body,outro)
print("\n"+output)

# trying to copy to clipboard (in macOS)
# first creating an escaped version of the output
escaped_output = output
for ch in ['\\']:
    if ch in escaped_output:
        escaped_output = escaped_output.replace(ch, "\\"+ch)

# check the status of copying and give feedback
return_value = os.system("echo '{}' | pbcopy".format(escaped_output))
if return_value == 0:
    print("\nSuccessfully copied to clipboard!")
else:
    print("\nCopy to clipboard failed")

