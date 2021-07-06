"""
表达式转换 转为后缀表达式
操作数直接输出，操作符需要对比栈内操作符再做决定
"""
from pythonds.basic.stack import Stack

def infixTopostfix(infixpr): # 中缀转后缀
    prec = {}
    prec['('] = 1
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    opStack = Stack()  # 储存还没有处理的运算符

    tokenList = infixpr.split(' ') # 按照空格分隔把中缀表达式变为列表
    posfixList = [] # 储存后缀表达式
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            posfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':    # 在没有碰到左括号之前，把其中的运算符都输出
                posfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]): # 当栈非空并且顶部的运算符优先级更大 则顶部的运算符输出
                posfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty(): # 当栈仍非空
        posfixList.append(opStack.pop())


    return  ''.join(posfixList)





print(infixTopostfix('A * B + C * D'))
