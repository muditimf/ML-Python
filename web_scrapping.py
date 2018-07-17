#!/usr/bin/python3


from nltk.corpus import stopwords
import nltk
from bs4 import BeautifulSoup
import urllib.request
import html5lib

#import data from website

web_data=urllib.request.urlopen('https://twitter.com/')

#print web data
#print(web_data.read())


#applying web scrapping algorithm

souped_data=BeautifulSoup(web_data,'html5lib')

#to get only text

text_data=souped_data.get_text()

#print text data of website
#print(text_data)

#stopwords 
tokenised=[i for i  in text_data.split() if i in stopwords.words('english')]


#print(tokenised)

#word_count=nltk.FreqDist(tokenised)
#print(word_count)
word_count.plot(15)


#sentiment analysis

#polarity=nltk.pos_tag(tokenised)
#print(polarity)


