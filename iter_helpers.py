# 这是一个示例 Python 脚本。
import itertools
import operator
# 按间距中的绿色按钮以运行脚本。
#actual = transpose([[1, -1], [2, 3]])
def transpose(list1):
    long=len(list1[0])+1
    index=long
    res=[]
    for i in itertools.product(list1[0],list1[1]):

        if(index==long):
            res.append(list(i))

        index-=1
        if(index==0):
            index=long

    return res


 #   for i in itertools.product(list1[0], list1[1]):
def fin(number):
     dic={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'0':0}
     if(type(number)==int):
         return True
     else:
         string1=number
         list1=list(string1)
         for i in itertools.product(list1):
             if(dic.get(i[0])==None):
                 return False
     return True



def scalar_product(list1,list2):
    sum=0
    index = 1
    long = len(list1) + 1
    index_for = 1
    for i in itertools.product(list1, list2):
        if (index_for == index):
            index += long
            if(fin(i[0]) and fin(i[1])):
                sum+=int(i[0])*int(i[1])
            else:
                return None
        index_for+=1
    return sum




if __name__ == '__main__':
    expected = 1
    actual = scalar_product([1, '2'], [-1, 1])
    assert expected == actual
    actual = scalar_product([1, 'xyz'], [-1, 1])
    assert actual is None

    expected = [[1, 2], [-1, 3]]
    actual = transpose([[1, -1], [2, 3]])
    assert expected == list(map(list, actual))



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
