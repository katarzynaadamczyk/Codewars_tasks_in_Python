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


def parse_properties(input_string):
    properties = {}
    string_properties = re.findall(r'(\w+)((\[\w*\])*)', input_string)
    for property in string_properties:
        if input_string.startswith(property[0]):
            if property[0].isupper():
                if len(property[1]) == 0:
                    raise ValueError("properties without delimiter")
                values = property[1].strip('[]').split('][')
                values.remove('') # ERROR
                properties.setdefault(property[0], values)
                input_string = input_string[len(property[0]) + len(property[1]):]
            else:
                raise ValueError("property must be in uppercase")
    return properties, input_string

def parse_children(input_string):
    children = []
    # TODO
    return children


def parse(input_string):
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
    for child in children_strings:
        children.append(parse(child))
    return SgfTree(properties, children)

def main():
    sgf = 'A[]'
    print(parse_properties(sgf))

if __name__ == '__main__':
    main()
