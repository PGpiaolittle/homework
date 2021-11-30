# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

def get_number(number):

    lon=len(str(number))
    sumodd=0
    sumeven=0
    while(lon):
        if(lon%2==0):
            sumodd+=number%10
        else:
            sumeven+=number%10
        number/= 10
        number = int(number)
        lon-=1
    if(sumodd==sumeven):
        return True
    else:
        return False
def get_nearest_lucky_ticket ( number ):
    if(get_number(number)):
        return number
    index=1
    while(True):
        if(get_number(number+index)):
            return number+index
        if(get_number(number-index)):
            return number-index
        index+=1




def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    assert get_nearest_lucky_ticket(111111) == 111111
    assert get_nearest_lucky_ticket(123321) == 123321
    assert get_nearest_lucky_ticket(123320) == 123321
    assert get_nearest_lucky_ticket(333999) == 334004
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
