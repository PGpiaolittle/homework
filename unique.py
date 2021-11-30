# 这是一个示例 Python 脚本。

def compress(list1):
   dit={}
   res=[]
   for i in list1:
       if(dit.get(i)==None):
           dit[i]=1
       else:
           dit[i]=dit[i]+1
   for kv in dit.items():
       res.append(kv)

   return res
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    expected_sorted = [(1 , 2 ) , (2 , 1 ) , (3 , 1)]
    actual_sorted = sorted ( compress ([1 , 2 , 1 , 3]) )
    assert expected_sorted == actual_sorted
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
