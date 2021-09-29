def big(a,b,c):
    if(a>b) and (a>c):
        print("a is bigger")
        large=a
    elif(b>c)and (b>a):
        print("b is bigger")
        large=b
    else:
        print("c is bigger")
        large=c
        return large
print(big(22,5,99))
