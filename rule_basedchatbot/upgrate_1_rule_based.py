from nltk import word_tokenize
import random
greeting = ["hola","hello","hi","Hi","hey","hey!"]
question = ["break","holiday","vacation","weekend"]
responses  = ["It was nice! I went to paris","Sadly, I just stayed at home"]

while True:
    rand_greeting = random.choice(greeting)
    rand_respon = random.choice(responses)
    usrinput = input(">>>")
    cleand_input = word_tokenize(usrinput)
    if not set(cleand_input).isdisjoint(greeting):
        print(rand_greeting)
    elif not set(cleand_input).isdisjoint(question):
        print(rand_respon)
    elif usrinput == "bye":
        break
    else:
        print("I don't know what you are saying")