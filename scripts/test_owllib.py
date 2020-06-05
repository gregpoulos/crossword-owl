from owllib import Word
import pytest

TEST_WORD_BASIC = "snorlax"
TEST_WORD_COMPOUND = "Snor Lax"
TEST_WORD_DIACRITICS = "snörlàx"
TEST_WORD_LEMMA = "SNORLAX"

def test_lemmatize():
  w = Word(TEST_WORD_BASIC)
  assert w.lemma == TEST_WORD_LEMMA
  
  w = Word(TEST_WORD_COMPOUND)
  assert w.lemma == TEST_WORD_LEMMA
  
  w = Word(TEST_WORD_DIACRITICS)
  assert w.lemma == TEST_WORD_LEMMA
