#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 10:41:56 2017

@author: naanu
"""


import glob, os


os.chdir("/home/naanu/Music/dataset/aclImdb/train/pos/")
counter = 0
positiveDataArray = []
for fle in glob.glob("*.txt"):
    with open(fle) as f:
        text = f.read()
        text = "1\t" + text
        positiveDataArray.insert(counter, text)        
#        print(positiveDataArray[counter])
        counter = counter + 1
        print(str(counter)+ "as 1")
        
os.chdir("/home/naanu/Music/dataset/aclImdb/train/neg/")

for fle in glob.glob("*.txt"):
    with open(fle) as f:
        text = f.read()
        text = "0\t" + text
        positiveDataArray.insert(counter, text)        
#        print(positiveDataArray[counter])
        counter = counter + 1
        print(str(counter)+ "as 0")
        
writeFile = open('/home/naanu/Music/Final_Pos_Neg_File.txt', 'w+')
for item in positiveDataArray:
#    print(item)
    writeFile.write("%s\n" % item)
    text = writeFile.read()
#    print(text)
    
    
    
