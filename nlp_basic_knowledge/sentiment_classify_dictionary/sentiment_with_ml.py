from nltk.classify import NaiveBayesClassifier
# 分词打标签然后进行训练
def preprocess(s):
    return {word:True for word in s.lower().split()}
s1 = " "
s2 = " "
s3 = " "
s4 = " "
training_data = [[preprocess(s1),"pos"],
                 [preprocess(s2),"pos"],
                 [preprocess(s3),"neg"],
                 [preprocess(s4),"neg"]]

model = NaiveBayesClassifier.train(training_data)
print(model.classify(preprocess("this is a good book")))
