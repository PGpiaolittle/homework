# 这是一个示例 Python 脚本。

def get_primes(n):
    res=[]
    if n==1:
        return res
    if n==2:
        res.append(2)
        return res
    for i in range(2,n+1):
        flag=False
        for j in range(2,i):
            if(i%j==0):
                flag=True
                break
        if(flag==False):
            res.append(i)
    return res

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    assert [2, 3, 5, 7, 11] == sorted(get_primes(11))
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
