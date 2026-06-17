import random


num = random.randint(1,100)
while True:
    guess = int(input("请输入一个1-100的整数："))
    if guess < num:
        print("小了！")
    elif guess > num:
        print("大了！")
    else:
        print("恭喜你，猜对了！")
        break
