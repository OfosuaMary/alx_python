count = 0
while count <= 9:
    count1 = 0
    while count1 <= 9:
     print("{}{}".format(count,count1), end='')
     if count != 9 or count1 != 9:
        print(",",end='')
     else:
        break
     count1 += 1
    count += 1

print(' ')