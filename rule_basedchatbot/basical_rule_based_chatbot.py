import random
greeting = ["hola","hello","hi","Hi","hey","hey!"]
# random_greeting = random.choice(greeting)
question = ["how are you","how do you do"]
response = ["ok, i am fine","fine thanks, and you ?","very well"]
# random_response = random.choice(response)
while True:
    userinput = input(">>>")
    if userinput in greeting:
        print(random.choice(greeting))
    elif userinput in question:
        print(random.choice(response))
    elif userinput == "bye":
        break
    else:
        print("I don't know what do you say!")

