# #从语料库中引入brown大学的语料库
# from nltk.corpus import brown
#
# a = brown.categories()
# print(a)
# print(len(brown.sents()))
# print(len(brown.words()))




# #　词频统计
# import nltk
# from nltk import FreqDist
# corpus = "this is my sentence this is my life this is the day"
# tokens = nltk.word_tokenize(corpus)
# print(tokens)
# fdist = FreqDist(tokens)
# # print(fdist.items())
# # 选取最常用的单词构建向量空间
# standard_freq_vector = fdist.most_common(50)
# size = len(standard_freq_vector)
# print(standard_freq_vector)
# stand_word_dic = [list(w)[0] for w in standard_freq_vector]
#
# # 对新句子进行编码
# sentence = ["this","is","my","favoriate","pen"]
# size = len(sentence)
# # 县初始化一个向量
# sent_vec = [0]*size
# i = 0
# for word in sentence:
#     try:
#         if word in stand_word_dic:
#             sent_vec[i] = 1
#             i+=1
#     except KeyError:
#         # 不在词汇表中的直接略过
#         i+=1
#         continue
# print(sent_vec)

# nltk实现TF-IDF

from nltk.text import TextCollection
corpus = TextCollection(["this is sentence one","this is sentence two","this is sentence three"])
print(corpus)
print(corpus.tf_idf("this","this is sentence four"))