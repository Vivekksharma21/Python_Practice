# spiral Helix

import turtle
loadWindow=turtle.Screen()
loadWindow.bgcolor("light green")
turtle.speed(2)
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()