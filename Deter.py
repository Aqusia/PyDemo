#bool type
print (type(1==1))
print (type(1==2))

#if
value = int(input("請輸入一個數字："))
if value>= 10:
    print ("你輸入的數字大於或等於10")
else:
    print ("你輸入的數字小於10")
    
#if elif 
#可以有多個elif，不一定要else
value = int(input("請輸入你的身高："))

if value >= 180:
    print ("你是高個子")
elif value >= 160:
    print ("你是中等身高")
else:
    print ("你是矮個子")
    
if int(input("請輸入你的身高：")) >= 180:
    print ("你是高個子，女生OK")
elif int(input("請輸入你的顏值等級：")) >= 9:
    print ("你是高顏值，女生也OK")
elif int(input("請輸入你的年收: ")) >= 1000000:
    print ("你是高收入，女生也OK")
else:
    print ("你不行，女生不要")
    
#嵌套if

#random
import random
num = random.randint(1, 4) 
input_num = int(input("請輸入1~4的數字："))

if input_num == num:
    print ("恭喜你猜對了！")
else:
    if input_num > num:
        print ("你猜的數字太大了！")
    else:
        print ("你猜的數字太小了！")
    
    if num == int(input("請輸入數字：")):
        print ("恭喜你猜對了！")
    else:
        print ("你猜錯了！正確的數字是", num)
    
    
    