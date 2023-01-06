def add(P, Q):     
   return P + Q   
def subtract(P, Q):    
   return P - Q   
def multiply(P, Q):    
   return P * Q   
def divide(P, Q): 
   return P / Q      
print ("Please select the operation.")    
print ("1. Add")    
print ("2. Subtract")    
print ("3. Multiply")    
print ("4. Divide")    
    
choice = input("Please enter choice (1/ 2/ 3/ 4): ")    
    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
    
if choice == '1':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif choice == '2':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
elif choice == '3':    
   print (num1, " * ", num2, " = ", multiply(num1, num2))    
elif choice == '4':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))    
else:    
   print ("This is an invalid input")    
