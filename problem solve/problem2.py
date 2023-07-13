#Take 3 integer input from user and find the largest number between using if-elif-else statement.

a = int(input("Enter the number of 1 : "))
b = int(input("Enter the number of 2 : "))
c = int(input("Enter the number of 3 : "))

if a>=b and a>=c:
    print("The largest number is A=",a)
elif b>=c and b>=a:
    print("The largest number is B=",b)
else:
    print("The largest number is C=",c)
    