# crossword-owl
Open Word List for crossword constructors

## Dev setup

1. Clone the repo:
   - `git clone https://github.com/gregpoulos/crossword-owl.git`
   - `cd crossword-owl`

2. Set up your Python environment:
   - `python3 -m venv .env --prompt owl-env`
   - `source .env/bin/activate`
   - `pip install -r requirements.txt`

2. [Optional] [Install the NLTK data.](https://www.nltk.org/data.html#interactive-installer) Open the Python terminal and run:
    - `import nltk`
    - `nltk.download()`

3. To run the tests:
    - `pytest src/test`


## Data Model

In the context of this document, we will use the term "word" to refer to any individual word, phrase, partial phrase, or string of characters that could be used as an entry in a puzzle. All of the follow may be considered "words" for our purposes:

* pancake
* Snorlax
* charismatic megafauna
* is to
* A-One
* A-1
* Jumping Jehoshaphat
* Jumpin' Jehoshaphat
* resume
* résumé
* Why I oughta ... 

Individual words (or phrases, etc.) are represented as `Word` objects. The OwlLib library uses the `WordList` object to represent a list of words.

### `Word`s

Any given `Word` has a few associated properties:

* The _token_ is the word's representation as a Unicode string.
* The _lemma_ is a normalized version of the word.
* The _score_ is the "quality" of a word, with higher numbers representing "better" words.

A simple word like "pancake" would have `"pancake"` as its token and `"PANCAKE"` as its lemma. It is possible for two different words to have the same lemma; for instance, the words "résumé" and "resume" would both be normalized to the lemma `"RESUME"`.

Here's the basic normalization process:

* Convert everything to ASCII (i.e., strip diacritics)
* Capitalize all letters
* Strip all white space

In theory, different normalization processes could be supported. For instance, maybe you'd want to convert all numerals into their spelled-out versions? Right now that's not possible -- but it could be!

TBD: A word could have one or more sample clues.


### `WordList`s

A `WordList` is an ordered list of `Word` objects (surprise!), but also supports the notion of a _doppel_ -- that is, two different words that normalize to the same lemma. So even though "résumé" and "resume" are represented as two distinct `Word` objects, they will share an entry in a `WordList` because they map to the same lemma, `"RESUME"`.


### Data Sources

* `common.owl` is Michael Wehar's [`5000-more-common.txt` word list](https://github.com/MichaelWehar/Public-Domain-Word-Lists), which has been released into the public domain.

* `broda.owl` is [Peter Broda's word list](https://peterbroda.me/crosswords/wordlist/), which he has generously provided to the community for free use.

* `wordnet-scrabble.owl` is derived from [Princeton's WordNet](https://wordnet.princeton.edu/), a lexical database for English, which is available under the [WordNet 3.0 license](https://wordnet.princeton.edu/license-and-commercial-use) for unencumbered use.

* `test-capitals.owl` and `test-default.owl` are toy word lists I created for testing purposes.
