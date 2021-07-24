from collections import OrderedDict as odict
import csv

class WordList:
  WORD_FIELDNAME = 'word'
  SCORE_FIELDNAME = 'score'
  DEFAULT_SCORE = 0

  def __init__(self, file, default_score=DEFAULT_SCORE):
    reader = csv.DictReader(file)
    if reader.fieldnames[0] != WordList.WORD_FIELDNAME:
      raise Exception("Couldn't parse .owl file: first field name must be 'word'")
    self.fieldnames = set(reader.fieldnames) - set(WordList.WORD_FIELDNAME)

    # if wordlist isn't prescored, add a 'score' attribute to each word
    prescored = WordList.SCORE_FIELDNAME in self.fieldnames
    if not prescored:
      self.fieldnames.add(WordList.SCORE_FIELDNAME)

    self.wl = odict()
    for row in reader:
      word = row[WordList.WORD_FIELDNAME]
      if not prescored:
        row[WordList.SCORE_FIELDNAME] = WordList.DEFAULT_SCORE
      self.wl[word] = row


  def write_to_dictfile(self):
    return False
