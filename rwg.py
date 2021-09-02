import requests
import random

wordsite = "http://www.mieliestronk.com/corncob_lowercase.txt"
response = requests.get(wordsite)
WORDS = response.content.splitlines()

def randomword():
  word = random.choice(WORDS)
  while len(word) > 3:
    return word
  else:
    randomword()

print (randomword())
