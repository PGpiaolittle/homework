# 这是一个示例 Python 脚本。

def calculate_special_sum (n):
    sum=0
    for i in range(1,n+1):
        sum+=pow(i,2)
    return sum

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    assert calculate_special_sum(3) == 14

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
