# mxctor - A LaTeX Matrix Constructor
## Usage

Run `python3 mxctor.py` and follow the instructions. In the process:

- When being prompted to enter "the type of matrix", input matrix type like `bmatrix` or use some of the special supports (see below)
- Press `Enter` without entering any value to use the default value (e.g. the default value for all entries is 0)
- The default value for matrix dimensions is 3x3, the default matrix type is `bmatrix`

Supports automatic copy to clipboard on macOS.

### Special Matrix Supports

- **Augmented Matrix**: Use `augmented` for inputting augmented matrix using `array` instead of choosing the string to be filled into the `\begin{}` clause
    - You will be prompt to enter the dividing bar position for the augmented matrix (default being before the last column)
- **Small Matrix**: Write `small` in "type of matrix field" to input inline small matrices
    - You need to provide the left and right brackets for it, default: "[]"


## To-Do-List

- Undo feature
- Copy to clipboard for other OS

