# Question
# How to convert a number from decimal to binary using recursion?

#Solution

def binary(n):
  assert int(n) == n, "Number must be an integer"
  if n == 0:
    return 0
  # Divide each number by 2 and multiply the remainder by 10 since binary starts from bottom up
  else:
    return n%2 + 10 * binary(int(n/2))

print(binary(13))