import turtle

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("black")
t.pencolor("violet")
t.speed(0)

def crazy(v):
    for i in range(560):
        t.fd(i)
        t.left(v)

crazy(137)
t.hideturtle()

#orange-124
#blue-167
#cyan-137(fav1)
#cyan-50(basic)
#107.117.127.137.147.157
#orange,blue,red,green,cyan,orange,violet
