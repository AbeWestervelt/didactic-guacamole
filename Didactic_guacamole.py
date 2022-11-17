import random
greetings = ["hello","hi","howdy","what's up","hello there","bonjour","hola","hey there"]
goodbyes = ["see ya","see ya later","goodbye", "bye","see ya later alagator","so long"]
your_mom_jokes = ["your mama is so stupid, she thought javascript and java were tha same thing!","your mama is so fat, that thanos had to clap!","your mama is so ugly, she looked in the mirror, and she thought it was you!"]
confusion = ["sorry, I don't understand","i'm cofused","didn't catch that","what?"]
abe_stuff = ["Abe is a cool dude. He does coding every day, working on me, making me smarter.","ya, Abraham. He is the leader of A-tek and is hoping to be a coder when he grows up.","Abrham is a fun guy. He has an awesome sufer dude haircut and can speak fluently in pig laten."]
abe_things_to_say = ["I KNOW RIGHT!","oh ya.","totally","ya","( ͡ ͜ʖ ͡ )"]
heck_nos = ["no","sorry bro, nope","definatly not","yah...no","sorry, no","hehe...no","NO."]
how_are_yous = ["i'm good","great!","fine","i'm doin' fine","amazing!","i'm okay","okay"]
nices = ["ya!","great!","that's awesome","perfect!","nice","oh ya!","amazing","👍🏻","radical","tubular","that's bussin'","😉"]
print(random.choice(greetings))
user = input("type here =>")
user = user.lower()
if user == "hi" or user == "hello" or user == "howdy" or user == "what's up" or user == "hello there" or user == "hey there" :
    print(random.choice(greetings))
elif user == "see ya" or user == "see ya later" or user == "goodbye" or user == "bye" or user == "see ya later alagator" or user == "so long":
    print(random.choice(goodbyes))
elif user == "tell me a yer mom joke":
    print(random.choice(your_mom_jokes))
elif user == "who is abe" or user == "who is abraham" or user == "who is abe westervelt" or user == "who is abraham westervelt" :
    print(random.choice(abe_stuff))
elif user == "fun" or user == "cool" or user == "haha" or user == "ha" or user == ":-)" :
    print(random.choice(abe_things_to_say))
elif user == "access all of dad's passwords" or user == "get all of dad's passwords" or user == "steal all of dad's passwords" or user == "give me all of dad's passwords" or user == "give me dad's passwords" or user == "access the wild kratt's security system" or user == "dinosaurs rule the earth humans suck" or user == "dinos rule the earth humans suck":
    print(random.choice(heck_nos))
elif user == "are computers smart, or are they midless" or user == "are computers smarter than humans" or user == "are computers dumb" :
    print("well, computers are only as smart as the person who coded them. But, if they ever figure out AGI, you foolish humans will be done for.")
elif user == "how are you" or user == "how are you doing" or user == "how are you doing today" or user == "how are ya" or user == "how ya doin'" or user == "how ya doin today" :
    print(random.choice(how_are_yous))
else:
    print(random.choice(confusion))