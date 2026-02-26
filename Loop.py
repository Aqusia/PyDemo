import random
"""
#while loop
i = 1
total =0
while i<=100:
    total += i
    i+=1
print ("1~100的總和是", total)

num = random.randint(1, 100)
flag = True
min =1 
max = 100
count = 0
while flag:
    guess = int(input(f"請猜一個{min}~{max}的數字："))
    count += 1
    if guess == num:
        print ("恭喜你猜對了！"+"你總共猜了"+str(count)+"次")
        flag = False
    else: 
        if guess > num:
            max = guess-1
            print ("你猜的數字太大了！")
        else:
            min = guess+1
            print ("你猜的數字太小了！")
            
# Walrus operator 
i=0                
while (i := i + 1) <= 100:
    j=0
    while (j := j + 1) <= 10:
        print (f"跟欣O說{j}次嗨熊男")
        
    print (f"今天是交往第{i}天")
"""
#print second argumment
print ("Hello World", end = ' ')
print ("I am loser")

#tab
print ("Hello\tWorld")
print ("I am\tloser")

# 9*9
print ("九九乘法表，for loop")
for i in range(1,10):
    for j in range(1,i+1):
        print (f"{i}*{j}={i*j}", end = '\t')
    print ()

print ("九九乘法表，while loop")
i = 1
while i< 10: 
    j = 1
    while j <= i:
        print (f"{i}*{j}={i*j}", end = '\t')
        j += 1
    i+=1
    print ()