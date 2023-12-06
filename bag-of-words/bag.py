import re
from collections import defaultdict

file = open('words.txt', 'r')
text = file.read()
text = re.sub("\[\d+\]", "", text)
text = re.sub("\n", " ", text)
text = re.sub("\(|\)|\.|,", "", text)
text = text.lower()
words = text.split(" ")
bag = defaultdict(lambda: 0)

for word in (words):
  # WITHOUT defaultdict
  # if bag.get(word):
  #   bag[word] += 1
  # else:
  #   bag[word] = 1

  bag[word] += 1

print(bag)
