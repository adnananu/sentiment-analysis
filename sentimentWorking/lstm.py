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
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import collections
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import numpy as np
import sys, Utility
from PreProcessData import cleanData

from numpy import array
import time

DATA_DIR = "/home/naanu/Music/dataForTest/testData.txt"

MAX_FEATURES = 12953 #15487 #114825 #2000
MAX_SENTENCE_LENGTH = 558 #1259 #2818 #40

EMBEDDING_SIZE = 128
HIDDEN_LAYER_SIZE = 64
BATCH_SIZE = 32
NUM_EPOCHS = 10
vocab_size = 0
word2index = {}
index2word = {}
# Read training data and generate vocabulary
maxlen = 0
word_freqs = collections.Counter()
num_recs = 0
history = ""
model = ""
xxtest = ""
yytest = ""
toknizer = ""
X = np.empty((5, ), dtype=list)
TestList  = np.empty((5, ), dtype=list)
d = []

def main(): #idiomatic way: allows me to write code in the order I like
    readData()
    
    
def readData():
    
    global maxlen, num_recs
    
    x = Utility.UtilityClass()       
    try:
        with open(DATA_DIR, 'r') as textFile:
            for line in textFile:
                label, sentence = line.strip().split("\t",1)
                sentence = sentence.replace('\t'," ")
                sentence = cleanData(x, \
                                    sentence,True,True,True,True,True,True)
                #decode the UTF-8-encoded String into a unicode string.
                words = word_tokenize(sentence)
                if len(words) > maxlen:
                    maxlen = len(words)
                for word in words:
                    word_freqs[word] += 1
                num_recs += 1
    #        ftrain.close()
            
            # Get some information about our corpus
            print("\nResult for Counting")
            print ("\tMax length: "+str(maxlen)) # 42  2818
            print ("\tWord frequency: "+str(len(word_freqs))) # 2313 114825
            del x
            createDict()
    except IOError, (errno, strerror):
        print "I/O error(%s): %s" % (errno, strerror)
    except KeyError, e:
        print 'I got a KeyError - reason "%s"' % str(e)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

        ######======================================######
   

def createDict():
    # 1 is UNK, 0 is PAD
    # We take MAX_FEATURES-1 featurs to accound for PAD
    global vocab_size, index2word, word2index
    vocab_size = min(MAX_FEATURES, len(word_freqs)) + 2
    word2index = {x[0]: i+2
                 for i, x in enumerate(word_freqs.most_common(MAX_FEATURES))}
    
    # using the same above word2index array
    word2index["PAD"] = 0
    word2index["UNK"] = 1
    index2word = {v:k for k, v in word2index.items()}
    print("\nEnd Part # 2") 
    trainTokenizer()
    sentToSequence()
   

        ###================================================####
        
def trainTokenizer():
    print("\nBefore Part # 3: Training Tokenizer")
    global toknizer,d
    x = Utility.UtilityClass()
    toknizer = Tokenizer(num_words=MAX_FEATURES)
    d = [None]*num_recs
    i = 0
    with open(DATA_DIR, 'r') as textFile:
        for line in textFile:
            label, sentence = line.strip().split("\t",1)
            sentence = sentence.replace('\t'," ")
            sentence = cleanData(x, \
                                    sentence,True,True,True,True,True,True)
                #decode the UTF-8-encoded String into a unicode string.
#            words = word_tokenize(sentence)
            sentence = sentence.encode("utf-8")
            d [i] = sentence
            i += 1 
#        print(d)
#        print("fitting text!")
        toknizer.fit_on_texts(d)
#        print(toknizer.word_index)

        ###================================================####
        
        
def sentToSequence():
    print("\nStarting Part # 3")
    global model, xxtest, yytest, history, toknizer, vocab_size, X,TestList
    x = Utility.UtilityClass()       
    
    X = np.empty((num_recs, ), dtype=list)
    TestList = np.empty((num_recs, ), dtype=list)
    y = np.zeros((num_recs, ))
    i = 0
    with open(DATA_DIR, 'r') as textFile:
        for line in textFile:
            label, sentence = line.strip().split("\t",1)
            sentence = sentence.replace('\t'," ")
            sentence = cleanData(x, \
                                    sentence,True,True,True,True,True,True)
                #decode the UTF-8-encoded String into a unicode string.
#            words = word_tokenize(sentence)
#            seqs = []
#            for word in words:
#                if word in word2index:   #if word2index.has_key(word):
#                    seqs.append(word2index[word])
#                else:
#                    seqs.append(word2index["UNK"])
#            
#            X[i] = seqs
#            if i < 1:
#                print("\nSeq Value: ")
#                print(seqs)
#                print("\nX Value: ")
#                print(X)
            seq = toknizer.texts_to_sequences([sentence.encode("utf-8")])
#            TestList[i] = sequence.pad_sequences(seq, maxlen=MAX_SENTENCE_LENGTH)
#            X[i] = sequence.pad_sequences(seq, maxlen=MAX_SENTENCE_LENGTH)
            X[i] = seq[0]
#            if i < 1:
#                print("\n Test Seq Value: ")
#                print(seq)
#                print("\n Test list Value: ")
#                print(TestList)
        
            y[i] = int(label)
            i += 1
#    print("delete Object X")
    del x
#    print("working with sequence")
#    print(X.shape)
#    print("Test list shape with sequence")
#    print(TestList.shape)
    vocab_size = min(MAX_FEATURES, len(word_freqs))
#    X = array(X)
#    print(X)
    # Pad the sequences (left padded with zeros)
    X = sequence.pad_sequences(X, maxlen=MAX_SENTENCE_LENGTH)
#    print("After padding ")
#    print(X)
#    print("\nAfter as array List\n ")
#    print(np.asarray(TestList))

    # Split input into training and test
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, 
                                                     random_state=42)
    print(Xtrain.shape, Xtest.shape, ytrain.shape, ytest.shape)
    print("\nStarting Part # 4 (Model building)")
    # Build model
#    time.sleep(45)
    
    model = Sequential()
    model.add(Embedding(vocab_size, EMBEDDING_SIZE, input_length=MAX_SENTENCE_LENGTH))
    model.add(SpatialDropout1D(Dropout(0.2)))
    model.add(LSTM(HIDDEN_LAYER_SIZE, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1))
    model.add(Activation("sigmoid"))
     
    model.compile(loss="binary_crossentropy", optimizer="adam", 
#sparse_categorical_crossentropy
#    model.compile(loss="categorical_crossentropy", optimizer="adam", 
                   metrics=["accuracy"])
     
    history = model.fit(Xtrain, ytrain, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS, validation_data=(Xtest, ytest))
    xxtest = Xtest
    yytest = ytest
    plotAndEvaluate()



def plotAndEvaluate():
    print("Starting Part # 5")
    global history, xxtest, yytest
    # plot loss and accuracy
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
    #evaluate
    score, acc = model.evaluate(xxtest, yytest, batch_size=BATCH_SIZE)
    print("Test score: %.3f, accuracy: %.3f" % (score, acc))
    test()

def test():
    print("Starting Part # 6") 
    
    for i in range(10):
        idx = np.random.randint(len(xxtest))
        xtest = xxtest[idx].reshape(1,MAX_SENTENCE_LENGTH) #40 #1259
        ylabel = yytest[idx]
        ypred = model.predict(xtest)[0][0]
        sent = " ".join([index2word[x] for x in xtest[0].tolist() if x != 0])
        print("%.0f\t%d\t%s" % (ypred, ylabel, sent))

if __name__ == '__main__':
    main()


        ####===============================================####
