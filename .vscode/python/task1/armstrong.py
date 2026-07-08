num = int(input("enter any 3 digit number"))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10
if num == sum:
        print(num,"is an armstrong number") 
else:
        print(num,"not an armstrong value")
