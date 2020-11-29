# function
def sum(n):
   if n <= 1:
      return n
   else:
      return n + sum(n-1)

print("Enter a positive number")
# type cast into integer 
num = int(input()) 
  
#condition
if num < 0:
 print("Enter a positive number")
else:
  print("The sum is",sum(num))
