# /user/bin/env python
#  -*- coding:utf-8 -*-
# Author:CLL

#购物车
# 启动时候输入工资
# 用户启动程序打印商品列表
# 允许用户选择购买商品
# 允许用户不断的购买商品
# 购买时检测 余额是否足够，够就直接扣款，否则打印余额不足
# 允许用户主动退出程序，退出时打印已购商品列表

list= [
    ("iphone",5000),
    ("ipa",8000),
    ("pro",9000),
    ("iphone",19.69),
    ("Coffee",69),
    ("Tesla",82000),
    ("bike",700),
    ("yifu",200)
]
arr = []
money= input("你的工资:")#输入工资
if money.isdigit():#是不是数字
    money = int(money)#那么money就等于输入的money
else:
    exit("输如的不是钱")#不是就退出
welcome = "欢迎来购物".center(50,"-")#欢迎购物
print(welcome)

onOff = False#标志位
#while onOff is not True:
while not onOff:#如果开关不是真的时候，执行下面的程序上边的条件一定要为真
    # for wupin in list: 循环那个变量
    #     wupin.name,wupin.money =  list  也是存变量
    print("list".center(50,"-"))#加样子
    for item in enumerate(list):#直接两个就循环了
        #print(item)
        index = item[0]
        inname = item[1][0]
        inmoney = item[1][1]
        print(index,'.',inname,inmoney)
    nub = input("[q = quit,c=check]你想买那个：")
    if nub.isdigit():#肯定是选择商品
        nub = int(nub)
        if nub < len(list):
            p_item = list[nub]
            if p_item[1]<= money:#买的起
                arr.append(p_item)#放入购物车
                print(arr)
                money -= p_item[1]#捡钱
                print("你买的[%s]加入你的购物车,你的余额：[%s]" %
                      (p_item,money))
            else:
                print("老子没钱了%s，不能买了"%money)
    else:
        if nub == "q" or nub == "quit":
            print("购买结束".center(40,'*'))
            for item in arr:
                print(item)
            print("end".center(40,"*"))
            print("你还有多少%s"% money)
            onOff  = True
        else:
            print("购买结束".center(40,'*'))
            for item in arr:
                print(item)
            print("end".center(40,"*"))
            print("你还有多少%s"% money)
            onOff  = True




