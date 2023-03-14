import random

def choosequestion(number):
    QuestionsList = ['Who is the father of C language?',
                     'Which of the following is not a valid C variable name?',
                     'Which is valid C expression?',
                     'What is an example of iteration in C?',
                     'What is short int in C programming?']
        
    OptionsList = [['Steve Jobs',' James Gosling','Dennis Ritchie','Rasmus Lerdorf'],
                   ['int number;',' float rate;','int variable_count;','int $main;'],
                   ['int my_num = 100,000;','int my_num = 100000;','int my num = 1000;','int $my_num = 10000;'],
                   ['for','while','dowhile','all the mentioned'],
                   ['The basic data type of C','Qualifier','Short is the qualifier and int is the basic data type','All of the mentioned']]
        
    AnswerList = ['Dennis Ritchie','int $main;','int my_num = 100000;','all the mentioned','Short is the qualifier and int is the basic data type']

    randomnumber = random.choice(number)
    RandomQues = QuestionsList[randomnumber]
    RandomQuesOption = OptionsList[randomnumber]
    RandomQuestionAns = AnswerList[randomnumber]
            
    return RandomQues,RandomQuesOption,RandomQuestionAns,randomnumber