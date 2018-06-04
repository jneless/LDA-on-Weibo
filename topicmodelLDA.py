# -*- coding: UTF-8 -*-
import jieba, os
from gensim import corpora, models, similarities
import codecs
import conf

train_set = []

# 读取global表
stopwords = codecs.open('stopWords/GlobalStopWords.txt', 'r', encoding='UTF-8').readlines()

# 去掉末尾\n符号
stopwords = [word.strip('\n') for word in stopwords]

# global表合并local表
stopwords.extend(conf.LocalStopWords)



# 得到output1文件夹属性：文件夹位置，文件夹内全部子文件夹名，文件夹内全部文件名
walk = os.walk('output1')

# 创建一个空链表备用
realWords=list()

for root, dirs, files in walk:

    # 只读模式，打开全部文件
    for name in files:
        f = open(os.path.join(root, name), 'r',encoding='UTF-8')

    # 读取打开的文件
    r1content = f.read()

    # 对r1内容进行分词
    # cut函数返回一个python生成器，必须转化为链表才可下一步操作
    word_list = list(jieba.cut(r1content, cut_all=False)) # false也就是精准模式

    # 对分词结果每一个元素判断是否在stopwords中
    for x in word_list:

        # 如果在（in）则无操作
        if x.strip() in stopwords:
            pass

        # 如果不在（not in）则保留这个词
        if x.strip() not in stopwords:
            realWords.append(x)

    train_set.append(realWords)

texts=train_set

# print(texts)

# 统计一共多少中不同字符，同时对每个字符进行编号
dictionary = corpora.Dictionary(texts)

# 查看指定编号的对应字符
# print(dictionary[3500])

# 详细编号情况
# print(dictionary.token2id)

# 对每一个texts中的词 统计出现的次数， 同时写入到对应的编号中
corpus = [dictionary.doc2bow(text) for text in texts]

# 查看词向量
# print(corpus)


# LDA训练，corpus词向量。在最后查阅id2word，根据词向量训练后得到用户的画像，为词s。在id2word找到词id的实际含义，返回。
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=conf.num_topics, id2word=dictionary)

for x in ldamodel.print_topics(num_topics=conf.num_topics, num_words=conf.num_words):
    print(x)

