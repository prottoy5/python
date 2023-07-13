# Write a program using conditional statement whether a number is even or odd.(even means divisibl by 2 and odd mean not divisible by 2)
#Suppose user provide input as 15 then it will print "15 is an odd number".

number = int(input("Enter a number : "))

if number%2 == 0:
    print(number," is an even number")
else:
    print(number," is an odd number")

