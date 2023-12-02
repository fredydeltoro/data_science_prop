def get_list_of_primes(n):
  numbers = range(2, n+1)
  primes = [2]
  numbers = filter_mulitples(primes[0], numbers)

  while True:
    current = numbers[0]
    if pow(current, 2) < n:
      primes.append(current)
      numbers = filter_mulitples(current, numbers)
    else:
      break

  return primes + numbers

# Filter all multiples of the current number


def filter_mulitples(number, arr):
  for i, el in enumerate(arr):
    if el % number == 0:
      arr.pop(i)

  return arr


print(get_list_of_primes(100))

# Jose Alfredo Monroy
