import nltk.tokenize
from nltk.tokenize import RegexpTokenizer
import nltk, re, pprint
import string
import matplotlib
import operator
import matplotlib.pyplot as plt
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
from bs4 import BeautifulSoup
from nltk.lm import NgramCounter
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


f = open('wiki_20', 'r', encoding ='utf8')
raw = f.read().replace(',',' ').replace('.', ' ').replace('-',' ').replace('(',' ').replace(')',' ').replace('"', ' ').replace("'", '').replace(':',' ').lower()
#print(raw)

soup = BeautifulSoup(raw, 'html.parser').get_text()
#print(soup)

tokenizer = RegexpTokenizer('\w+|\$[\d].]+|\S+')
tokens = tokenizer.tokenize(soup)
#print(tokens)


def numberlist(input, markdown):
    sum=0
    sum1=0
    i=0
    count=0
    c, v = zip(*input)
    v = sorted(v, reverse=True)
    # print(v)
    # for q in v:
    #     if q>200:
    #         print(q)
    for m in v:
        sum1= sum1+m
    limit = sum1
    print("Total count of corpus: ",limit)
    for i in v:
        sum=sum+i
        if sum>(markdown * limit):
            print("The required number to cover is: ",count)
            print("Sum value is: ",sum)
            return i
        else:
            count=count+1

def method(inp):
    unigram = ngrams(inp, 1)
    bigram = ngrams(inp, 2)
    trigram = ngrams(inp, 3)

    first = dict(Counter(unigram))
    second = dict(Counter(bigram))
    third = dict(Counter(trigram))
    # print(first)
    # print(second)
    # print(third)

    print("Number of unique unigrams: ",len(first))
    print("Number of unique bigrams: ",len(second))
    print("Number of unique trigrams: ",len(third))

    first = sorted(first.items(), key=lambda item: item[1])
    second = sorted(second.items(), key=lambda item: item[1])
    third = sorted(third.items(), key=lambda item: item[1])

    numberlist(first, 0.9)
    numberlist(second, 0.8)
    numberlist(third, 0.7)

    fina = []
    for q in first:
        if (q[1]>8):
            fina.append(q)
    first1 = dict(fina)
    # print(len(first1))
    finb = []
    for w in second:
        if (w[1] >8):
            finb.append(w)
    second1 = dict(finb)
    # print(len(second1))
    finc = []
    for e in third:
        if (e[1] >8):
            finc.append(e)
    third1 = dict(finc)
    # print(len(third1))

    plt.yscale('log')
    plt.plot([str(i) for i in first1.keys()], first1.values(), color='r')
    plt.show()
    plt.yscale('log')
    plt.plot([str(i) for i in second1.keys()], second1.values(), color='g')
    plt.show()
    plt.yscale('log')
    plt.plot([str(i) for i in third1.keys()], third1.values(), color='b')
    plt.show()


method(tokens)

ps = PorterStemmer()
my_list = []
tokens1 = tokens
for w in tokens1:
    my_list.append(ps.stem(w))

method(my_list)

wordnet_lemmatizer = WordNetLemmatizer()
the_list = []
tokens2 = tokens
for tk in tokens2:
    the_list.append(wordnet_lemmatizer.lemmatize(tk))

method(the_list)


