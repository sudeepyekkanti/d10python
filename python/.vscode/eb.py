bill=int(input("enter number of units consumed:"))
total=0
if(bill<=100):
    total=bill*2
elif (bill<=200):
    total=100*2+((bill-100)*3)
else:
    total=100*2+100*3+((bill-200)*5)
    print(f"total bill amount of this month rs:{total}")  