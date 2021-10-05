def max_sum(N_vertices, A, B):
    if N_vertices < 1 or len(A) == 0 or len(B) == 0 or len(A) != len(B):
        return 0
    
    # create an array for count of each appearance of vertex
    vertex_count = {}
    for i in range(N_vertices):
        vertex_count[i + 1] = 0

    # count each appearance
    for i in range(len(A)):
        vertex_count[A[i]] += 1
        vertex_count[B[i]] += 1
    
    lst = list(vertex_count.values())


    print(vertex_count)
    print(lst)

    pass

def main():
    print(f'Solution for N = 5, A = [2, 2, 1, 2], B = [1, 3, 4, 4] is {max_sum(5, [2, 2, 1, 2], [1, 3, 4, 4])}, it should equal 31')
    print(f'Solution for N = 3, A = [1], B = [3] is {max_sum(3, [1], [3])}, it should equal 5')
    print(f'Solution for N = 5, A = [1], B = [3] is {max_sum(5, [1], [3])}, it should equal 9')
    print(f'Solution for N = 4, A = [1, 3], B = [2, 4] is {max_sum(4, [1, 3], [2, 4])}, it should equal 10')

    

if __name__ == '__main__':
    main()