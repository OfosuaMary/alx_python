def fibonacci_sequence(n):
    a=0
    b=1
    c=[]
    if n==1:
        c= [0]
    elif n==2:
        c= [0,1]
    elif n>2:
        c= [0,1]
        i=3
        while i<=n:
            d=a+b
            c.append(d)
            a=b
            b=d
            i+=1
    return c
print(fibonacci_sequence(1))

