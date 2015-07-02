"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def simple_calculator():
    input_math = str(raw_input("Please enter formula type and up to 2 int"))
    token = input_math.rstrip()
    token = input_math.split(" ")

    for parts in token:
        placeholder = len(token)

    while True:
        if token[0] == "q" or token[0] == "Q":
            print "Goodbye!"
            return 
        else:
            # token[1] = int(token[1])
            # token[2] = int(token[2])
            if token[0] == "add":
                print add(int(token[1]), int(token[2]))
                break
            elif token[0] == "subtract":
                print subtract(int(token[1]), int(token[2]))
                break
            elif token[0] == "multiply":
                print multiply(int(token[1]), int(token[2]))
                break
            elif token[0] == "divide":
                print divide(int(token[1]), int(token[2]))
                break
            elif token[0] == "square":
                print square(int(token[1]), int(token[2]))
                break
            elif token[0] == "cube":
                print cube(int(token[1]))
                break
            elif token[0] == "power":
                print power(int(token[1]), int(token[2]))
                break
            elif token[0] == "module":
                print mod(int(token[1]), int(token[2]))
                break
            else:
                print "That is not a correct input"
                break
    print "Awesome! Go Again! Type 'q' to quit"
    simple_calculator()

simple_calculator()




