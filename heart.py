import turtle

t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart")

# Drawing heart
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(68)
t.circle(-90, 200)
t.forward(188)
t.end_fill()

# Writing text
t.up()
t.setpos(-90, 125)
t.down()
t.color("lightgreen")
t.write("MANGATS!!!", font=("Verdana", 20, "bold"))
t.ht()

turtle.mainloop()