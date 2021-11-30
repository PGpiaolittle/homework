# 这是一个示例 Python 脚本。


from memory_profiler import profile
import time
from contextlib import contextmanager
# 按间距中的绿色按钮以运行脚本。

@profile
#@profile(precision=4,stream=open('memory_profiler.log','w+'))
def some_function ():
    return sum ( range ( 1000 ) )


# print execution time when calculation is over
@contextmanager
def timer():
    start=time.time()

    yield



if __name__ == '__main__':

    result = some_function()  # return a value and print execution time

    with timer():
        print(sum(range(1000)))


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
