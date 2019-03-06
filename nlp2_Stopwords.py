from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "Hi This is an example to show the result of filtering the stop words from this very own sentence"
#stopwords = set(stopwords.words())
words = word_tokenize(example)
filtered_sentence = ""
for w in words:
    if w not in stopwords.words():
        #filtered_sentence.append(w)
        #print(w)
        filtered_sentence += w + " "
print(filtered_sentence)