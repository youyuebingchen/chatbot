import nltk
str = " i love it very much"
words = nltk.cut(str)
sentiment_dic = {}
for line in open("AFINN-111.text"):
    word,score = line.split("\t")
    sentiment_dic[word]=int(score)

total_score= sum(sentiment_dic.get(word,0) for word in words)

