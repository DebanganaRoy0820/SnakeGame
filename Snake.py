from turtle import Turtle

STARTING_POS = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        # White Square Turtle Body
        #   Creates Snakes
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, i):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(i)
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DOWN:
            return
        self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            return
        self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            return
        self.head.setheading(RIGHT)
