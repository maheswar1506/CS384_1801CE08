# Function to add two numbers 
def add(num1, num2): 
    addition = num1 + num2
    return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
    subtraction = num1 - num2
    return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
    #Multiplication Logic 
    multiplication = num1 * num2
    return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
    #DivisionLogic 
    if num2 == 0:
        return 0
    division = num1/num2
    return division

# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
    #DivisionLogic 
    if ((isinstance(num1,(int,float))) and isinstance(num2,(int,float)) and (int(num2)==num2)):
        num2 = int(num2)
        if num1==0 and num2==0:
            return 1
        elif num1==0 and num2!=0:
            return 0
        elif num1!=0 and num2==0:
            return 1
        elif num2<0:
            return round((1/power(num1,-num2)),3)
        else:
            p = power(num1,num2//2)
            if num2%2 == 0:
                return round(p*p,3)
            else:
                return round(num1*p*p,3)
    return 0

# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n): 
    temp = [0]
    if ((isinstance(a,(int,float))) and (isinstance(r,(int,float))) and (isinstance(n,(int,float)) and int(n)==n)):
        n = int(n)
        gp=[]
        if n<=0:
            return temp
        gp.append(round(a,3))
        if n==1:
            return gp
        for x in range(1,n):
            gp.append(round(gp[x-1]*r,3))
        return gp 
    return temp
# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
    ap=[]
    return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
    hp=[]
    return hp