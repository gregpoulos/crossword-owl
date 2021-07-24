from collections import OrderedDict
from functools import total_ordering
from owllib import SCRABBLE_VALUES
import re
from unidecode import unidecode

@total_ordering
class Word:
  def __init__(self, token, score=0):
    self.token = token
    self.score = score
    self.lemma = self.lemmatize()

  def __hash__(self):
    return hash((self.token, self.score))

  def __eq__(self, other):
    return (self.token == other.token) and (self.score == other.score)

  def __lt__(self, other):
    return ((len(self.lemma) < len(other.lemma)) or
            (self.lemma < other.lemma) or
            (self.score < other.score) or
            (self.token < other.token))

  def lemmatize(self):
    return re.sub(r'\W', '', unidecode(self.token)).upper()
    
  def scrabble(self):
    return sum(SCRABBLE_VALUES[char] for char in self.lemma)
