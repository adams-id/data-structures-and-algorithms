#Question
#How to calculate the power of a number using recursion?

#Solution
def powerOfNum(n, p): #n is the number and p is the power
  #The constraints
  assert int(p) == p, "The power must be an integer only"
  #When power is 0, return 1 
  if p == 0:
    return 1
  elif p < 0:
    return 1/ n * powerOfNum(n, p+1)
  #Recursive case is to multiply the number by the calculation and stop when the criterion is met
  else:
    return n * powerOfNum(n, p-1)

print(powerOfNum(4, 3))