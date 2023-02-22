''' exercise pascals'''

def rows(row_count):
    if row_count < 0:
        raise ValueError('number of rows is negative')
    if row_count == 0:
        return []
    result = [[1]]
    for _ in range(2, row_count + 1):
        result.append([result[-1][0]] + [a + b for a, b in zip(result[-1][:-1], result[-1][1:])] + [result[-1][-1]])
    return result

def main():
    TRIANGLE = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
]
    print(rows(0), 'should equal', TRIANGLE[:0])
    print(rows(1), 'should equal', TRIANGLE[:1])
    print(rows(5), 'should equal', TRIANGLE[:5])
    
if __name__ == '__main__':
    main()
    