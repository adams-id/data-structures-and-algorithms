def factorial(n):
  #The constraints
  assert n >=0 and int(n) == n, "The number must be a positive integer only!"
  #Base condition i.e the stopping criterion
  if n in [0,1]:
    return 1
  #The recursive case
  else:
    return n * factorial(n-1)

print(factorial(6))