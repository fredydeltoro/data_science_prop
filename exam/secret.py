# Get secret number of getting the max and min value from the array
def secret(arr=[0]):
  max_val = arr[0]
  min_val = arr[0]

  for el in arr:
    # validation to get the curren min value
    if el < min_val:
      min_val = el

    # validation to get the curren max value
    if el > max_val:
      max_val = el

  # return the secret value result of max minus min
  return max_val - min_val


print(secret([5, 6, 3, 9, 1, 10]))
