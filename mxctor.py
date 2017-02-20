# Created by VVVFO on Feb 20 2017

import os

# prompting for the number of rows and columns
rows = int(input("Rows: "))
cols = int(input("Columns: "))
mattype = (input("Type of matrix (default: bmatrix): ") or "bmatrix")

# constructing the opening and ending text
intro = "\\begin{{{}}}\n".format(mattype)
outro = "\\end{{{}}}".format(mattype)

# If the format selected is augmented matrix, override the above intro and outro
if mattype == "augmented":    
    intro = "\\left[\\begin{{array}}{{{}|c}}\n".format("c" * (cols - 1))
    outro = "\\end{array}\\right]"

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

