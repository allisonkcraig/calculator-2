"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def simple_calculator():
    """Simple calculator for small computations"""
    input_math = str(raw_input("What is your math?"))
    token = input_math.rstrip()
    token = input_math.split(" ")
    token[1] = int(token[1])
    token[2] = int(token[2])
    while True:
        if token[0] == "q" or token[0] == "Q":
            print "Goodbye!"
            return 
        else:
            if token[0] == "add":
                print add(token[1], token[2])
                return
            elif token[0] == "subtract":
                print subtract(token[1], token[2])
                return
            elif token[0] == "multiply":
                print multiply(token[1], token[2])
                return
            elif token[0] == "divide":
                print divide(token[1], token[2])
                return
            elif token[0] == "square":
                print square(token[1], token[2])
                return
            elif token[0] == "cube":
                print cube(token[1])
                return
            elif token[0] == "power":
                print power(token[1], token[2])
                return
            elif token[0] == "mod":
                print mod(token[1], token[2])
                return
            else:
                print "That is not a correct input"
                return
    
    simple_calculator()

simple_calculator()




