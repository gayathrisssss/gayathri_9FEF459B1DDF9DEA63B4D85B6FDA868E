def factorial(n):
 if n==0 or n==1:
   return 1
 else:
   return n*factorial(n-1)
number=int(input ("Enter a Value:"))
fact=factorial(number)
print ("The Factorial of",number,"is",fact)