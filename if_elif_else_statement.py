# marks = 85    #90-100 = 2 chocolate,80-90 = 1 chocolate, <=80 = not get anything

marks = int(input())
print("Student marks : ",marks)

if marks >= 90 and marks <= 100:
    print("Student get 2 chocolate")

elif marks >= 80 and marks <= 89:
    print("Student get 1 chocolate")

else:
    print("not get anything")






