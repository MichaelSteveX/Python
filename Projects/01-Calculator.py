# Write a program to create a calculator 

print("*****AREA CALCULATOR*****")
print("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of rectanngle
press 4 to get the area of triangle 
""")
choice = int(input("Enter a number between 1-4 :"))

if choice == 1 :
    side = float(input("Enter the length of one side:"))
    area = side**2
    print("the area of square is",area)

elif choice ==2:
    length = float(input("Enter the length of :"))
    width = float (input("Enter the width of the rectangle:"))
    area = length*width
    print ("the area of rectangle is ",area)

elif choice == 3:
    radius = float(input("enter the radius of the circle"))
    area = ((22/7)*(radius**2))
    print("the area of the circle is ",area)

elif choice == 4:
    base = float(input("enter the base of the traingle "))
    height = float(input("enter the height of the triangle"))
    area = 0.5*base*height
    print("the area of the triangle is", area)

else:
    print("invalid input")