# Builling system at super mart 


""""
Here we use Nested loop function 
"""
while True:
    name = input("Enter customer's name:")
    total = 0

    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter the amount:"))
        quantity = float(input("Enter Quantity"))
        total += amount * quantity
        repeat = input("Do you want to add more items (yes/no):")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name:",name)
    print("Amount to be paid:",total)
    print("*******Happy Shooping********")

    repeat1 = input("do you want to go to next customer ?(yes/no):")
    if repeat1 == "no" or repeat == "N0":
        break


