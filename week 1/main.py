#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle

turtle.Screen().setup(1.0, 1.0)

t = turtle.Turtle()

t.shape("turtle")

distance = 75
while True:
    for c in ["red", "green", "yellow", "blue", "purple"]:
        t.color(c)
        t.forward(distance)
        t.left(72)
    distance += 5
    t.left(5)
