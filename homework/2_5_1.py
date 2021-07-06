"""
python 数据类型的各种操作的大O
"""
from timeit import Timer
def test1():
    l = [i for i in range(1000)]

t1 = Timer("test1()", "test1")
print ("concat %f seconds\n" % (t1.timeit(number=1000)))


