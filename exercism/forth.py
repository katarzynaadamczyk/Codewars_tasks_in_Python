''' exercise forth '''

import re

# subclassing the Exception to create a StackUnderflowError
class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


def check_stackunderflow(stack, num=2):
    if len(stack) < num:
        raise StackUnderflowError("Insufficient number of items in stack")


def raise_divisionerror():
    raise ZeroDivisionError("divide by zero")


def raise_undefinedoperationerror():
    raise ValueError("undefined operation")


def add(stack):
    check_stackunderflow(stack)
    return stack[:-2] + [stack[-1] + stack[-2]]
        
        
def substract(stack):
    check_stackunderflow(stack)
    return stack[:-2] + [stack[-2] - stack[-1]]


def multiply(stack):
    check_stackunderflow(stack)
    return stack[:-2] + [stack[-1] * stack[-2]]


def divide(stack):
    check_stackunderflow(stack)
    if stack[-1] == 0:
        raise_divisionerror()
    return stack[:-2] + [stack[-2] // stack[-1]]


def dup(stack):
    check_stackunderflow(stack, 1)
    return stack + [stack[-1]]


def drop(stack):
    check_stackunderflow(stack, 1)
    return stack[:-1]


def swap(stack):
    check_stackunderflow(stack)
    return stack[:-2] + [stack[-1], stack[-2]]


def over(stack):
    check_stackunderflow(stack)
    return stack + [stack[-2]]


def create_command_table():
    table = {'+': add, '-': substract, '*': multiply, '/': divide,
             'dup': dup, 'drop': drop, 'swap': swap, 'over': over}
    return table


def add_new_command(line, table):
    # TODO
    return table

def evaluate(input_data):
    command_table = create_command_table()
    stack = []
    for line in input_data:
        line = line.lower()
        if re.match(r'^: .* ;$', line):
            command_table = add_new_command(line, command_table)
        else:
            for command in line.split():
                if re.match(r'-?\d+', command):
                    stack.append(int(command))
                elif command in command_table.keys():
                    stack = command_table[command](stack)
                else:
                    raise_undefinedoperationerror()
    return stack
