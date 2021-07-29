# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
from turtle import *
from time import sleep


def rightwing(t):
    t.down()
    t.right(45)
    loop = 0
    while loop < 18:
        t.forward(6)
        t.right(5)
        loop = loop +1
    t.up()
    loop = 0
    while loop < 18:
        t.left(5)
        t.back(6)
        loop = loop + 1
    t.left(45)


def leftwing(t):
    t.down()
    t.left(45)
    loop = 0;
    while loop < 18:
        t.forward(6)
        t.left(5)
        loop = loop +1
    t.up()
    loop = 0;
    while loop < 18:
        t.right(5)
        t.back(6)
        loop = loop + 1
    t.right(45)


def bird(t, alpha):
    t.left(alpha)
    rightwing(t)
    t.right(2 * alpha)
    leftwing(t)
    t.left(alpha)


wn = turtle.Screen()
alex = turtle.Turtle()
loop = 0
while loop < 5:
    pos = 0
    lp = 0
    while lp < 10:
        alex.color("black")
        bird(alex, pos)
        alex.color("white")
        bird(alex, pos)
        pos = pos + 2
        lp = lp +1
    alex.right(2)
    alex.forward(10)
    lp = 0
    while lp < 10:
        pos = pos - 2
        alex.color("black")
        bird(alex, pos)
        alex.color("white")
        bird(alex, pos)
        lp = lp + 1
    alex.right(2)
    forward(10)
    loop = loop + 1
