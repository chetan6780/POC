import turtle

t=turtle.Turtle()
l1=["purple","red","orange","blue","green","yellow","violet"]
t.speed(0)

for i in range(500):
    t.color(l1[i%7])
    t.pensize(i/10+1)
    t.fd(i)
    t.left(59)
    t.left(76)
    t.hideturtle()
    

