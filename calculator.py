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
        quit_program()

# Your code goes here
def simple_calculator():
    formula_input = str(raw_input("Please enter Formula: "))
    one_integers_needed_list = ("square", "^2","cube", "^3")

    for function_type in one_integers_needed_list:
        if formula_input not in function_type:
            integer_input_1 = int(raw_input("Please Enter First Number: "))
            print "i'm printing one number"
            break
        else:
            integer_input_1 = int(raw_input("Please Enter First Number: "))
            integer_input_2 = int(raw_input("Please Enter Second Number: "))
            print "i'm printing two number"
            break

    while True:
            if formula_input == "add" or formula_input == "+":
                print add(integer_input_1, integer_input_2)
                break
            elif formula_input == "subtract" or formula_input == "-":
                print subtract(integer_input_1, integer_input_2)
                break
            elif formula_input == "multiply" or formula_input == "*":
                print multiply(integer_input_1, integer_input_2)
                break
            elif formula_input == "divide" or formula_input == "/":
                print divide(integer_input_1, integer_input_2)
                break
            elif formula_input == "square" or formula_input == "^2":
                print square(integer_input_1)
                break
            elif formula_input == "cube" or formula_input == "^3":
                print cube(integer_input_1)
                break
            elif formula_input == "power" or formula_input == "^":
                print power(integer_input_1, integer_input_2)
                break
            elif formula_input == "module" or formula_input == "%":
                print mod(integer_input_1, integer_input_2)
                break
            else:
                print "That is not a correct input"
                break
    quit_program()

simple_calculator()




