"""if __name__ == '__main__':
    n = int(input())
    list1=[]
    temp=[]
for i in range(n):
    cmd=str(input(''))
    if cmd=='insert':
        a=int(input(""))
        b=int(input(""))
        temp=list1.insert(a,b)
    elif cmd=='print':
        print(temp)
    elif cmd=='remove':
        a=int(input(""))
        temp=list1.remove(a)
    elif cmd=='append':
        a=int(input(""))
        temp=list1.append(a)
    elif cmd=='sort':
        temp=list1.sort()
    elif cmd=='pop':
        temp=list1.pop()
    elif cmd=='reverse':
        temp=list1.reverse()
"""

"""
if __name__ == '__main__':
    L=[]
    N = int(input())
    for i in range(0,N):
        a=input().split(" ")
        if a[0]=="insert":
            L.insert(int(a[1]),int(a[2]))
        elif a[0]=="remove":
            L.remove(int(a[1]))
        elif a[0]=="append":
            L.append(int(a[1]))
        elif a[0]=="sort":
            L.sort()
        elif a[0]=="pop":
            L.pop()
        elif a[0]=="reverse":
            L.reverse()
        elif a[0]=="print":
            print(L)
"""

"""
class Person:
    def __init__(self,initialAge):
         # Add some more code to run some checks on initialAge
        self.age = 0
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age<13 :
            print("You are young.")
        elif (13 <= age <18):
            print("You are a teenager.")
        elif age >= 18:
            print("You are old.")

    def yearPasses(self):    
        # Increment the age of the person in here
        global age
        age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
"""

# for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])


"""
for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])
"""



"""
#upper to lower

def swap_case(s):
    a =[]
    for i in s:
        if i.isupper():
            a+=(i.lower())
        else:
            a+=(i.upper())

        # listToStr = ''.join([str(elem) for elem in a])
        listToStr = ''.join(map(str, a))
    return listToStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
"""


"""
# ABCDCDC
# CDC                      GROUP OF 3 FROM STRING 5 TIMES

count =0
for i in range(0,len(string)-len(sub_string)+1):   #7-3+1=5
    try:
        if string[i:i+len(sub_string)]==sub_string:    #[0:3]==CDC,[1:4]==CDC,[2:5]==CDC,[3:6]==CDC,[4:7]==CDC.      5 TIMES
            count+=1
    except IndexError:
        break
return count

"""

"""
my_solution
def count_substring(string, sub_string):
    count =0
    l1=len(string)
    l2=len(sub_string)
    for i in range(0,l1-l2+1):  
        if string[i:i+l2]==sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

"""

#  count = 0
#     for n in range (len(string),0,-1):                         #READS FROM RIGHT TO LEFT THATS NOT IN Q.
#         try :
#             if string[n-len(sub_string):n] == sub_string :           
#                 count +=1
#         except IndexError : break

"""
def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            flag=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    return count

"""