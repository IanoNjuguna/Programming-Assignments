#!/bin/python3
import turtle

bob = turtle.Turtle()

def polygon(t, n, length):
    angle = (360.0 / n)

    for i in range(n):
        t.fd(length)
        t.fd(angle)

polygon(bob, 4, 50)
turtle.mainloop()
