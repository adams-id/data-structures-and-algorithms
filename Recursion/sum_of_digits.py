#Question
#How to find the sum of digits of a positive integer number using recursion?

#Solution
def sumOfDigits(n):
  assert n>=0 and int(n) == n, "The number has to be a positive integer only"
  #If n is a single digits, return n
  if n%10 == n:
    return n
  #Take the remainder of every division by 10 and add them together
  return sumOfDigits(n//10) + sumOfDigits(n%10)

print(sumOfDigits(674))