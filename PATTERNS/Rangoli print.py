import string
def print_rangoli(size):
    alpha = string.ascii_lowercase

    if size>0 and size<=27:
        L = []

        for i in range(size):
            str = "-".join(alpha[i:n])
            L.append(str[::-1]+str[1:])

        width = len(L[0])

        for i in range(n-1, 0, -1):
            print(L[i].center(width, "-"))

        for i in range(n):
            print(L[i].center(width, "-"))

    else:
        print("Enter a valid number between 0 to 28")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
