# 0 ,1, 0+1=1, 1+1=2 , 2+1=3 and so on
num=int(input("enter the number of terms"))
a=0
b=1
print("fibonacci series:")
for i in range(num) :
    print (a,end=" ")
    c=a+b
    a=b
    b=c