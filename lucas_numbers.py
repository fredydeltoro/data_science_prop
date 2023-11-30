# Get lucas secuence
def lucas_numbers(num_of_elements):
  numbers = [2, 1]

  for _ in range(2, num_of_elements):
    numbers.append(numbers[-2] + numbers[-1])

  return numbers


print(lucas_numbers(3))
