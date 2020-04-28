#!/usr/bin/env python3

import sys

import nltk
from nltk.corpus import wordnet as wn

synsets = list(wn.all_synsets())
words = set()
outfile = sys.argv[1]

for name in [synset.name() for synset in synsets]:
  word = name[:name.find('.')]    # strip grammatical data
  word = word.replace('_', ' ')   # underscores to whitespace
  words.add(word)

words = sorted(list(words))

with open(outfile, 'w') as f:
  for word in words:
    f.write(f'{word}\n')
