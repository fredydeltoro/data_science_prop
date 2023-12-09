# Generate an array of catalan numbers
def catalan_numbers(num_of_elements):
  numbers = []
  for i in range(num_of_elements):
    numbers.append(get_catalan_number(i))

  return numbers


# Get just one catalan number
def get_catalan_number(n):
  return factorial(2*n)/(factorial(n+1)*factorial(n))


# factorial throuth tail recursion
def factorial(n):
  return tail_fact(n, 1)


# tail recursion
def tail_fact(n, a):
  if n == 0:
    return a
  else:
    return tail_fact(n-1, n*a)


print(catalan_numbers(13))
