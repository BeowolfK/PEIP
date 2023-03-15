import turtle

def fractal_tree(n, length):
    angle = 30
    if n == 0:
        turtle.color("black")
        #turtle.color("green")
        turtle.forward(length)
        turtle.backward(length)
        #turtle.color("brown")

        return

    #turtle.width(n)
    turtle.forward(length/3)
    turtle.left(angle)

    fractal_tree(n-1, length * 2/3)

    turtle.right(2*angle)

    fractal_tree(n-1, length * 2/3)

    turtle.left(angle)
    turtle.backward(length/3)


LENGTH = 800

turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.left(90)
turtle.backward(LENGTH/2)

turtle.color("black")
turtle.pendown()
fractal_tree(15, LENGTH)

turtle.mainloop()