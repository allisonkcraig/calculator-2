"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def quit_program():
    answer = str(raw_input("Quit? Y or N"))
    if answer == "y" or answer == "Y":
        print "Goodbye!"
        return 
    elif answer == "n" or answer == "N":
        simple_calculator()
    else:
        print "That is not an answer, MAKE UP YOUR MIND"

# Your code goes here
def simple_calculator():
    formula_input = str(raw_input("Please enter Formula: "))
    interger_input_1 = int(raw_input("Please Enter First Number: "))
    interger_input_2 = int(raw_input("Please Enter Second Number If Applicable: "))

    while True:
            if formula_input == "add":
                print add(interger_input_1, interger_input_2)
                break
            elif formula_input == "subtract":
                print subtract(interger_input_1, interger_input_2)
                break
            elif formula_input == "multiply":
                print multiply(interger_input_1, interger_input_2)
                break
            elif formula_input == "divide":
                print divide(interger_input_1, interger_input_2)
                break
            elif formula_input == "square":
                print square(interger_input_1, interger_input_2)
                break
            elif formula_input == "cube":
                print cube(interger_input_1, interger_input_2 == None)
                break
            elif formula_input == "power":
                print power(interger_input_1, interger_input_2)
                break
            elif formula_input == "module":
                print mod(interger_input_1, interger_input_2)
                break
            else:
                print "That is not a correct input"
                break
    print "Awesome! Go Again! Type 'q' to quit"
    quit_program()

simple_calculator()




