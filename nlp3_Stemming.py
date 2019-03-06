from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example = ["python", "pythoner", "pythoned", "pythoning", "pythonly"]
for w in example:
    print(ps.stem(w))

new_text = "It is very important for a pythoner to python pythonly while pythoning the pythoned Python code"
words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))