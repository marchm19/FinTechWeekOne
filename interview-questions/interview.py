def fizzBuzz():
    for i in range (1,101):
        result = ""
        if(i%3==0 or i%5==0):
            if(i%3==0):
                result+="fizz"
            if(i%5==0):
                result+="buzz"
        else:
            result+=str(i)
        print(result)
#fizzBuzz()

def fibonacci(num):
    if num == 2:
        return 1
    elif num==1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

#print(fibonacci(20))

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
    
def pascal(num):
    row =[]
    for i in range(0,num+1):
        row.append(int(nCr(num,i)))
    return row
    
#print(pascal(4))

def prime(num):
    primes = []
    for i in range(2,num):
        factor = False
        for j in range(2,i+i):
            if(i%j==0 and i!=j):
                factor = True
        if not factor:
            primes.append(i)
    return primes

#print(prime(20))

def squareRoot(num):
    return math.sqrt(num)