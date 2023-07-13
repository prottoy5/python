# Write a program to take integer input from user and display the grade according to the follow criteria.
#         Marks                   Grade
#         >90                     A
#         >80 AND <=90            B
#         >=60 AND <=80           C
#         BELOW 60                D

marks = int(input("Enter the marks : "))

if marks>90:
    print("A")
elif marks>80 and marks<=90:
    print("B")
elif marks>=60 and marks<=80:
    print("C")
else:
    print("D")

    