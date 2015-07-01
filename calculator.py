"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def simple_calculator():
    input_math = str(raw_input("What is your math?"))
    token = input_math.rstrip()
    token = token.split(" ")
    while True:
        if token[0] == "q" or "Q":
            print "Goodbye!"
            return 
        else:
            if token[0] == "add":
                print add(token[1], token[2])
            elif token[0] == "sub":
                print subtract(token[1], token[2])
            elif token[0] == "multiply":
                print multiply(token[1], token[2])
            elif token[0] == "divide":
                print divide(token[1], token[2])
            elif token[0] == "square":
                print square(token[1], token[2])
            elif token[0] == "cube":
                print cube(token[1])
            elif token[0] == "power":
                print power(token[1], token[2])
            elif token[0] == "mod":
                print mod(token[1], token[2])
            else:
                print "That is not a correct input"

                




