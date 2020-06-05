from collections import defaultdict
from unidecode import unidecode

SCRABBLE_VALUES = defaultdict(int, (
  ('A', 1), ('B', 3), ('C', 3), ('D', 2), ('E', 1), ('F', 4), ('G', 2), 
  ('H', 4), ('I', 1), ('J', 8), ('K', 5), ('L', 1), ('M', 3), ('N', 1), 
  ('O', 1), ('P', 3), ('Q', 10), ('R', 1), ('S', 1), ('T', 1), ('U', 1), 
  ('V', 4), ('W', 4), ('X', 8), ('Y', 4), ('Z', 10)
))

class Word:

  def __init__(self, token):
    self.token = token
    self.lemma = self.lemmatize()

  def lemmatize(self):
    return unidecode(self.token).translate(str.maketrans('', '', ' \'')).upper()

  def scrabble_score(self):
    return sum(SCRABBLE_VALUES[char] for char in self.lemma)
