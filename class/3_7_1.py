"""
后缀表达式计算  先把中缀改成后缀 然后再运行后缀计算
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


    return  ''.join(posfixList), ' '.join(posfixList)

def math(op, x1, x2): # 计算表达式
    expression = x1+op+x2
    return eval(expression)  # 变回字符

def posfixEval(posfixExpr): # 计算后缀
    operandStack = Stack() # 储存还未处理的操作数
    tokenList = posfixExpr.split(' ')

    for token in tokenList:
        if token in '0123456789':
            operandStack.push(token)
        else:
            oprand2 = operandStack.pop() # 先出来的是右操作数
            oprand1 = operandStack.pop()
            result = math(token, oprand1, oprand2)
            operandStack.push(str(result))

    return operandStack.pop()

_, posfixList = infixTopostfix('1 + 5 * 6 - 6 / 3')
result = float(posfixEval(posfixList))
print(posfixList, result)
