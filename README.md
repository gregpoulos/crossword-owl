# crossword-owl
Open Word List for crossword constructors

## Dev setup notes

I'm assuming you're on a Mac.

0. Clone the repo:
   - `git clone https://github.com/gregpoulos/crossword-owl.git`
   - `cd crossword-owl`

1. Set up your Python environment:
   - `python3 -m venv .env --prompt owl-env`
   - `source .env/bin/activate`
   - `pip install -r requirements.txt`

2. Open the Python terminal and install the NLTK data. (See [the NLTK install guide](https://www.nltk.org/data.html#interactive-installer) for more info.)
    - `import nltk`
    - `nltk.download()`
