# chatbot 第二课 (july online)
---
## NLP 基础
nltk为基础

---
### nltk
http://www.nltk.org 推荐3.4（很多都是以3.4为基石）<br/> 
python 上注明的自然语言处理库<br/>

- 自带语料库，词性分类库。安装完成后下载语料库 nltk.download()
- 自带分类，分词，（并行能力）等功能<br/>
  nltk.corpus,tokenize(分析),paring(句子shu)，stem
- 强大的社区支持
- 还有n多的简单版wrapper
 
---
### 文本处理流程
raw_text --->tokenize (-->POStag) --->lemma/stemming --->stopwords --->wordlist
#### 分词
- 启发式heuristic(查字典)
- 机器学习、统计方法（基于数据）：HMM、CRF（具体公式）、nn、lstm(训练)
- 英文：tokenize
- 中文：jieba 启发式：cut(cur_all=True/Fasle) viterbi算法，cut_for_search()模式更精确
- 分词之后被分成一个个单词list
##### 难点
- 社交网络语言的tokenize: 正则表达式
- 纷繁复杂的词形：1、inflection(时态)变化 2、derivation(词性)变化

#### 词形归一化 
- stemming 词干提取，就是把不影响词性的inflection的小尾巴去掉<br/>
  nltk.stem.porter lancaster snowballstemmer
- lemmatization 词形归一：把各种类型的词的变形都归为一种形式<br/>
  nltk.stem  wordnetlemmatizer 通过查表的方式还原成原形<br/>
  问题：比如 went ->go ->温斯特 解决：加上pos tag  默认是名词nn<br/>
  part of speech(POS) table:nltk.pos_tag((text)) 先pos 再lemma
#### 停用词
- nltk.cropus stopwords<br/>
  [word for word in wordlist if word not in stopwords.words("english")]<br/>
  去除停用词后得到一个干净的数据列表，后续应用数据进行模型训练
 	
### makefeatures
---
### NLP经典三个案例
#### 情感分析
##### 情感词库
类似于关键词打分机制，稳定但不够高级

- 建一个字典，word :scroe,查看要打分句子分词后的词在字典中的分值进行加和
- 问题：太 naive 1、新词怎么办2、特殊词汇怎么办 3、更深层次的玩意怎么办
##### 配上ML的情感分析
先分词再打标签然后进行机器学习训练然后分类
#### 文本相似度
先向量化
##### 余弦定理

#### 文本分类
- TF term frequency 衡量一个term在文档中出现的频繁程度。<br/>
  TF(t) = (t在文档中的次数)/(文档中所有term的总数)
- IDF inverse document frequency 衡量一个term的重要性。<br/>
  降低常用词的重要性，提升罕见次的重要性。<br/>
  IDF(t) = log(文档总数/含有t的文档的总数)
- TF-IDF = TF*IDF
- 实现 使用nltk.text 中TextCollection：这个类会自动帮忙断句做统计做计算<br/>
 cropus = textcollection([.....]) --- corpus.tf_idf("word","sentence")

---
### 深度学习加持
deep learn is a branch of machine learning based in a set if algorithms that attempt to model high level abstractions in data of multiple linear and non-lineaar transformations
#### autoencoder
自编码器：将信息编码处理，再解码 data-specific 
### word2vec(mikolov,2013)
##### lexical taxonomy 词汇分类：wordNet(miller,1900)
- static 每隔一段时间就要更新
- 只有英语有
##### symbolic representation 符号表示： One-hot(turian et al. 2010)
- 可以表达所有的单词向量
- 单词间的关系不能计算出来
##### distributional similarity based representation 相似度表示
##### fulldocumen：TF-IDF
##### window: co-occurrence matrix + SVD (Bullinaria& levy,2012)
- 共线矩阵，精准到语境本身
#### CBOW
- input为周围词语，输出为当前词

#### skip gram
- 只给中间词猜周围词都是哪些。会让生僻词曝光率更高，
- 对于小规模的训练数据集很好