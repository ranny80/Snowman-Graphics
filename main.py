import turtle

canvas = turtle.Screen()
snowman = turtle.Turtle()

# Background color
canvas.bgcolor("light blue")

# Title
canvas.title("Snowman Graphics")
snowman.shape("circle")

snowman.color("white")

print("Building...")

snowman.right(180)

snowman.begin_fill()

snowman.circle(85)

snowman.end_fill()

snowman.right(900)

snowman.begin_fill()

snowman.circle(65)

snowman.end_fill()

snowman.right(180)

snowman.goto(0, 210)

snowman.begin_fill()

snowman.circle(40)

snowman.end_fill()

# It will disappear the turtle when the process is finished
snowman.hideturtle()

print("Build successful.")

canvas.mainloop()
