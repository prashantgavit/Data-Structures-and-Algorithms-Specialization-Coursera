n=int(input())
def Fun_Fibonacci(n):
       if (n==0):
               return(0)
       elif (n==1):
               return(1)
       else:
               return(Fun_Fibonacci(n-1)+Fun_Fibonacci(n-2))

print(Fun_Fibonacci(n))
