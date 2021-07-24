class WordList:
  def __init__(self, wordlist=OrderedDict()):
    self.wordlist = wordlist

  def add(self, word):
    if word.lemma in self.wordlist:
      doppels = self.wordlist[word.lemma]
      doppels.remove(word) # the new word overwrites an existing word with the same token
      doppels.add(word)
    else:
      self.wordlist[word.lemma] = {word}

  def merge(self, other):
    for doppels in other.wordlist.values():
      for doppel in doppels:
        self.add(doppel)
