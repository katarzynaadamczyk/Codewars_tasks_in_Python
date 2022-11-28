''' exercise SGF Parsing '''

import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return 'Properties: ' + str(self.properties) + ', Kids: ' + str(self.children)


def parse_properties_old(input_string):
    properties = {}
    string_properties = re.findall(r'(\w+)((\[.*\])*)', input_string, flags=re.DOTALL)
    for property in string_properties:
        if input_string.startswith(property[0]):
            if property[0].isupper():
                if len(property[1]) == 0:
                    raise ValueError("properties without delimiter")
                values = property[1].strip('[]').split('][')
                while '' in values:
                    values.remove('')
                properties.setdefault(property[0], values)
                input_string = input_string[len(property[0]) + len(property[1]):]
            else:
                raise ValueError("property must be in uppercase")
    return properties, input_string


'''

    Newlines are removed if they come immediately after a \, otherwise they remain as newlines.
    All whitespace characters other than newline are converted to spaces.
    \ is the escape character. Any non-whitespace character after \ is inserted as-is. Any whitespace character after \ follows the above rules. Note that SGF does not have escape sequences for whitespace characters such as \t or \n.

'''

def remove_whitespaces(input_string):
    input_string = input_string.replace('\\n', '').replace('\t', ' ').replace('\\]', ']').replace('\\[', '[')
    return input_string

def parse_properties(input_string):
    properties = {}
    while not (input_string.startswith(';') or input_string.startswith('(;')) and len(input_string) > 0:
        key = ''
        while len(input_string) and input_string[0] not in '[]();':
            key += input_string[0]
            input_string = input_string[1:] 
        if key.isalpha() and key.isupper():
            if len(input_string) == 0 or input_string[0] != '[':
                raise ValueError("properties without delimiter")
            values, first_index, last_index = [], 1, 1
            while last_index < len(input_string):
                if input_string[last_index] == ']' and input_string[last_index-1:last_index+1] != '\\]':
                    property_ = remove_whitespaces(input_string[first_index:last_index])
                    values.append(property_)
                    input_string = input_string[last_index+1:]
                    last_index = 0
                    if len(input_string) == 0 or input_string[0] != '[':
                        break
                last_index += 1
            properties.setdefault(key, values)
        else:
            raise ValueError("property must be in uppercase")
    return properties, input_string
        

def parse_children(input_string):
    print(input_string)
    children = []
    no_brackets, no_square_brackets, first_index, index = 0, 0, 0, 0
    while index < len(input_string):
        if (input_string[index] == ';' or input_string[index:index+2] == '(;') and no_square_brackets == 0:
            no_brackets += 1
            index += 1
        elif input_string[index] in ');' and no_square_brackets == 0:
            no_brackets -= 1
        elif input_string[index] == '[' and input_string[index-1:index+1] != '\\[':
            no_square_brackets += 1
        elif input_string[index] == ']' and input_string[index-1:index+1] != '\\]':
            no_square_brackets -= 1
        index += 1
        if no_brackets == 0 or index == len(input_string):
            children.append(input_string[first_index:index])
            first_index = index
    return children


def parse(input_string):
    print(input_string)
    if len(input_string) < 3:
        if input_string == '()':
            raise ValueError('tree with no nodes')
        raise ValueError('tree missing')
    if input_string in ['(;)']:
        return SgfTree()
    if input_string.startswith('(;') and input_string.endswith(')'):
        input_string = input_string[2:-1]
    elif input_string.startswith(';'):
        input_string = input_string[1:]
    else:
        raise ValueError('tree missing') 
    properties, input_string = parse_properties(input_string)
    children_strings = parse_children(input_string)
    children = []
    print(children)
    for child in children_strings:
        children.append(parse(child))
    
    return SgfTree(properties, children)

def main():
    sgf = "(;A[B];B[C])"
    print(parse(sgf))

if __name__ == '__main__':
    main()
