bot_name="Akio"
bot_type="Personal Chatbot Friend"
bot_chat_name="Akio :"
bot_status=0

def qs(q):
    print()
    if "your" and "name" in q:
        print(bot_chat_name,"My name is",bot_name,".")
    elif "type" and "chatbot" and "you" in q:
        print(bot_chat_name,"I'm your",bot_type,".")
    elif "akio" in q:
        print(bot_chat_name,"Yes .")
        ask()
    elif "thanks" in q:
        print(bot_chat_name,"It's Okay .")
        global bot_status
        bot_status-=1
    else:
        print(bot_chat_name,"Sorry . . .")
        ask()

def satisfy():
    print()
    print(bot_chat_name,"Want to ask more ? ( Yes / No )")
    cs=input("You  : ")
    if cs=='No' or cs=="no":
        print()
        print(bot_chat_name,"I'm Happy that I satisfied You .")
        global bot_status
        bot_status-=1
    else:
        ask()

def intro():
    global bot_status
    bot_status=1
    q=input("Akio : Hi ! Ask a question .\nYou  : ")
    qs(q.lower())

def ask():
    q=input("You  : ")
    qs(q.lower())

intro()
while bot_status==1:
    satisfy()
