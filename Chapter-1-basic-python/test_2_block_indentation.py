"""
    Python uses indentation to define control and loop constructs.
    You need to pay close attention to the use of whitespace it could result in code that behaves in unexpected ways.

    Python uses the colon symbol (:) and indentation for showing where blocks of code begin and end.
    That is, blocks in Python, such as functions, loops, if clauses and other constructs, have no ending identifiers.
    All blocks start with a
    colon and then contain the indented lines below it.

    always use 4 spaces for indentation.
"""
a, b = 1, 2
if a > b:       # If block starts here
    print(a)    # This is part of the if block
else:           # else must be at the same level as if
    print(b)    # This line is part of the else block
