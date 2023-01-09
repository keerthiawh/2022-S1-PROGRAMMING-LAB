num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))
num3=int(input("Enter Third Number :"))
max = 0
if num1 >= num2 and num1 >= num3:
  print("Greatest Number is :",num1)
elif num2 >= num1 and num2 >= num3:
  print("Greatest Number is :",num2)
else:
  print("Greatest Number is :",num3)
