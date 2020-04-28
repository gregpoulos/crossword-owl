# crossword-owl
Open Word List for crossword constructors

## Dev setup notes

I'm assuming you're on a Mac.

1. Set up your Python virtual environment.
    `brew install pipx`
    `pipx install virtualenv`
    `cd path/to/repo`
    `virtualenv --python python3 .`
    `source ./bin/activate`

2. Install `nltk`.
    `pip install nltk`

3. Open the Python terminal and install the NLTK data. (See [the NLTK install guide](https://www.nltk.org/data.html#interactive-installer) for more info.)
    `import nltk`
    `nltk.download()`
