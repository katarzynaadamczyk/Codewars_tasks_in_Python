''' my solution to task https://www.codewars.com/kata/6408ba54babb196a61d66a65'''


def the_bee(n):
    # prepare first column
    data = [[1 for _ in range(n)]]
    
    # increasing columns
    for i in range(1, n):
        tmp = [1]
        for y in range(n + i - 2):
            tmp.append(tmp[-1] + data[-1][y] + data[-1][y + 1])
        tmp.append(tmp[-1] + data[-1][-1])
        data.append(tmp)

    # decreasing columns
    for i in range(1, n):
        tmp = [sum(data[-1][:2])]
        for y in range(len(data[-1]) - 2):
            tmp.append(tmp[-1] + sum(data[-1][y + 1:y + 3]))
        data.append(tmp)
    
    return data[-1][-1]

def tests():
    print(the_bee(2), 'should equal', 11)
    print(the_bee(3), 'should equal',291)
    print(the_bee(5), 'should equal',259123)
    print(the_bee(20), 'should equal',11419120154603538332020717795)
    print(the_bee(33), 'should equal',706829476133138423874525925298446150375545319299)
    print(the_bee(50), 'should equal',61068096560504518254246449553519425203436341865056944755649047832571626123)
   
if __name__ == '__main__':
    tests()
    