''' exercise resistors '''

colors_to_numbers_dict = {'black': '0',
                          'brown': '1',
                          'red': '2',
                          'orange': '3',
                          'yellow': '4',
                          'green': '5',
                          'blue': '6',
                          'violet': '7',
                          'grey': '8',
                          'white': '9'}

len_to_prefix_dict = {9: 'giga',
                      6: 'mega',
                      3: 'kilo'}

def label(colors):
    if len(colors) == 0:
        return '0 ohms'
    result = ''.join([colors_to_numbers_dict.get(color, '0') for color in colors[:2]])
    zeros = '' if len(colors) < 3 else int(colors_to_numbers_dict.get(colors[2], 0)) * '0'
    result = str(int(result + zeros))
    zeros = result[result.find('0'):]
    ending = 'ohms'
    for number, name in len_to_prefix_dict.items():
        if len(zeros) >= number:
            result = result[:len(result)-number]
            ending = name + ending
            break
    return ' '.join([result, ending])
