import random

def choosesbqquestion(number):
    sbqquestionlist = ['Tell about yourself.',
                       'Do you think that aliens exist?Justify.',
                       'Do you like Marvel movies?Justify',
                       'What is your wierdest thought?',
                       'What is your comment about Multiverse']
    
    randomnumber = random.choice(number)
    print(sbqquestionlist[randomnumber])
    return sbqquestionlist[randomnumber],randomnumber