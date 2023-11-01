import turtle

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        turtle.up()
        turtle.goto(self.x, self.y + (self.height / 2))
        turtle.down()

        turtle.fillcolor("black")
        turtle.begin_fill()

        for i in range(0, 2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)

        turtle.end_fill()

    def move(self, change):
        if abs(self.y + change) <= 250:
            self.y += change
