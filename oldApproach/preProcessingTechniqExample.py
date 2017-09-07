#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:40:00 2017

@author: naanu
"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

from nltk.corpus import stopwords
nltk.download('stopwords')
from string import punctuation

text = "Can't I have some juice to drink? Joe went to the store."

sents = sent_tokenize(text)
print(sents)

word = [word_tokenize(sent) for sent in sents]
print(word)



""" Stop words """

customStopWords = set(stopwords.words('english')+list(punctuation))
wordsWOStopWords = [newWord for newWord in word_tokenize(text) if newWord not in customStopWords]
print(wordsWOStopWords)

""" WITH TreebankWordTokenizer """

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
tokenizer.tokenize("doesn't I have some juice to drink?")



""" WITH Lematization """
from nltk.stem.wordnet import WordNetLemmatizer 
lem = WordNetLemmatizer()
word = "multiplying" 
lem.lemmatize(word, "v")


from nltk.stem.porter import PorterStemmer 
stem = PorterStemmer()
stem.stem(word)



""" TOKENIZING SENTENCES """


import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
tokenizer.tokenize(para)['Hello World.', "It's good to see you.", 'Thanks for buying this book.']


""" TOKENIZING WORDS """

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
tokenizer.tokenize('Hello World.')['Hello', 'World', '.']


""" lemmas and synonyms in WordNet """

from nltk.corpus import wordnet
nltk.download('wordnet')
syn = wordnet.synsets("book")[0]
lemmas = syn.lemmas()
print(len(lemmas))





