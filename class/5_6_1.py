"""
递归方法解决汉诺塔
N-1的盘片塔  从开始柱 经过目标柱  到中间柱
第N块盘片 从开始柱 到目标柱
N-1的盘片塔 从中间柱 经过开始柱 到目标柱
"""

def moveTower(height, fromPole, withPole, toPole):
    if height >= 0:
        moveTower(height-1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height-1, withPole, fromPole, toPole)

def moveDisk(disk, fromPole, toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")

moveTower(3, '#1', '#2', '#3')
