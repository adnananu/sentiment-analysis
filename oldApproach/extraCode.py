#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:40:55 2017

@author: naanu
"""

"""POS tagging issue for WORDNET"""

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''
    
    
    
""" LEMMATIZING """
lema = WordNetLemmatizer()
newLema = ""
for word, tag in tagged:
    newLema = lema.lemmatize(word,get_wordnet_pos(tag))

print(newLema)





""" STEMMING """

#stemmer = LancasterStemmer()
#stemWords = [stemmer.stem(word) for word in word_tokenize(text)]
#print(""" STEMMING """)
#print(stemWords)

"""HTML cleaning"""
fReading = open("/home/naanu/Music/dataForTest/sampleOnly.txt", 'r')
text =""
for line in fReading:
    text = line

print(text)
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

abc = cleanhtml(text)
print("\n\n\n"+abc)


#text = ''.join("Yes, this movie is a real thief. It stole some shiny Oscars "+
#            "from Avatar just because politicians wanted another war-hero "+
#            "movie to boost the acceptance (support?) for the wars U.S. is "+
#            "still fighting today. I do not really want to go here into "+
#            "politics, but come on, this is more clear than the summer sky."+
#            " Hurt locker does not really have anything outstanding, no "+
#            "real plot at all. I really feel myself in the 50's of Hungary"+
#            " Even if we consider this title a reasonable piece of "+
#            "the \"U.S. wars are cool\" genre, you surely have much"+
#            " better movies to choose from. <br /><br />It is slick &"+
#            " well produced, so it might last a while yet.  :D"+
#            " I was expecting a little something from \"K-911"+
#            " That's my whole $1.00 on this film."+
#            " >On 'Max Power's Scale of 1 to 10' I rate this movie: 1"+
#            " PS I would like to correct Corinthian's review"+
#            " The Cat In The Hat * out of *****"+
#            " who has never had sex because he was told in high school 20"+
#            " years prior that his penis is too big?"+
#            " I gave this loooooooooooong film a \"2\" because of the"+
#            " attractive actors and semi-sexy love scenes."+
#            " while Mariel would soon receive an Oscar nomination for"+
#            " Woody Allen’s MANHATTAN (1979)"+
#            " so i will go on.... (ctrl+c, ctrl+v) :)))"+
#            " This is one of the most inert movies ever made  so inert"+
#            " The only mystery here is how Oscar®"+
#            " they will rule us? Hmmm Yup 


#..hello"+
#            " Taken from the play by US' born Thornton Wilder"+
#            " in the future of the developing country of the USA"+
#            " I love \" The Da Vinci Code!"+
#            " Love luv lubb the Da Vinci Code!"+
#            " I'm not a big"+
#            " i love kirsten / leah / kate escapades"+
#            " i've ever read..."+
#            " ' The Da Vinci Code'it was AWESOME.")