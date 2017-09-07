#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:48:12 2017

@author: naanu
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import collections, re
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from bs4 import BeautifulSoup
from contractionRemoval import expandContractions
import RepeatReplacer
#nltk.download('popular')
#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

"""Loading Data"""
fReading = open("/home/naanu/Music/dataForTest/testData.txt", 'r')


"""   Variable Decalartion    """
maxlen = 0
count = 0
lineNumb = 0
num_recs = 0
word_freqs = collections.Counter()


"""     Counting WORD frequency and max Lenght       """

for line in fReading:
    label, sentence = line.strip().split("\t",1)
    sentence = sentence.replace('\t'," ")
    words = word_tokenize(sentence.lower().decode("utf-8"))
    if len(words) > maxlen:
        maxlen = len(words)
        lineNumb = count
    for word in words:
        word_freqs[word] += 1
    num_recs += 1
    count = count +1
fReading.close()

print("\nResult for Counting")
print ("\tMax length: "+str(maxlen))
print ("\tWord frequency: "+str(len(word_freqs)))



""" STOP WORDS"""

#
#customStopWords = set(stopwords.words('english')+list(punctuation))
#afterStopWords = [word for word in word_tokenize(text) if word not in customStopWords]
#print(""" STOP WORDS""")
#print(afterStopWords)
#afterStopWords = " ".join(afterStopWords)



#""" POS Tagging """
#
#POSWords = word_tokenize(afterStopWords)
#tagged = nltk.pos_tag(POSWords)
#print(""" POS """)
#print(tagged)

def cleanHTML(raw_text):
    return BeautifulSoup(raw_text).text

fReading = open("/home/naanu/Music/dataForTest/sampleOnly.txt", 'r')
text =""
for line in fReading:
    text = line

# emotional symbols may affect the meaning of the review
smileys = """:-) :) :o) :] :3 :c) :> =] 8) =) :} :^)
                :D 8-D 8D x-D xD X-D XD =-D =D =-3 =3 B^D :D :\ :| ;( :( :/ :-( :'( :D :P""".split()
                
smiley_pattern = "|".join(map(re.escape, smileys))
review_text = re.sub(smiley_pattern, "", cleanHTML(text))


def removeExtra(raw_text):
    return re.sub("[^A-Za-z.']+", ' ', text)



contRemov = expandContractions(text)

rr = RepeatReplacer.RepeatReplacing()
repReplacer = rr.replace(text.lower().decode("utf-8"))# Converting to unicode!