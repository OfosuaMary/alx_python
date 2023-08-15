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
            print("{:d} ".format(matrix[c][r]), end='')
            r+=1
        print('')
        r = 0
        c+=1      
