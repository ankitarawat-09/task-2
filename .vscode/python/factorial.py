num=int(input("enter your value"))
factorial=1
#using for loop 
for i in range(1,num+1):
    factorial=factorial*i
    print("factorial of ",num, "is",factorial)