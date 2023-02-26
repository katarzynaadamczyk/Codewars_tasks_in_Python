''' exercise proverb '''

line = 'For want of a {} the {} was lost.'
ending = 'And all for the want of a {}.'

def proverb(*args, qualifier):
    result = []
    if args:
        for arg_1, arg_2 in zip(args[:-1], args[1:]):
            result.append(line.format(arg_1, arg_2))
        if qualifier is None:
            result.append(ending.format(args[0]))
        else:
            result.append(ending.format(qualifier + ' ' + args[0]))
    return result
