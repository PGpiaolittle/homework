# 这是一个示例 Python 脚本。
import random
def check_card_number_str(number):
    number = number.strip()
    sum=0
    long=len(number)
    for i in range(long-1,0,-2):
        sum+=int(number[i])
    for i in range(long - 2, 0, -2):
        sum+=int((int(number[i])*2)%9)
    if(0==sum%10):
        return True
    else:
        return False
def check_card_number(bankCardNO):
    ''' 校验银行卡算法符合 Luhm算法 （即是否有效）'''
    EvenSum = 0
    OddSum = 0
    luhmSum = 0
    index=1
    while(bankCardNO):
        if(index%2==0):
            EvenSum+=((bankCardNO%10)*2)%9
        else:
            OddSum+=bankCardNO%10
        bankCardNO=int(bankCardNO/10)
        index+=1
    if((OddSum+EvenSum)%10==0):
        return True
    else:
        return False



def luhnBankCardNOGenerator():
    ''' 生成校验码 Luhm算法'''
    if(random.randint(4,5)==4):
        cardNO = '4' + '%14d' % (random.randint(1, 99999999999999))
    else:
        cardNO = '5' + '%14d' % (random.randint(1, 99999999999999))
    EvenSum = 0
    OddSum = 0
    cardNOList =list(cardNO)

    for i in range(len(cardNOList)):
        k = 0
        if i%2 == 0:
            k = int(cardNOList[(len(cardNOList)-1)-i]) * 2
            if int(k / 10):
                kk = k - 9
            else:
                kk = k
            EvenSum = EvenSum + kk
        else:
            OddSum = OddSum + int(cardNOList[(len(cardNOList)-1)-i])
    checkNO = 10 - ((EvenSum + OddSum) % 10)
    bankCardNO = cardNO + str(checkNO)

    return  bankCardNO


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print(luhnBankCardNOGenerator())
    assert check_card_number(4540553713804935)
    assert check_card_number(5082337440657928)  # valid Mastercard card number
    assert not check_card_number_str(' 4601496706376197 ')



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
