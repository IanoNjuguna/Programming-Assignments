#!/bin/python3

from re import U


def right_justify(str):
    update_string = " " * 70 + str
    strlen = len(update_string)

    print(f" {update_string}")
    print(strlen)

right_justify("monty")

