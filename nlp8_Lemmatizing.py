#Better than stemming which sometimes create non-existent words

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better", pos="a")) #mentioning part of speech = adjecive as by default it considers noun
print(lemmatizer.lemmatize("best"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("running"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("pythonly"))
