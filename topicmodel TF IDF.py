# -*- coding: UTF-8 -*-
import jieba, os
from gensim import corpora, models, similarities
import codecs
import conf

train_set = []


stopwords = codecs.open('stopWords/GlobalStopWords.txt','rb',encoding='utf8').readlines()
stopwords = [ w.strip('\n') for w in stopwords ]
stopwords.extend(conf.LocalStopWords)



walk = os.walk('output1')
for root, dirs, files in walk:

    l=[]

    for name in files:
        f = open(os.path.join(root, name), 'r',encoding='UTF-8')
    raw = f.read()
    word_list = list(jieba.cut(raw, cut_all = False))

    for x in word_list:
        if x.strip() not in stopwords:
            l.append(x)

    train_set.append(l)

texts=train_set


dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=conf.num_topics, id2word=dictionary)

for x in ldamodel.print_topics(num_topics=conf.num_topics, num_words=conf.num_words):
    print(x)
