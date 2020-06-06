from owllib import Word
import pytest

TEST_WORD_BASIC = "Snorlax"
TEST_WORD_BASIC_LEMMA = "SNORLAX"
TEST_WORD_BASIC_SCRABBLE_SCORE = 14 # (s, n, o, r, l, a) = 1; x = 8

TEST_WORD_COMPLEX = "Type: Null"
TEST_WORD_COMPLEX_LEMMA = "TYPENULL"

TEST_WORD_DIACRITICS = "Flabébé"
TEST_WORD_DIACRITICS_LEMMA = "FLABEBE"

TEST_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TEST_ALPHABET_SCRABBLE_SCORE = 87


@pytest.fixture
def basic_word():
  return Word(TEST_WORD_BASIC)

@pytest.fixture
def complex_word():
  return Word(TEST_WORD_COMPLEX)

@pytest.fixture
def word_with_diacritics():
  return Word(TEST_WORD_DIACRITICS)

@pytest.fixture
def alphabet():
  return Word(TEST_ALPHABET)


def test_lemmatize(basic_word, complex_word, word_with_diacritics):
  assert basic_word.lemmatize() == TEST_WORD_BASIC_LEMMA
  assert complex_word.lemmatize() == TEST_WORD_COMPLEX_LEMMA
  assert word_with_diacritics.lemmatize() == TEST_WORD_DIACRITICS_LEMMA

def test_scrabble_score(basic_word, alphabet):
  assert basic_word.scrabble_score() == TEST_WORD_BASIC_SCRABBLE_SCORE
  assert alphabet.scrabble_score() == TEST_ALPHABET_SCRABBLE_SCORE
