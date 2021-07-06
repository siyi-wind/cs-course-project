"""
用递归画分形树
"""

import turtle

t = turtle.Turtle()

def tree(batch_len):
    if batch_len > 5:
        t.forward(batch_len) # 画树干
        t.right(20) # 画右小树
        tree(batch_len-5)
        t.left(40) # 左转20度
        tree(batch_len-5) # 画左小树
        t.right(20) # 回正
        t.backward(batch_len) # 回到树杈处

t.left(90) # 保证往上画
t.penup() # 抬笔
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(40)
t.hideturtle() # 隐藏画笔
turtle.done()
