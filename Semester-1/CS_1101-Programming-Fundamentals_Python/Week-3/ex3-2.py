#!/bin/python3

def do_twice(str):
    print(f"{str}")
    print(f"{str}")

def do_four(do_twice, str):
    do_twice(str)
    do_twice(str)

do_four(do_twice, "string")
