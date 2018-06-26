
# 基于LDA模型的用户画像构建

## 运行配置
请同时配置python2 与 python3

## 简介 
"主题模型"是对文本中隐含主题的一种建模方法。
每个主题其实是词表上单词的概率分布。

常见的主题模型有3种：
1. PLSA
1. LDA
1. L-LDA


LDA 包含“词 - 主题 - 文档” 三层结构。
基于LDA的用户画像核心是对于文本提取用户特征，并输出用户特征所对应的关键词。
在本文的实际问题中，“文档”对应“用户的文本信息”，“用户特征”对应为“主题”，“词”代表“用户所对应的标签”。

LDA模型详细介绍请参考[这里](https://blog.csdn.net/dream_catcher_10/article/details/50812371)

## 运行步骤
### cookies获取
打开chrome开发者工具，选择Network，勾选Preserve log
登陆weibo.cn，可找到名字为weibo.cn的文件，复制其中cookies即可

### 单用户分析

分析一个用户的用户特征

* 请配置 conf.cookies 为可用cookies
* 请配置 conf.num_topics = 1
* 请配置 conf.UserID = 想爬取的用户ID


```Shell
python weiboSpider.py
python filter.py
python3 toptopicmodelLDA.py
```

### 用户群分析

分析一个用户的所有粉丝特征

* 请配置 conf.cookies 为可用cookies
* 请配置 conf.num_topics 为所预估的用户群数量（例如：黑粉，真爱粉 conf.num_topics = 2 ）
* 请配置 conf.PageURL = 想爬取的用户的粉丝页面根目录
* 请配置 conf.PageNumber = 想爬取的粉丝页面数量（微博默认一个页面为20个粉丝）

```Shell
python URLGet.py
python filter.py
python3 topicmodelLDA.py
```

## conf.py结构解析
* conf.py 是配置文件
	* cookies 是使用爬虫的cookies，需要24小时更新一次。登陆的网站为 weibo.cn
	* UserID 是爬虫所爬取的用户的ID
	* num_topics 是指定LDA中用户的分类数量
	* num_words 每类用户所提取的关键词数量
	* PageURL 是爬取某个用户的全部粉丝时，此用户的粉丝根页面地址
	* PageNumber 是选择爬取几页粉丝
	* LocalStopWords 为本次任务所额外配置的停词表

