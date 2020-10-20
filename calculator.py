# lets try the calculator

print("Enter the Number that you want to operate")
a = input("Enter the operator such as +, -, *, / :")
n1 = float(input("Enter your first value in number :"))
n2 = float(input("Enter your second value in number :"))

if a == '+':
  print(n1,a,n2,"=",n1+n2)
elif a == '-':
  print (n1,a,n2,"=",n1-n2)
elif a == '*':
  print (n1,a,n2,"=",n1*n2)
elif a == '/':
  print(n1,a,n2,"=",n1/n2)
else:
  print("Please Enter the valid number")