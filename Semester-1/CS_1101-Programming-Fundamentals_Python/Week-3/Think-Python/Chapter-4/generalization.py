#!/bin/python3
import turtle

bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 100)
turtle.mainloop()
