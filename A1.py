import math
P=int(input("Enter the Principal Amount Deposited:"))
r=int(input("Enter the rate of Intrest:"))
n=int(input("Enter no of Years:"))
x=r/100
x2=1+x
x3=1
x3=math.pow(x2,n)
# without using Math fun
#for i in range(1,n+1):
    #x3=x3*x2
A=P*x3
CI=A-P
print("Principal Amount:",P)
print("Rate of Intrest:",r)
print("Intrest Period:",n,"Years")
print("Amount including intrest :",A)
print(" Intrest :",CI)