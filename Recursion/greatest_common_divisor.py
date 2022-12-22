#Question
# How to find the Greatest Common Divisor of two numbers using recursion

#Solution
# Using Euclidean algorithm ... 
def gcd(a, b):
  assert int(a) == a and int(b) == b, "Both numbers have to be integers only!"
  #Convert any negaive number to positive so he modulo opeation would work
  if a < 0:
    a = -1 * a
  if b < 0:
    b = -1 * b
  # Stop criterion
  if b == 0:
    return a
  #Recursive case
  else:
    return gcd(b, a % b)

print(gcd(16, 12))