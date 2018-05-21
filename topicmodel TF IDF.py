import jieba, os
from gensim import corpora, models, similarities
import codecs


train_set = []

stopwords = codecs.open('stopWords/1893（utf8）.txt','r',encoding='utf8').readlines()
stopwords = [ w.strip() for w in stopwords ]
stopwords.append(' ')
stopwords.append('\u200b')
stopwords.append('\n')

walk = os.walk('output1')
for root, dirs, files in walk:

    l=[]

    for name in files:
        f = open(os.path.join(root, name), 'r',encoding='UTF-8')
    raw = f.read()
    word_list = list(jieba.cut(raw, cut_all = False))

    for x in word_list:
        if x not in stopwords:
            l.append(x)

    train_set.append(l)

texts=train_set


dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=1, id2word=dictionary)

for x in ldamodel.print_topics(num_topics=1, num_words=30):
    print(x)
