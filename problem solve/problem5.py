# Write a program to check whether a year is leap year or not. Take input from user if year = 1996, it is a leap year.
# Condition for leap year : 
# 1. If a year is divisible by both 400 and 100 it is a leap year.
# 2. If a year is divisible by 4 and not divisible by 100 it is a leap year.

year = int(input("Enter a year : "))

'''if year % 400 == 0:
    print("It is a leap year.")
elif year % 100 == 0:
    print("It is not a leap year.")
elif year % 4 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")
'''

if year % 400 == 0 and year % 100 == 0:
   print("It is a leap year.")
elif year % 4 == 0 and year % 100 != 0:
   print("It is a leap year.")
else:
   print("It is not a leap year.")

   

    




