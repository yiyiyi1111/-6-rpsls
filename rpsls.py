#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020.4.6
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
def name_to_number(name):
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
        print("Error: No Correct Name")
        
def number_to_name(number):
    if number==0:
        return"ʯͷ"
    elif number==1:
        return"ʷ����"
    elif number==2:
        return"ֽ"
    elif number==3:
        return"����"
    elif number==4:
        return"����"
     
def rpsls(player_choice):
        print("����ѡ��Ϊ:",player_choice)
        player_number=name_to_number(player_choice)
        computer_number=random.randrange(0,5)
        computer_choice=number_to_name(computer_number)
        print("�������ѡ��Ϊ:",computer_choice)
        if player_number-computer_number in range(-4,-2)or range (1,3):
            print("��Ӯ��")
        elif player_number-computer_number in range(-2,0) or range (3,5):
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
            
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
