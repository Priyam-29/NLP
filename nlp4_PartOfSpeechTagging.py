import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize  #PunktSentenceTokenizer is an ML based tokenizer

train_text = state_union.raw("2005-GWBush.txt")    # raw() returns the whole file as a single string
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

for i in tokenized:
    words = word_tokenize(i)
    print(nltk.pos_tag(words))   #it returns tuples



