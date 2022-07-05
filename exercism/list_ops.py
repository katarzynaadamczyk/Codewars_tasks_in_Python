''' exercise list ops '''

def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    while len(lists):
        upper_level, item = lists, lists[0]
        while isinstance(item, type(lists)) and len(item) > 0:
            upper_level = item
            item = item[0]
        if not isinstance(item, type(lists)):
            result.append(item)
        upper_level.remove(item)
    return result
 

def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    return len(list)


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    if list:
        result = list[0]
        for index in range(1, len(list)):
            result = function(result, list[index])
        initial = function(result, initial)
    return initial


def reverse(list):
    return list[::-1]


if __name__ == '__main__':
    print(concat([[[1], [2]], [[3]], [[]], [[4, 5, 6]]]))
    lst = [1, 2, 3, 1, 1, 1]
    lst.remove(1)
    print(lst)