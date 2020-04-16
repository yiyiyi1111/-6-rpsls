#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：邓鑫怡
日期：2020.4.6
"""

import random

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀
def name_to_number(name):
    if name=="石头":
        return 0
    elif name=="史波克":
        return 1
    elif name=="纸":
        return 2
    elif name=="蜥蜴":
        return 3
    elif name=="剪刀":
        return 4
    else:
        print("Error: No Correct Name")
        
def number_to_name(number):
    if number==0:
        return"石头"
    elif number==1:
        return"史波克"
    elif number==2:
        return"纸"
    elif number==3:
        return"蜥蜴"
    elif number==4:
        return"剪刀"
     
def rpsls(player_choice):
        print("您的选择为:",player_choice)
        player_number=name_to_number(player_choice)
        computer_number=random.randrange(0,5)
        computer_choice=number_to_name(computer_number)
        print("计算机的选择为:",computer_choice)
        if player_number-computer_number in range(-4,-2)or range (1,3):
            print("您赢了")
        elif player_number-computer_number in range(-2,0) or range (3,5):
            print("计算机赢了")
        else:
            print("您和计算机出的一样呢")
            
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
