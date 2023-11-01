import turtle
from paddle import Paddle
import time

width = 600
height = 500

turtle.title("Ping-Pong")

turtle.tracer(0, 0)
turtle.hideturtle()

player1 = Paddle(-width / 2, 0, 20, 70)
player2 = Paddle((width / 2) - 20, 0, 20, 70)

active_paddle = 1

def move_up():
    if active_paddle == 1:
        player1.move(10)
    elif active_paddle == 2:
        player2.move(10)

def move_down():
    if active_paddle == 1:
        player1.move(-10)
    elif active_paddle == 2:
        player2.move(-10)

turtle.listen()
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")

def update():
    try:
        turtle.clear()

        player1.draw()
        player2.draw()

        turtle.update()

        time.sleep(0.05)
        update()

    except:
        exit()

update()

turtle.mainloop()
