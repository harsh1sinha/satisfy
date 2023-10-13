

def recursion_fibo(n):
   if n <= 1:
       return n
   else:
       return(recursion_fibo(n-1) + recursion_fibo(n-2))

n_terms = 10


if n_terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n_terms):
       print(recursion_fibo(i))
