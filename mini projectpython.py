import math
import random
a=int(input("enter starting number of range: "))
b=int(input("enter ending number of range: "))
n=random.randrange(a,b,1)
print("Randomly picked number is ",n)
if n%2==0:
    print(n,"is a even number")
else:
    print(n,"is a odd number")
if n>0:
     print(n,"is a positive number")
else:
    print(n,"is a negative number")
if n==1 or n==2:
    print(n,"is a prime number")
else:
    for j in range(2,int(math.sqrt(n))+1):
        if n%j==0:
            print(n,"is composite number")
        else:
            print(n,"is a prime number")
