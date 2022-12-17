if __name__ == "__main__":
    x = input().split()
    n = int(x[0])
    m = int(x[1])
    a,b,c ="-",".|.","WELCOME"

    l=((n-1)//2)+1
    for i in range(1,l):
        print((b*((2*i)-1)).center(m,a))

    print(c.center(m,a))

    for i in range(0,l-1):
        print(((n-2-(2*i))*b).center(m,a))
