from turtle import *


def draw_fish():
    screen = Screen()
    screen.setup(1200, 800)

    t = Turtle()
    t.speed(0)
    t.pensize(3)

    # Рисуем тело рыбы (овал)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color('black')

    t.setheading(-45)
    for _ in range(2):
        t.circle(100, 90)  # Полукруг
        t.circle(50, 90)   # Полукруг меньшего радиуса

    # Рисуем верхний плавник
    t.penup()
    t.goto(50, 100)
    t.pendown()
    t.setheading(60)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(120)
    t.forward(50)

    # Рисуем нижний плавник
    t.penup()
    t.goto(100, -25)
    t.pendown()
    t.setheading(-95)
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.left(120)
    t.forward(50)

    # Рисуем хвост
    t.penup()
    t.goto(155, 40)
    t.pendown()
    t.setheading(30)
    t.forward(100)
    t.right(150)
    t.forward(50)
    t.left(50)
    t.forward(50)
    t.right(135)
    t.forward(87)

    # Рисуем глаз рыбы
    t.penup()
    t.goto(25, 50)
    t.pendown()
    t.begin_fill()
    t.color('black')
    t.circle(10)
    t.end_fill()

    # Рисуем волны
    t.up()
    t.goto(-600, 300)
    t.down()
    t.color('blue')
    t.setheading(270)
    for i in range(7):
        t.circle(50, 180)
        t.begin_fill()
        t.circle(-50, 180)
        t.end_fill()

    # Рисуем водоросли
    t.up()
    t.goto(-570, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(2):
        t.circle(25, 180)
        t.circle(-15, 180)

    t.up()
    t.goto(-470, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(3):
        t.circle(22, 180)
        t.circle(-25, 180)

    t.up()
    t.goto(-380, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(2):
        t.circle(25, 180)
        t.circle(-15, 180)

    t.up()
    t.goto(-290, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(3):
        t.circle(22, 180)
        t.circle(-25, 180)

    t.up()
    t.goto(-180, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(2):
        t.circle(25, 180)
        t.circle(-15, 180)

    t.up()
    t.goto(-90, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(3):
        t.circle(22, 180)
        t.circle(-25, 180)

    t.up()
    t.goto(0, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(2):
        t.circle(25, 180)
        t.circle(-15, 180)

    t.up()
    t.goto(110, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(3):
        t.circle(22, 180)
        t.circle(-25, 180)

    t.up()
    t.goto(210, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(2):
        t.circle(25, 180)
        t.circle(-15, 180)

    t.up()
    t.goto(300, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(3):
        t.circle(22, 180)
        t.circle(-25, 180)

    t.up()
    t.goto(390, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(2):
        t.circle(25, 180)
        t.circle(-15, 180)

    t.up()
    t.goto(495, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(3):
        t.circle(22, 180)
        t.circle(-25, 180)

    t.up()
    t.goto(565, -400)
    t.down()
    t.color('green')
    t.setheading(360)
    for i in range(2):
        t.circle(25, 180)
        t.circle(-15, 180)


    # Функция для рисования пузырьков
    def draw_bubble(x, y, radius):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color('lightblue')
        t.circle(radius)

    # Рисуем несколько пузырьков
    draw_bubble(10, 100, 5)
    draw_bubble(12, 125, 3)
    draw_bubble(0.8, 150, 7)
    draw_bubble(15, 170, 10)
    draw_bubble(10, 210, 15)

    # Smile *)
    t.penup()
    t.goto(-6, 10)
    t.pendown()
    t.color('black')
    t.setheading(-60)
    t.circle(20, 120)

    # Завершаем рисование
    t.hideturtle()
    screen.exitonclick()


draw_fish()
