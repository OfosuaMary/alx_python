count = 0
while count <= 9:
    count1 = 0
    while count1 <= 9:
     print("{}{}".format(count,count1), end='')
     if count == 9 and count1 == 9:
        print(' ')
        break
     print(",",end='')
     
     count1 += 1
    count += 1

