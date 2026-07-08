import csv
import os 
file_name = "expenses.csv"
if not os.path.exists(file_name):
    with open (file_name,"w",newline="") as file :
        writer=csv.writer(file)
        writer.writerow(["item","amount"])
def add_expense():
        item=input("enter expenses name-")
        amount=input("enter the amount-")
       
        with open(file_name,"a",newline="")as file:
            writer=csv.writer(file)
            writer.writerow([item,amount])
        print("expenses added successsfully \n")
        # function too view expwnses
def view_expenses():
    print("\n----expenses----")
    with open(file_name,"r")as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                print(f"item:{row[0]} amount:rs{row[1]}")
                print()
        #  function to calculate total expenses
def total_expenses():
              total=0
              with open(file_name,"r")as file:
                    reader=csv.reader(file)
                    next(reader)
                    for row in reader:
                          total += float(row[1])
              print(f"\n total expenses= rs{total}\n")
while True:
     print("=====expense tracker=====")
     print("1 add expense")
     print("2 view expenses")
     print("3 total expenses")
     print(" 4 exit")
    
     choice=input("enter your choice")
     if choice=="1":
            add_expense()
     elif choice == "2":
          view_expenses()

     elif choice == "3":
             total_expenses()
     elif choice == "4":
              print("thank you for using expenses tracker!!")
              break
else:
        print("invalid choice! please try again \n")
        

