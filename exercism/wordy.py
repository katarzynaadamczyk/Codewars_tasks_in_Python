''' 
exercise wordy 

explanation of my idea:
first check if question is for sure What is ...?
then check how many numbers there are in the text
text_regex - check if in the text there are appropriate words only (what is and names of operations)
first if -> check if there is match with question regex and if there are only appropriate words in the question
if no -> unknown operation
second if -> check if there is at least one number in the text
if no -> syntax error
operation_regex -> number name_of_operation number
shorten question to only operations
take first operation and make appropriate operation, 
if there is none -> return syntax error until there is only last number left in the question

'''

import re

def plus(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 != 0:
        return number1 // number2
    raise ValueError('syntax error')
    
operations = {'plus': plus, 
              'minus': minus, 
              'multiplied by': multiply, 
              'divided by': divide}

lst_of_words = ['^What is', 'raised to the', 'th power', 'st power', 'nd power', 'rd power'] 

def answer(question):
    number_regex = re.compile(r'-?[0-9]+')
    question_regex = re.compile(r'^What is.*\?')
    texts_regex = re.compile('|'.join(lst_of_words + list(operations.keys()))) 
    numbers = number_regex.findall(question)
    if not question_regex.match(question) or ' '.join(texts_regex.findall(question)) != ' '.join(re.findall(r'[A-Za-z]+', question)):
        raise ValueError('unknown operation')
    if len(numbers) == 0:
        raise ValueError('syntax error')
    result = int(numbers[0])
    operations_regex = re.compile(r'(-?[0-9]+) (' + '|'.join(operations.keys()) + ') (-?[0-9]+)')
    question = question[len('What is '):-1]
    while len(question) > len(numbers[-1]):
        operation = operations_regex.findall(question)
        if operation and operation[0][1] in operations.keys():
            result = operations[operation[0][1]](result, int(operation[0][2]))
            question = question[len(' '.join(operation[0][:-1]))+1:]
        else:
            operation = re.findall(r'(-?[0-9]+) (raised to the) (-?[0-9]+)(st|nd|rd|th) (power)', question)
            if operation:
                result = result ** int(operation[0][2])
                question = operation[0][2] + question[len(' '.join(operation[0])) - 1:]
                print(question)
            else:
                raise ValueError('syntax error')
    return result

if __name__ == '__main__':
    print('What is 5?')
    print(answer('What is 5?'))
    print('What is 5 plus 5?')
    print(answer('What is 5 plus 5?'))
    print('What is 5 plus 5 plus 10?')
    print(answer('What is 5 plus 5 plus 10?'))
    print("What is 7 plus multiplied by -2?")
    try:
        print(answer("What is 7 plus multiplied by -2?"))
    except ValueError as e:
        print(e.args)
    print('Who is the president?')
    try:
        print(answer('Who is the president?'))
    except ValueError as e:
        print(e.args)
    print("What is 2 2 minus 3?")
    try:
        print(answer("What is 2 2 minus 3?"))
    except ValueError as e:
        print(e.args)
    print('What is 2 raised to the 5th power plus 10?')
    try:
        print(answer('What is 2 raised to the 5th power plus 10?'))
    except ValueError as e:
        print(e.args)
        