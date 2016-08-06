# BFPrinter

This is a straightforward, tiny script that takes an input string and creates a program
in the BrainFu*k programming language that prints that string.

This is done through incrementing the value at the pointer based on the character's
ascii value and then incrementing the pointer. The inherent limitation is BrainFu*k's
30,000 Byte limitation, so no more than 30,000 characters can be printed.

