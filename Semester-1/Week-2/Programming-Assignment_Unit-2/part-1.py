#!/bin/python3

"""
The circumference of a circle is calculated by 2πr
π = 3.14159 (rounded to five decimal places)
Write a function called print_circum that takes an
argument for the circle’s radius and prints the circle's radius
"""

import math

pie = round(math.pi, 5)

def print_circum(radius):
    circumference = 2 * pie * radius
    print (f"The circumference of a circle with radius {radius} is {circumference:.5f}")

print_circum(5)
print_circum(2)
print_circum(3.56)
