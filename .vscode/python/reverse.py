#reverse the string using for loop 
string = input("enter any string")
reverse=""
for char in string :
    reverse=char+reverse
print("reversed string: ", reverse) 