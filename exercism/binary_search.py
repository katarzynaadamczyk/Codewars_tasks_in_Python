''' exercise binary search '''

def find(search_list, value):
    if search_list[0] == value:
        return 0
    if search_list[-1] == value:
        return len(search_list) - 1
    min_index = 0
    max_index = max(len(search_list) - 1, 0)
    while min_index != max_index:
        mid_index = (max_index + min_index) // 2
        print(search_list[mid_index])
        if search_list[mid_index] == value:
            return mid_index
        if search_list[mid_index] < value:
            if mid_index == min_index:
                break
            min_index = mid_index
        else:
            if max_index == min_index:
                break
            max_index = mid_index
    raise ValueError("value not in array")

if __name__ == '__main__':
    print('result:', find([1, 3, 4, 6, 8, 9, 11], 6), 3)
    print('result:', find([6], 6), 0)
    print('result:', find([1, 3, 4, 6, 8, 9, 11], 1), 0)
    print('result:', find([1, 3, 4, 6, 8, 9, 11], 11), 6)
    print('result:', find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 144), 9)
    print('result:', find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21), 5)
    print('result:', find([1, 3, 4, 6, 8, 9, 11], 7))