# Haroon Nasir
# 08/09/2025

# Draws a simple and colorful spiral

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simple Colorful Picture")

# Create turtle
t = turtle.Turtle()
t.speed(20)

# Draw a colorful spiral
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(100):
    t.color(colors[i % 6])
    t.forward(i * 2)
    t.right(91)

# Keep the window open
t.hideturtle()