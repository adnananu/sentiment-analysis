#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 21:00:55 2017

@author: naanu
"""

from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.datasets import imdb
import numpy as np
from keras.preprocessing.text import Tokenizer



#######################AD
print('Working with LSTM...')
max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

#print('Loading data...')
#(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
#print(len(x_train), 'train sequences')
#print(len(x_test), 'test sequences')
#
#
#print('Pad sequences (samples x time)')
#x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
#x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
#print('x_train shape:', x_train.shape)
#print('x_test shape:', x_test.shape)
#
#print('Build model...')
#model = Sequential()
#model.add(Embedding(max_features, 128))
#model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
#model.add(Dense(1, activation='sigmoid'))
#
## try using different optimizers and different optimizer configs
#model.compile(loss='binary_crossentropy',
#              optimizer='adam',
#              metrics=['accuracy'])
#
#print('Train...')
#model.fit(x_train, y_train,
#          batch_size=batch_size,
#          epochs=10,
#          validation_data=(x_test, y_test))
#score, acc = model.evaluate(x_test, y_test,
#                            batch_size=batch_size)
#print('Test score:', score)
#print('Test accuracy:', acc)

## save the model to disk
#filename = 'finalized_model.sav'
#pickle.dump(model, open(filename, 'wb'))

#data = "I am not feeling good"
#data = data.lower()
#tokenizer = Tokenizer(nb_words=2)
#tokenizer.fit_on_texts(data)
#sequences = tokenizer.texts_to_sequences(data)
#text = sequence.pad_sequences(sequences)
#print("Tokens", text)
#prediction = model.predict(np.array(text), batch_size=1, verbose = 1)[0] # taking the very first column index
#print("Result for sentiment: "+str(prediction * 100))


#training the tokenizer!!
bol = True
def cleanser(sentence):
   global bol
   sentence = str(sentence).lower()
   sentence = ''.join(s if s.isalpha() or s.isdigit() or s == "'" or s == " " else " " for s in sentence)
   words = str(sentence).split()
   #words = [word for word in words if word not in stopwords.words('english')]
   words = [word for word in words if word.isalpha()]
   if bol:
       print(words)
       bol = False
   return words

short_pos = open("positive.txt", "r").read()
short_neg = open("negative.txt", "r").read()
 
# move this up here
#all_words = []
#documents = []
 
#  j is adject, r is adverb, and v is verb
# allowed_word_types = ["J","R","V"]
allowed_word_types = ["J"]
d = []
 
for p in short_pos.split('\n'):
    d.extend(cleanser(p))
    
for p in short_neg.split('\n'):
    d.extend(cleanser(p))



data = "i am so happy"
data = data.lower()
tokenizer = Tokenizer(num_words=250000)
tokenizer.fit_on_texts(d)
test_case = tokenizer.texts_to_sequences(data)
print("text to sequence", test_case)
test_case = sequence.pad_sequences(test_case,maxlen=maxlen)
print("Tokens after pad sequence", test_case)
#prediction = model.predict(test_case)[0] # taking the very first column index
#print("Result for sentiment 2: "+str(prediction * 100))
