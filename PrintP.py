
"""
    I am loser
    god damn
"""


# 你媽
money = 666

print ("你媽原本有",money)

money -= 10
print ("你媽剩下",money)

string_type = type("I am loser")
print (string_type)

money = str(11.4515)
print (type(money),money)

money = int(11.5515)
print (type(money),money)

#介紹註解與參數的使用，並說明 type 型態的定義與作用。

#針對參數型態的部分，將講解以下重點：
#1. 參數的型態並非固定不變
#2. 介紹其他型態轉成 String，以及 String 轉成其他型態的過程（這部分不一定會成功）oney)

str_money = str(money)
print (type(str_money),str_money)

#opertor ...
print(9//2)
print(9**2)

#字符串的使用
print ("I am loser")
print ('I am loser')
print ("'I am loser'")
print ('\'I am loser\'')

#str combine
print ("I am " + "loser")

#% 格式化
name = "loser"
print ("I am %s" % name)
dollar = 666
print ("I have %d dollars" % dollar)
height = 1.75
print ("My height is %.2f meters" % height)

#f format 不理會類6型，直接將變數帶入字串中
print (f"I am {name} and I have {dollar} dollars. My height is {height:.2f} meters.")

#using expression in f format
print (f"Next year, I will have {dollar + 100} dollars")

#practice stock
company = "Apple"
price = 100.255
code = "APL"
daily_change = 1.1
days = 2

# output info
print(f"Company: {company}, Price: ${price:.2f}, Code: {code}")
print("Daily Change: %.2f, Days: %d, Total: %.3f" % (daily_change, days, price *(daily_change**days) ))