from nltk.tokenize import word_tokenize, sent_tokenize

example = "Hey! How are you? Dr. Sam - M.B.B.S., and M.D., is waiting for you. Mr. and Mrs. Shah are welcomed. Today's a pleasant day; Oh for a refreshing tea! Call us @123 for help."
words = word_tokenize(example)
for w in words:
    print(w)
sentences = sent_tokenize(example)
for s in sentences:
    print(s)