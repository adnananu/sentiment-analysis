#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 18:15:45 2017

@author: naanu
"""

from keras.layers.core import Activation, Dense, Dropout, SpatialDropout1D
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
import collections
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import numpy as np
import os

DATA_DIR = "../dataset"

MAX_FEATURES = 15487 #114825 #2000
MAX_SENTENCE_LENGTH = 1259 #2818 #40

EMBEDDING_SIZE = 128
HIDDEN_LAYER_SIZE = 64
BATCH_SIZE = 32
NUM_EPOCHS = 10

# Read training data and generate vocabulary
maxlen = 0
word_freqs = collections.Counter()
num_recs = 0
ftrain = open("/home/naanu/Music/dataForTest/testData.txt", 'r')
count = 0
lineNumb = 0
for line in ftrain:
    
#    print(count)
#    tabs = line.count('\t')
#    if tabs > 1:
#        print(tabs, count)
#        break
#    if count == 1584:
#        tabs = line.count('\t')
#        print(tabs)
    label, sentence = line.strip().split("\t",1)
    sentence = sentence.replace('\t'," ")
    words = word_tokenize(sentence.lower().decode("utf-8")) #You are doing it the wrong way around. You are reading UTF-8-encoded data, so you have to decode the UTF-8-encoded String into a unicode string.So just replace .encode with .decode, and it should work (if your .csv is UTF-8-encoded).
    if len(words) > maxlen:
        maxlen = len(words)
        lineNumb = count
    for word in words:
        word_freqs[word] += 1
    num_recs += 1
    count = count +1
ftrain.close()

    ## Get some information about our corpus
print("\nResult for Counting")
print("\tLine number for long string: "+str(lineNumb))
print ("\tMax length: "+str(maxlen)) # 42  2818
print ("\tWord frequency: "+str(len(word_freqs))) # 2313 114825
    
    #==============================================================================
    # 
    # 
    # # 1 is UNK, 0 is PAD
    # # We take MAX_FEATURES-1 featurs to accound for PAD

print("Starting Part # 2")    
vocab_size = min(MAX_FEATURES, len(word_freqs)) + 2
word2index = {x[0]: i+2
             for i, x in enumerate(word_freqs.most_common(MAX_FEATURES))}
#    #Testing the for loop
#    #for i, x in enumerate(word_freqs.most_common(MAX_FEATURES)):
#    #    print("i: "+str(i), "x: "+str(x))
#    #Result ofword2index
#    # {'appeals': 998,
#    # 'chick': 999,
#    # 'arenas': 1000,
#    # 'genre': 1001,}
#
#    #using the same above word2index array
word2index["PAD"] = 0
word2index["UNK"] = 1
index2word = {v:k for k, v in word2index.items()}
#    #Result of index2word
#    #{922: 'bible',
#    # 923: 'libraries',
#    # 924: 'witchcraft',
#    # 925: 'color',
#    # 926: 'dance',
#    # 927: 'obnoxious',
#    # 928: 'thinks'}
#
##==============================================================================
#
## 
## # convert sentences to sequences
#

print("Starting Part # 3")

X = np.empty((num_recs, ), dtype=list)
y = np.zeros((num_recs, ))
i = 0
ftrain = open("/home/naanu/Music/dataForTest/testData.txt", 'r')
for line in ftrain:
    label, sentence = line.strip().split("\t",1)
    sentence = sentence.replace('\t'," ")
    words = word_tokenize(sentence.lower().decode("utf-8"))
    seqs = []
    for word in words:
        if word in word2index:   #if word2index.has_key(word):
            seqs.append(word2index[word])
        else:
            seqs.append(word2index["UNK"])
    X[i] = seqs
    y[i] = int(label)
    i += 1
ftrain.close()
# 
# # Pad the sequences (left padded with zeros)
X = sequence.pad_sequences(X, maxlen=MAX_SENTENCE_LENGTH)
    # 
    # Split input into training and test
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, 
                                                 random_state=42)
print(Xtrain.shape, Xtest.shape, ytrain.shape, ytest.shape)
 

print("Starting Part # 4")
   # 
    # # Build model
model = Sequential()
model.add(Embedding(vocab_size, EMBEDDING_SIZE, 
                     input_length=MAX_SENTENCE_LENGTH))
model.add(SpatialDropout1D(Dropout(0.2)))
model.add(LSTM(HIDDEN_LAYER_SIZE, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1))
model.add(Activation("sigmoid"))
 
model.compile(loss="binary_crossentropy", optimizer="adam", 
               metrics=["accuracy"])
 
history = model.fit(Xtrain, ytrain, batch_size=BATCH_SIZE, 
                     epochs=NUM_EPOCHS,
                     validation_data=(Xtest, ytest))


print("Starting Part # 5")
    # # plot loss and accuracy
plt.subplot(211)
plt.title("Accuracy")
plt.plot(history.history["acc"], color="g", label="Train")
plt.plot(history.history["val_acc"], color="b", label="Validation")
plt.legend(loc="best")
 
plt.subplot(212)
plt.title("Loss")
plt.plot(history.history["loss"], color="g", label="Train")
plt.plot(history.history["val_loss"], color="b", label="Validation")
plt.legend(loc="best")
 
plt.tight_layout()
plt.show()
 
 # evaluate
score, acc = model.evaluate(Xtest, ytest, batch_size=BATCH_SIZE)
print("Test score: %.3f, accuracy: %.3f" % (score, acc))



print("Starting Part # 6") 

for i in range(10):
    idx = np.random.randint(len(Xtest))
    xtest = Xtest[idx].reshape(1,1259) #40
    ylabel = ytest[idx]
    ypred = model.predict(xtest)[0][0]
    sent = " ".join([index2word[x] for x in xtest[0].tolist() if x != 0])
    print("%.0f\t%d\t%s" % (ypred, ylabel, sent))


#==============================================================================
