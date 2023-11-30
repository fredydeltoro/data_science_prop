import math


# Get Lucas sequence
def lucas_numbers(num_of_elements):
  numbers = [2, 1]

  for _ in range(2, num_of_elements):
    numbers.append(numbers[-2] + numbers[-1])

  return numbers


print(lucas_numbers(3))


# Get a specific number of Lucas, through their closed formula https://en.wikipedia.org/wiki/Lucas_number#Relationship_to_Fibonacci_numbers
def get_lucas_number(n):
  phi = math.sqrt(5)

  a = pow((1 + phi)/2, n)
  b = pow((1 - phi)/2, n)

  return a + b


print('{:.0f}'.format(get_lucas_number(2)))
