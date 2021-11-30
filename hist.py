# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
def distribute(list,k):
    # lst = [0 for n in range(6)]
    lst=[0]*k
    min=99999.0
    max=0.0
    for i in list:
        if(i<min):
            min=i
        if(i>max):
            max=i
    range=(max-min)/k
    for i in list:
        index=int((i-min)/range)
        if((i-min)!=0and(i-min)%range==0):
            index-=1
        lst[int(index)]+=1
    return lst


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    assert distribute([1.25, 1, 2, 1.75], 2) == [2, 2]
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
