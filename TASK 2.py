def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y!=0:
        return x/y
    else:
        return "Divide by zero error"
    
while True:
    print("SIMPLE CALCULATOR")
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print("Choose operation: ")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    
    operation=input()
    
    if operation=='1':
        result=add(num1,num2)
        
    elif operation=='2':
        result=sub(num1,num2)
        
    elif operation=='3':
        result=mul(num1,num2)
        
    elif operation=='4':
        result=div(num1,num2)
        
    elif operation=='5':
        print("Exiting the calculator.Byee!")
        break
        
    else:
        result="Invalid input.Please choose a valid operation"
        
    print("Result: ",result)