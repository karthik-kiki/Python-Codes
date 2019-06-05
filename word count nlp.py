import nltk
from nltk import *
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords

sample="Hello, I am Karthik and it ain't a lucky day today. Sir scolded me."
sent=(sent_tokenize(sample))        #splitting sentence
word=(word_tokenize(sample))        #splitting words
print(sent)
print(word)

stop_word=set(stopwords.words("english"))       #depicts all stopwords fot english language
new=[]
for i in word:
    if i not in stop_word:
        new.append(i)
print(new)

tot_sent=FreqDist(sent)     #total sentences length
count=len(tot_sent)
print(count)
tot_word=FreqDist(word)     #total words length
counts=len(tot_word)
print(counts)
print(tot_word.most_common(25))     #how much times a word repeat




