num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
print("Select the choice : 1.Addition\n2.Substraction\n3.Division\n4.Multiplication\n5.Power OR Exponent")


choice=int(input("Enter Your Choice: "))

if choice==1:
    c=num1+num2
    print("Addition is : ",c) 
elif choice==2:
    c=num1-num2
    print("substraction is : ",c)
elif choice==3:
    c=num1/num2
    print("division is : ",c)
elif choice==4:
    c=num1*num2
    print("multiplication is : ",c)
elif choice==5:
    c=num1**num2
    print("Power of number 1 is : ",c)
else:
    print("Invalid choice : ")