from owllib.word import Word
import pytest

TEST_WORD_BASIC = "Snorlax"
TEST_WORD_BASIC_LEMMA = "SNORLAX"
TEST_WORD_BASIC_SCRABBLE_SCORE = 14 # (s, n, o, r, l, a) = 1; x = 8

TEST_WORD_COMPLEX = "Type: Null"
TEST_WORD_COMPLEX_LEMMA = "TYPENULL"

TEST_WORD_DIACRITICS = "Flabébé"
TEST_WORD_DIACRITICS_LEMMA = "FLABEBE"


@pytest.fixture
def basic_word():
  return Word(TEST_WORD_BASIC)

@pytest.fixture
def complex_word():
  return Word(TEST_WORD_COMPLEX)

@pytest.fixture
def word_with_diacritics():
  return Word(TEST_WORD_DIACRITICS)


def test_word_hashing():
  w1 = Word('Snorlax')
  w2 = Word('Snorlax')
  w3 = Word('Snor Lax')
  assert {w1, w2, w3} == {w1, w3}
  assert {w1, w3} - {w1} == {w3}
  assert set() - {w1} <= {w1} - set()

def test_lemmatize(basic_word, complex_word, word_with_diacritics):
  assert basic_word.lemmatize() == TEST_WORD_BASIC_LEMMA
  assert complex_word.lemmatize() == TEST_WORD_COMPLEX_LEMMA
  assert word_with_diacritics.lemmatize() == TEST_WORD_DIACRITICS_LEMMA

def test_scrabble(basic_word):
  assert basic_word.scrabble() == TEST_WORD_BASIC_SCRABBLE_SCORE
  assert Word('ABCDEFGHIJKLMNOPQRSTUVWXYZ').scrabble() == 87
