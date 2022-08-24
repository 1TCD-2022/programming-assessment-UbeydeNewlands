import random
import time

x = 0
letter = ""
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
answer = ["true", 'true', 'false', 'true', 'true', 'false', 'true', 'true', 'false', 'true', 'true', 'false']
chosen_answer = []
#List of answers for each question
random.shuffle(questions)
question = 1
correct = 0
print("Welcome to True False quiz")
while question < 11:
#while is to set maximum questions asked is 10
    if questions[0] == 'Denis Glover wrote the poem The Magpies':
        #checking if this one is the first one in the questions if it is th code starts working
            print("{}. Denis Glover wrote the poem The Magpies".format(question))
            #printing the question
            x = 0
            #this x means what question are we currently in
    #every paragraph has same logic
    elif questions[0] == 'God Save the King was New Zealand’s national anthem up to and during WWII':
            print("{}. God Save the King was New Zealand’s national anthem up to and during".format(question))
            x = 1

    elif questions[0] == 'Kiri Te Kanawa is a Wellington-born opera singer':
            print("{}. Kiri Te Kanawa is a Wellington-born opera singer".format(question))
            x = 2

    elif questions[0] == 'Phar Lap was a New Zealand born horse who won the Melbourne Cup':
            print("{}. Phar Lap was a New Zealand born horse who won the Melbourne Cup".format(question))
            x = 3

    elif questions[0] == 'Queen Victoria was the reigning monarch of England at the time of the Treaty':
            print("{}. Queen Victoria was the reigning monarch of England at the time of the Treaty".format(question))
            x = 4

    elif questions[0] == 'Split Enz are a well-known rock group from Australia who became very famous in New Zealand during the 80s':
            print("{}. Split Enz are a well-known rock group from Australia who became very famous in New Zealand during the 80s".format(question))
            x = 5

    elif questions[0] == "Te Rauparaha is credited with intellectual property rights of Kamate!":
            print("{}. Te Rauparaha is credited with intellectual property rights of Kamate!".format(question))
            x = 6

    elif questions[0] == 'The All Blacks are New Zealand’s top rugby team':
            print("{}. The All Blacks are New Zealand’s top rugby team".format(question))
            x = 7

    elif questions[0] == 'The Treaty of Waitangi was signed in 1901':
            print("{}.The Treaty of Waitangi was signed in 1901".format(question))
            x = 8

    elif questions[0] == 'Thomas Bracken wrote the words to the national anthem God Defend New Zealand.':
            print("{}. Thomas Bracken wrote the words to the national anthem God Defend New Zealand.".format(question))
            x = 9

    elif questions[0] == 'Aotearoa commonly means Land of the Long White Cloud':
            print("{}. Aotearoa commonly means Land of the Long White Cloud".format(question))
            x = 10


    elif questions[0] == 'The Treaty of Waitangi was signed at Parliament':
            print("{}.The Treaty of Waitangi was signed at Parliament".format(question))
            x = 11


    chosen = input('true or false: ')
    #the input is taken here
    chosen = chosen.lower().strip()
    #the answer must be lower and no spce included so we can check what we are looing for
    if chosen == "t":
        chosen = "true"
    elif chosen == "f":
        chosen = "false"
    #if the user is lazy and just writes t or f this ine will realize it
    if chosen in answer:
        #this one is cheking if users input is true false
        if chosen in answer[x]:
            print("correct!")
            correct += 1
            #if the question is working it adds +1 to correct
        else:
            print("False!")
            #if the answer is false
        del questions[0]
        question += 1
    chosen_answer.append(chosen)



time.sleep(1)  
print("you have made {} correct answers overall".format(correct))
time.sleep(1)
while True:
    
    if "false" not in chosen_answer:
        letter = "t"
        print("stop spamming {}".format(letter))
        break

    if "true" not in chosen_answer:
        letter = "f"
        print("stop spamming {}".format(letter))
        break
    
    if correct >= 8 and correct < 10:
        print("academic overall New Zealand knowledge")
        break
    
    elif correct >= 0 and correct <6:
        print("You can do better if you try again harder")
        break
    
    elif correct >= 6 and correct < 7:
        print("nice try")
        break
    
    elif correct == 10:
        print("You know everything you should teach instead")
        break
#a fun ending thing
time.sleep(5)
print("the end")
print(' ________________ ')
print('| MADE BY UBEYDE |')
print('|    12:47p.m    |')
print('|    6/07/2022   |')
print('|________________|')
time.sleep(50)
print("you can go now")
#fun easter egg
