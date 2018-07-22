from autocorrect import spell
import nltk
from nltk.tokenize import word_tokenize

file = open("put.txt",newline='')
result = file.read()
words = word_tokenize(result)
for i in words:
    print(spell(i))
print(spell('servie'))
print(spell(u'mussage'))
print(spell(u'survice'))
print(spell(u'hte'))