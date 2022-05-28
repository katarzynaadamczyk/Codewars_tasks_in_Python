''' exercise wordy '''

import re


def answer(question):
    number_regex = re.compile(r'[0-9]+')
    question_regex = re.compile(r'^What is ([0-9]+)(.*([0-9]+))*\?$')
    numbers = number_regex.findall(question)
    if not question_regex.match(question):
        raise ValueError('unknown operation')
    result = int(numbers[0])
    operations_regex = re.compile(r'(plus|minus|multiplied by|divided by) ([0-9]+)')
    operations = operations_regex.findall(question)
    if len(operations) + 1 != len(numbers):
        raise ValueError('syntax error')
    for operation, value in operations_regex.findall(question):
        if operation == 'plus':
            result += int(value)
        elif operation == 'minus':
              
    
    return result


if __name__ == '__main__':
    print(answer('What is 5?'))
    print(answer('What is 5 plus 5?'))
    print(answer('What is 5 plus 5 plus 10?'))
    try:
        print(answer('Who is the president?'))
    except ValueError as e:
        print(e.args)