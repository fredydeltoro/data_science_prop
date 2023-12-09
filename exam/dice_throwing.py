import random

random.seed(100)


def dice_th(times):
  frecuencies = {}
  distribution = {}

  # Generate all posible sums and store
  for i in range(2, 13):
    frecuencies[i] = 0

  # Throwing dices and storing result
  for _ in range(times):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    frecuencies[dice_1+dice_2] += 1

  # Calculating the distribution
  for _sum in frecuencies:
    distribution[_sum] = frecuencies[_sum]/(times*1.0)

  # Get by separate the sum and probabilities
  sums = list(distribution.keys())
  probabilities = list(distribution.values())

  # SCALE
  max_bar_length = 100

  # printing and improvised graphic with prints like this 7:########## (10.00%)
  for _sum, probability in zip(sums, probabilities):
    bar_length = int(probability * max_bar_length)
    # print like porcentage with this {:.2%}
    print("{}:{} ({:.2%})".format(_sum, '#' * bar_length, probability))


dice_th(random.randint(30, 100))
