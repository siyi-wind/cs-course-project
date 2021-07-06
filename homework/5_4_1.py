"""
用递归画螺旋
"""

import turtle

t = turtle.Turtle()

def drawSpiral(t, linelen):
    if linelen > 0:
        t.color((0.2, 0.2, 0.3))
        t.forward(linelen) # 画一条线
        t.right(90) # 右转90度
        drawSpiral(t, linelen-5)

drawSpiral(t, 100)
turtle.done()
