#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：热耳 time:2020/2/16
import turtle as t
def drawHeart(r,c):
    t.pendown()
    t.down()
    t.fillcolor(c)
    t.begin_fill()
    factor = 180
    t.seth(45)
    t.circle(-r, factor)
    t.fd(2 * r)
    t.right(90)
    t.fd(2 * r)
    t.circle(-r, factor)
    t.end_fill()
    t.penup()
def hearts():
    drawHeart(20,'pink')
    t.left(90)
    t.fd(50)
    drawHeart(10,'pink')
    t.right(180)
    t.fd(50)
    drawHeart(15,'blue')
    t.left(90)
    t.fd(50)
    drawHeart(10,'blue')



t.pensize(3)
hearts()