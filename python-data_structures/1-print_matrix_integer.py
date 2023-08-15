def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    col = len(matrix[0])
    r=0
    c=0
    if(row*col == 0):
        print(' ')
    else:
     while c < col:
        while r < row:
            print("{} ".format(matrix[c][r]), end='')
            r+=1
        print('')
        r = 0
        c+=1      


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
print("--")
print_matrix_integer()