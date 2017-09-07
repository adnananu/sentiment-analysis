#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 22:47:07 2017

@author: naanu
"""




def cleanser(sentence):

   sentence = str(sentence).lower()
   sentence = ''.join(s if s.isalpha() or s.isdigit() or s == "'" or s == " " else " " for s in sentence)
   words = str(sentence).split()
   #words = [word for word in words if word not in stopwords.words('english')]
   words = [word for word in words if word.isalpha()]

   return words

short_pos = open("positive.txt", "r").read()
short_neg = open("negative.txt", "r").read()
 
# move this up here
d = []
 
for p in short_pos.split('\n'):
    d.extend(cleanser(p))
    
for p in short_neg.split('\n'):
    d.extend(cleanser(p))
            
print (len(d))