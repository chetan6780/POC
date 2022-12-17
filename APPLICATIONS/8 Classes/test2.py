# def D(s):
#     i = 0
#     while i < len(s):
#         if ((ord(s[i]) < ord('A') or ord(s[i]) > ord('Z')) and (ord(s[i]) < ord('a') or ord(s[i]) > ord('z'))):
#             del s[i]
#             i -= 1
#         i += 1
#     A="".join(s)
#     print (A)
#     return A

# s = input("Input string: ")
# k= input("Input string: ")

# s = [i for i in s]
# k= [i for i in k]

# p=D(s)
# y=D(k)

# if p==y:
# 	print("\nBoth are same strings")
# else:
# 	print("\nBoth are different strings")


def D(s):
    i = 0
    while i < len(s):
        if ((ord(s[i]) < ord('A') or ord(s[i]) > ord('Z')) and (ord(s[i]) < ord('a') or ord(s[i]) > ord('z'))):
            del s[i]
            i -= 1
        i += 1
    A = "".join(s)
    # print(A)
    return A


s = input("Enter message: ")
s = [i for i in s]
M = D(s)

a = "INR 5,000 debited to your A/c No XX2728 on 17/03/2020 through NEFT with UTR MAHBH227282061717 by MLWB, INFO:"
a = [i for i in a]
M1 = D(a)

b = "INR 5,000.00 credited to your A/c No XX5927 on 17/03/2020 through NEFT with UTR MAHBH20077821717 by MLWB, INFO:"
b = [i for i in b]
M2 = D(b)


c = "we have recieved your request to change your account Number if you are not then click on the link:"
c = [i for i in c]
M3 = D(c)


d = "we have recieved your request to change your account Number if you are not then click on the link:"
d = [i for i in d]
M4 = D(d)


e = "Account verification inprogress.Confirm your information to regiain access.[link removed]"
e = [i for i in e]
M5 = D(e)

f = "Notification ID: 9766020145 [randomly generated number]For your protection, you must verify this activitybefore you can continue using your account.We will review the activity on your account with you and upon verification we will remove anyrestrictions placed on your bank accounts."
f = [i for i in f]
M5 = D(f)


g = "Update your account now. [link removed]If you choose to ignore our request, you leave us nochoice but to temporarily suspend your account.\Yours sincerely,Name of bank"
g = [i for i in g]
M6 = D(g)

if M == M1 or M == M2 or M == M3 or M == M4 or M == M5 or M == M6:
    print("\nSomeone is doing fraud with you. \nDont Give any reply.\nDont click anything. \nIf you have done anything Immidiately contact bank and police.\n ")
else:
    print("\nThis message is safe ,have a Good day\n")
