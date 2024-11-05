#Blayne Hoy
#U3 Lab 2

def for_factorial(n):
  result = 1
  for x in range(1, n + 1):
    result *= x
  return result

def while_factorial(n):
  result2 = 1
  while n > 0:
    result2 *= n
    n -= 1
  return result2

def recursion_factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * recursion_factorial(n-1)

def main():
  n = 5

  for_result = for_factorial(n)
  while_result = while_factorial(n)
  recursion_result = recursion_factorial(n)

  print(f"{n} calculated using for loop : {for_result}")
  print(f"{n} calculated using while loop : {while_result}")
  print(f"{n} calculated using recursion : {recursion_result}")




if __name__ == "__main__":
  main()
