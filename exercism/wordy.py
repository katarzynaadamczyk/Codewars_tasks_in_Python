''' exercise wordy '''

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

def answer(question):
    number_regex = re.compile(r'-?[0-9]+')
    question_regex = re.compile(r'^What is.*\?')
    texts_regex = re.compile('|'.join(['^What', 'is'] + list(operations.keys()))) # rozdzielić by
    numbers = number_regex.findall(question)
    texts = texts_regex.findall(question)
    print(texts)
    print((re.findall(r'[A-Za-z]+', question)))
    if not question_regex.match(question) or len(texts) != len(re.findall(r'[A-Za-z]+', question)):
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
            raise ValueError('syntax error')
    return result

if __name__ == '__main__':
    print(answer('What is 5?'))
    print(answer('What is 5 plus 5?'))
    print(answer('What is 5 plus 5 plus 10?'))
    try:
        print(answer("What is 7 plus multiplied by -2?"))
    except ValueError as e:
        print(e.args)
    try:
        print(answer('Who is the president?'))
    except ValueError as e:
        print(e.args)
    try:
        print(answer("What is 2 2 minus 3?"))
    except ValueError as e:
        print(e.args)