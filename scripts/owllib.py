from collections import defaultdict, OrderedDict
import re
from unidecode import unidecode

SCRABBLE_VALUES = defaultdict(int, (
  ('A', 1), ('B', 3), ('C', 3), ('D', 2), ('E', 1), ('F', 4), ('G', 2), 
  ('H', 4), ('I', 1), ('J', 8), ('K', 5), ('L', 1), ('M', 3), ('N', 1), 
  ('O', 1), ('P', 3), ('Q', 10), ('R', 1), ('S', 1), ('T', 1), ('U', 1), 
  ('V', 4), ('W', 4), ('X', 8), ('Y', 4), ('Z', 10)
))


@total_ordering
class Word:
  def __init__(self, token, score=0):
    self.token = token
    self.score = score
    self.lemma = self.normalize()

  def __hash__(self):
    return hash((self.token, self.score))

  def __eq__(self, other):
    return (self.token == other.token) and (self.score == other.score)

  def __lt__(self, other):
    return ((len(self.lemma) < len(other.lemma)) or
            (self.lemma < other.lemma) or
            (self.score < other.score) or
            (self.token < other.token))

  def normalize(self):
    return re.sub(r'\W', '', unidecode(self.token)).upper()
    
  def scrabble(self):
    return sum(SCRABBLE_VALUES[char] for char in self.lemma)


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
