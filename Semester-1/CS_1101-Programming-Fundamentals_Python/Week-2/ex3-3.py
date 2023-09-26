#!/bin/python3
def grid_width():
    print("+----+----+----+----+")

def grid_length():
    print("|    |    |    |    |")
    print("|    |    |    |    |")
    print("|    |    |    |    |")
    print("|    |    |    |    |")

def square_grid():
    grid_width()
    grid_length()
    grid_width()
    grid_length()

def four_clmn_grid():
    square_grid()
    square_grid()
    grid_width()

four_clmn_grid()
