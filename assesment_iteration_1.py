import random
questions = ['Denis Glover wrote the poem The Magpies',
    'God Save the King was New Zealand’s national anthem up to and during WWII',
    'Kiri Te Kanawa is a Wellington-born opera singer',
    'Phar Lap was a New Zealand born horse who won the Melbourne Cup',
    'Queen Victoria was the reigning monarch of England at the time of the Treaty',
    'Split Enz are a well-known rock group from Australia who became very famous in New Zealand during the 80s',
    'Te Rauparaha is credited with intellectual property rights of Kamate!',
    'The All Blacks are New Zealand’s top rugby team',
    'The Treaty of Waitangi was signed at Parliament',
    'The Treaty of Waitangi was signed in 1901',
    'Thomas Bracken wrote the words to the national anthem God Defend New Zealand.',
    'Aotearoa commonly means Land of the Long White Cloud']
answers = ['true', 'false'] #List of answers for each question
answer = ["true", 'true', 'false', 'true', 'true', 'false', 'true', 'true', 'false', 'false', 'true', 'true']
selected_answers = [] #Contains selected answers
random.shuffle(questions)
question = 1
correct = 0
print("Welcome to True False quiz")
while question < 11:
#while is to set maximum questions asked is 10
    if questions[0] == 'Denis Glover wrote the poem The Magpies':
    #checking if this paragraph is the question
        print("{}. Denis Glover wrote the poem The Magpies".format(question))
        #printing the question after making this is the question
        chosen = input('True or False: ')
        #input
        chosen = chosen.lower()
        #making the answer lower so it doesnt crush to simple mmistakes
        if chosen in answers:
        #cheking the input
            del questions[0]
            #deleting the question from list so it doen't be asked twice
            question += 1
            #ending information to while loop that one more question is asked
            if chosen in answer[0]:
            #this is the checklist, if this is true than it means the answer is true
                correct += 1
#every paragraph has the same logic
    elif questions[0] == 'God Save the King was New Zealand’s national anthem up to and during WWII':
        print("{}. God Save the King was New Zealand’s national anthem up to and during".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[1]:
                correct += 1
    elif questions[0] == 'Kiri Te Kanawa is a Wellington-born opera singer':
        print("{}. Kiri Te Kanawa is a Wellington-born opera singer".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[2]:
                correct += 1

    elif questions[0] == 'Phar Lap was a New Zealand born horse who won the Melbourne Cup':
        print("{}. Phar Lap was a New Zealand born horse who won the Melbourne Cup".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[3]:
                correct += 1

    elif questions[0] == 'Queen Victoria was the reigning monarch of England at the time of the Treaty':
        print("{}. Queen Victoria was the reigning monarch of England at the time of the Treaty".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[4]:
                correct += 1

    elif questions[0] == 'Split Enz are a well-known rock group from Australia who became very famous in New Zealand during the 80s':
        print("{}. Split Enz are a well-known rock group from Australia who became very famous in New Zealand during the 80s".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[5]:
                correct += 1

    elif questions[0] == 'Te Rauparaha is credited with intellectual property rights of Kamate!':
        print("{}. Te Rauparaha is credited with intellectual property rights of Kamate!".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[6]:
                correct += 1

    elif questions[0] == 'The All Blacks are New Zealand’s top rugby team':
        print("{}. The All Blacks are New Zealand’s top rugby team".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[7]:
                correct += 1

    elif questions[0] == 'The Treaty of Waitangi was signed at Parliament':
        print("{}. The Treaty of Waitangi was signed at Parliament".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[8]:
                correct += 1
    elif questions[0] == 'The Treaty of Waitangi was signed in 1901':
        print("{}.The Treaty of Waitangi was signed in 1901".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[9]:
                correct += 1
    elif questions[0] == 'Thomas Bracken wrote the words to the national anthem God Defend New Zealand.':
        print("{}. Thomas Bracken wrote the words to the national anthem God Defend New Zealand.".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[10]:
                correct += 1
    elif questions[0] == 'Aotearoa commonly means Land of the Long White Cloud':
        print("{}. Aotearoa commonly means Land of the Long White Cloud".format(question))
        chosen = input('True or False: ')
        chosen = chosen.lower()
        if chosen in answers:
            del questions[0]
            question += 1
            if chosen in answer[11]:
                correct += 1
