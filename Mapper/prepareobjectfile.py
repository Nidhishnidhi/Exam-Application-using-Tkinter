def prepareobject(lstobj): 
    
    dataDict = {'email': lstobj[0],
                'name': lstobj[1],
                'nationality':lstobj[2],
                'DOB': lstobj[3],
                }
    return dataDict


def prepareobjectlogintime(emailID, loginTime):
    
    loginTimeDict = {
        'email': emailID,
        'loginTime': loginTime
        }
    
    return loginTimeDict

def preparemcq(email,mcqDict):
    
    mcqDict = {'Email':email,
               'McqQuestionAnswer':mcqDict}
    return mcqDict
'''
def preparesbq(email,questions,sbqAnsList):
    print(questions,"\n",sbqAnsList)
    print(questions[0])
    sbqdict = {'Email':email,
               questions[0]:sbqAnsList[0],
               questions[1]:sbqAnsList[1],
               questions[2]:sbqAnsList[2],
               questions[3]:sbqAnsList[3],
               questions[4]:sbqAnsList[4]}
    print(sbqdict)
    return sbqdict'''