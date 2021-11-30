# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
def merge(arr1, arr2):
    result = []
    i = 0
    j = 0
    a = len(arr1)
    b = len(arr2)
    while (i < a and j < b):
        if (arr1[i] < arr2[j]):
            result.append(arr1[i])
            i = i + 1
        else:
            result.append(arr2[j])
            j = j + 1
    while (i < a):
        result.append(arr1[i])
        i = i + 1
    while (j < b):
        result.append(arr2[j])
        j = j + 1
    if (type(arr1) == type(result)):
        return result
    return tuple(result)


if __name__ == '__main__':

    assert merge([1, 2, 7], [3]) == [1, 2, 3, 7]

    assert merge((3, 15), (7, 8)) == (3, 7, 8, 15)

print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
