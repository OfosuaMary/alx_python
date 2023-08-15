def no_c(my_string):
    no_c_string=''
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        else:
            no_c_string +=(x)
    return (no_c_string)
