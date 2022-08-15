import random
import time
x = 0
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
            print("{}. Denis Glover wrote the poem The Magpies".format(question))
            x = 0
    #every paragraph has the same logic

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

    elif questions[0] == 'Split Enz are a well-known rock group from Australia who became very famous  in New Zealand during the 80s':
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
    #the input is taken heer
    chosen = chosen.lower().strip()    
    if chosen == "t":
        chosen = "true"
    elif chosen == "f":
        chosen = "false"
        
    if chosen in answers:
        if chosen in answer[x]:
            print("correct!")
            correct += 1
        else:
            print("False!")
        del questions[0]
        #cheking if the input is true or false
        question += 1


time.sleep(1)  
print("you have made {} correct answers overall".format(correct))
time.sleep(1)  
if correct > 5 and correct < 10:
    print("nice overall New Zealand knowledge")
elif correct == 10:
    print("You know everything you should teach instead")
#a fun ending thing
time.sleep(5)
print(' _________________ ')
print('|  MADE BY UBEYDE |')
print('|     12:47 pm    |')
print('|     6/07/202    |') 
print('|_________________|')
#producer
time.sleep(50)
print("you can go now")
time.sleep(2.3)
print("it took my 5 seconds to write this part but you have been waitig for a minute")
time.sleep(10)
print("still here?")
time.sleep(1)
print("take this 10 bucks and go home aerly today")

