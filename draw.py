from turtle import Turtle


def draw_square():
    window = Turtle().screen
    window.bgcolor('red')
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.speed(50)
    turtle.color('blue')

    for x in range(0, 180):
        for j in range(1, 5):
            turtle.forward(100)
            turtle.right(90)
        turtle.right(2)

    turtle_circle = Turtle()
    turtle_circle.shape('arrow')
    turtle_circle.circle(100)

    window.exitonclick()


def my_initials():
    window = Turtle().screen
    window.bgcolor('grey')

    turtle = Turtle()
    turtle.color('white')
    turtle.circle(100)

    turtle2 = Turtle()
    turtle2.setpos(120.0, 0.0)
    turtle2.clear()

    turtle2.left(90)
    turtle2.forward(200)
    turtle2.right(150)
    turtle2.forward(230)
    turtle2.left(150)
    turtle2.forward(200)

    print turtle.position()

    window.exitonclick()


def fuck_you():
    window = Turtle().screen
    window.bgcolor('black')
    f = Turtle()
    f.color('white')
    f.left(90)
    f.forward(100)
    f.right(90)
    f.forward(50)

    u = Turtle()
    u.color('white')
    u.setpos(60.0, 100.0)
    u.clear()

    u.right(90)
    u.forward(100)
    u.left(90)
    u.forward(50)
    u.left(90)
    u.forward(100)

    c = Turtle()
    c.color('white')
    c.setpos(180.0, 100.0)
    c.clear()

    c.backward(50)
    c.left(-90)
    c.forward(100)
    c.left(90)
    c.forward(50)

    k = Turtle()
    k.color('white')
    k.setpos(200.0, 100.0)
    k.clear()

    k.right(90)
    k.forward(100)
    k.sety(50)
    k.right(-45)
    k.forward(50)
    k.backward(50)
    k.right(-90)
    k.forward(50)

    u2 = Turtle()
    u2.color('white')
    u2.setpos(300.0, 100.0)
    u2.clear()

    u2.right(90)
    u2.forward(100)
    u2.left(90)
    u2.forward(50)
    u2.left(90)
    u2.forward(100)

    window.exitonclick()


draw_square()

print 'My bae Hannah I love u'
