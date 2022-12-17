#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = '<'
d = '>'
e = 'O'
#Top Cone
for i in range(thickness):   #thickness=5,c='h',i=0,1,2,3,4
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):    #thickness=5,c='h',i=0,1,2,3,4,5
    print((c*thickness).center(thickness*2)+(d*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):    #thickness=5,c='h',i=0,1,2
    print((e*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):       #thickness=5,c='h',i=0,1,2,3,4
    print((c*thickness).center(thickness*2)+(d*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):        #thickness=5,c='h',i=0,1,2,3,4
    print(((d*(thickness-i-1)).rjust(thickness)+d+(d*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
