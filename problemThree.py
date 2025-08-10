# Haroon Nasir
# 08/09/2025

# Asks user for input on qualities of their polygon, and then drawing it using turtle graphics

import turtle

# Ask user for inputs
sides = int(input("Enter the number of sides: "))
length = float(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

# Set up the turtle
t = turtle.Turtle()
t.color(line_color, fill_color)  # (pen color, fill color)

# Start filling
t.begin_fill()

# Draw the polygon
for _ in range(sides):
    t.forward(length)
    t.left(360 / sides)

# End filling
t.end_fill()

# Finish
turtle.done()