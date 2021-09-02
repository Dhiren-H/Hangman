def play():
  wordsite = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
  response = requests.get(wordsite)
  WORDS = response.content.splitlines()
  word = random.choice(WORDS)
  def randomword():
    
    while len(word) > 3:
      return word
    else:
      randomword()
  print("  Length of word: " + str(len(word)))
  question = input("  Guess a letter: ")
