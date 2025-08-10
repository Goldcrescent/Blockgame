import turtle

m = turtle.Turtle()

def draw_square():
    size = 100
    for _ in range(4):
        m.fd(size)
        m.rt(90)

def draw_circle():
    radius = 50
    m.circle(radius)

def draw_triangle():
    size = 100
    for _ in range(3):
        m.fd(size)
        m.rt(120)

def fd():
    m.fd(90)

def bk():
    m.bk(90)

def lt():
    m.lt(90)

def rt():
    m.rt(90)

def quit():
    exit()

screen = turtle.Screen()
screen.listen()
screen.onkey(draw_circle, "c")
screen.onkey(draw_square, "s")
screen.onkey(draw_triangle, "t")
screen.onkey(fd, "w")
screen.onkey(bk, "s")
screen.onkey(lt, "a")
screen.onkey(rt, "d")
screen.onkey(quit, "q")

turtle.mainloop()
