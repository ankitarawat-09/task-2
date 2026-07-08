# iif the word spells same backward and forward
word=input("enter your string/word:")
reverse=""
for ch in word :
    reverse=ch+reverse
if word ==reverse :
    print("the word is palindrome")
else :
    print("the word is not palindrome")