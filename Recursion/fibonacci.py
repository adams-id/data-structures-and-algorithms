def fibonacci(n):
  #The constraints
  assert n>=0 and int(n) == n, "Fibonnacci number cannot be negative or non-integer"
  #Base condition i.e the stopping criterion
  if n in [0,1]:
    return n
  #The recursive case
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))