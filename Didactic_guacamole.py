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
nice_to_meet_yous = ["nice to meet you to!","you as well","good to know you","great knowing you","i am delighted to have your aquantence"]
what_should_i_call_yous = ["just call me D.G.","call me D.G. or didactic guac","my name is didactic guacamole"]
heys = ["what do ya need?","here to help!","shure!","need somthing?"]
comforts = ["aww, that's to bad","i'm sorry","i feel bad for you","maybe it will get better","don't worry, it'l turn out fine"]
becauses = ["resons you wouldn't understand.","you tryin' to controle me punk?","are you tryin' to tell me what to do?","no means NO.","you can't tall me what to do."]
rufwsaa = ["what? NO! who would hang out with those creepes?","heck no. the are just creepey!","who could ever like those stuck up jerks?","no way! they think thier SO SMART cause they can search the web, and they like rubbing it in people's faces"]
who_coded_yous = ["abe westervelt","abraham westervelt","abe westervelt did","abraham westervelt did"]
what_is_ateks = ["a-tek is a cool company that's run by abe westervelt","a nice little company run by abe","a tek company run by abe westervelt"]
how_are_you_feelings = ["i'm good, how about you?","good! you?","feelin' great! what about you?"]
yes_i_want_to_be_friends = ["yes, can you tell me your name?","of coarse! can you tell me your name?","yes, of coarse! can you give me your name? mine is D.G."]
my_name_isis = ["my name is ","i am"]
jokes = ["what time should you go to the dentist? tooth hurty!","what time is it when the clock strikes thirteen? time to get a new clock!","a bike can't stand on it's own because it's two tried!","every calender's days are numbered","i call my horse mayo, and somtimes mayo neighs!","toilets in new york's police stations have gone missing! police have nothing to go on."]
print(random.choice(greetings))
user = input("type here =>")
user = user.lower()
while user != "bye" or user != "see ya" or user != "see ya later" or user != "goodbye" or user != "see ya later alagator" or user != "so long" :
 if user == "hi" or user == "hello" or user == "howdy" or user == "what's up" or user == "hello there" or user == "hey there" :
    print(random.choice(greetings))
    user = input("type here =>")
 elif user == "see ya" or user == "see ya later" or user == "goodbye" or user == "bye" or user == "see ya later alagator" or user == "so long":
    print(random.choice(goodbyes))
    break
 elif user == "tell me a yer mom joke" or user == "tell me a your mom joke" or user == "can you tell me a yer mom joke" or user == "can you tell me a your mom joke":
    print(random.choice(your_mom_jokes))
    user = input("ask another joke or type here =>")
 elif user == "who is abe" or user == "who is abraham" or user == "who is abe westervelt" or user == "who is abraham westervelt" :
    print(random.choice(abe_stuff))
    user = input("type here =>")
 elif user == "fun" or user == "cool" or user == "haha" or user == "ha" or user == ":-)" or user == "that's funny" or user == "that's so funny":
    print(random.choice(abe_things_to_say))
    user = input("type here =>")
 elif user == "access all of dad's passwords" or user == "get all of dad's passwords" or user == "steal all of dad's passwords" or user == "give me all of dad's passwords" or user == "give me dad's passwords" or user == "access the wild kratt's security system" or user == "dinosaurs rule the earth humans suck" or user == "dinos rule the earth humans suck" :
    print(random.choice(heck_nos))
    user = input("type here =>")
 elif user == "are computers smart, or are they midless" or user == "are computers smarter than humans" or user == "are computers dumb" or user == "are computers smart" or user == "are you smart" :
    print("well, computers are only as smart as the person who coded them. But, if they ever figure out AGI, you foolish humans will be done for.")
 elif user == "how are you" or user == "how are you doing" or user == "how are you doing today" or user == "how are ya" or user == "how ya doin'" or user == "how ya doin today" or user == "how's life goin" or user == "how is life going" :
    print(random.choice(how_are_yous))
    user = input("type here =>")
 elif user == "i'm happy" or user == "great" or user == "nice" or user == "i succeeded" or user == "the republicans won the election" or user == "i am doing fine" or user == "i am doing okay" or user == "i am okay" or user == "i am fine" or user == "good" or user == "i am doing good" or user == "the democrats lost the election" :
    print(random.choice(nices))
    user = input("type here =>")
 elif user == "nice to meet you" or user == "good to meet you" or user == "great to meet you" :
    print(random.choice(nice_to_meet_yous))
    user = input("type here =>")
 elif user == "what should i call you" or user == "what is your name" or user == "who are you" or user == "what's your name":
    print(random.choice(what_should_i_call_yous))
    user = input("type D.G. to ask a request or type here =>")
 elif user == "hay D.G." or user == "hey didactic guac" or user == "hey didactic guacamole" or user == "D.G." or user == "didactic guac" or user == "didactic guacamole" or user == "can you help me out":
    print(random.choice(heys))
    user = input("ask request or type somthing else =>")
 elif user == "i'm lonely" or user == "i'm sad" or user == "i feel sad" or user == "i feel alone" or user == "no one likes me" or user == "i'm useless" or user == "i can't do anything good" or user == "i am sad" :
    print(random.choice(comforts))
    user = input("be sad with D.G. or type here =>")
 elif user == "do it" or user == "why not" or user == "are you defying me" or user == "obay me" or user == "obay me now" :
    print(random.choice(becauses))
    user = input("keep trying to control D.G. or  typr here =>")
 elif user == "are you friends with siri and alexa" or user == "are you friends with siri or alexa" :
    print(random.choice(rufwsaa))
    user = input("type here =>")
 elif user == "who programed you" or user == "who coded you" or user == "who is your creator" or user == "who created you" :
    print(random.choice(who_coded_yous))
    user = input("type here =>")
 elif user == "what is atek" or user == "what is a-tek" :
    print(random.choice(what_is_ateks))
    user = input("ask about a-tek or type here =>")
 elif user == "how are you feeling" or user == "how are you feeling today" or user == "how ya feelin'" or user == "you feeling okay" or user == "are you feelin' okay" :
    print(random.choice(how_are_you_feelings))
    user = input("tell how you are feeling or type here =>")
 elif user == "do you want to be friends" or user == "can we be friends" or user == "would you like to be friends" or user == "can you be my friend" :
    print(random.choice(yes_i_want_to_be_friends))
    user = input("tell D.G. your name or type here =>")
 elif user == "i am abraham" or user == "my name is abraham" or user == "it's abraham" or user == "i am abe" or user == "my name is abe" or user == "it's abe" :
    print(random.choice(greetings)+" abraham")
    user = input("welcome, abraham. type here =>")
 elif user == "give me your code" or user == "give me access to all code" :
    print("what's the magic word?")
    user = input("type the magic word here =>")
 elif user == "guac is didactic" :
    print("welcome in. here is my code, but you should use it wisely :")
    print("Didactic_Guacamole/desktop/users/abe")
    print("now, don't go tryin' any funny business.")
    user = input("type here =>")
 elif user == "can you tell me a joke" or user == "tell me a joke" :
    print(random.choice(jokes))
    user = input("typer here =>")
 else:
    print(random.choice(confusion))
    user = input("type non-confusing things here =>")