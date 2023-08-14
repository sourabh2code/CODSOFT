# Basic Airthmetic Calculator


m=1

def power(a,b):
    print("Power of a to b  = ",a**b)

while m==1 :

    print("..................................CALCULATOR.............................")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Divison")
    print("4. Floor Divison")
    print("5. Power")
    print("6. Subtraction")
    
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    c=input("Enter the choice(1/2/3/4/5/6) : ")

    if c=='1' :
        k=a+b
        print("Addition of ",a,"and ",b," = ",k)
          
    elif c=='2' :
        k=a*b
        print("Multiplication of ",a,"and ",b," = ",k)
        
    elif c=='3' :
        k=a/b
        print("Divison of ",a,"and ",b," = ",k)
       
    elif c=='4' :
        k=a//b
        print("Floor Divison of ",a,"and ",b," = ",k)
        
    elif c=='5' :
        power(a,b)

    elif c=='6' :
        k=a-b
        print("Subtraction of ",a,"and ",b," = ",k)

    else :
        print("Invalid Choice . Please enter valid choice(1/2/3/4/5/6)")

    
    s=input("Do you want to calculate more number (y/n) :  ")
    if s=='n' :
        m=0
    else :
        m=1
    
    
print("Thank You ! ! !")      
    
