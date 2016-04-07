"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


def calculator():
    while True: 
        string_list = raw_input("This is Siri, please give me a mathematical command ").split()
        if string_list[0] == "+":
            print add(int(string_list[1]),int(string_list[2]))
        elif string_list[0] == "-":
            print subtract(int(string_list[1]),int(string_list[2]))
        elif string_list[0] == "*":
            print multiply(int(string_list[1]),int(string_list[2]))
        elif string_list[0] == "/":
            print divide(int(string_list[1]),int(string_list[2]))
        elif string_list[0] == "square":
            print square(int(string_list[1]),int(string_list[2]))
        elif string_list[0] == "cube":
            print cube(int(string_list[1]))
        elif string_list[0] == "pow":
            print power(int(string_list[1]),int(string_list[2]))
        elif string_list[0] == "mod":
            print mod(int(string_list[1]),int(string_list[2]))
        elif string_list[0] == "q":
            break

calculator()