def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    col = len(matrix[0])
    r=0
    c=0
    if(row*col == 0):
        print('')
    else:
     while c < col:
        while r < row:
            if r== row-1:
                print("{:d}".format(matrix[c][r])) 
            else:
             print("{:d} ".format(matrix[c][r]), end='')

            r+=1
        
        r = 0
        c+=1      
