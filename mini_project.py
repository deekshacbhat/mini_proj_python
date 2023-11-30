import random

alpha_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num_list=['1','2''3','4','5','6','7','8','9','0']
sym_list=['!','@','#','$','%','^','&','*']
password_list=""

num=int(input("How many numbers do you want?"))
alpha=int(input("How many aplhabets do you want?"))
sym=int(input("How many symbols do you want?"))
'''
for i in range(0,num):
    password_list.append(random.choice(num_list))
for i in range(0,alpha):
    password_list.append(random.choice(alpha_list))
for i in range(0,sym):
    password_list.append(random.choice(sym_list))
password="".join(password_list)

random.shuffle(password)
print(password)'''






