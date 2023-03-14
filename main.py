from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import random
from Config import connectionfile
from Service import createaccountfile, insertdetailfile, insertmediafile, logintoaccountfile, retrieve,choosesbqquestionfile
from Service import logintimestorefile, retrievedatafile, captchafile, choosequestionfile, storefile
from Mapper import prepareobjectfile
import string
from PIL import Image, ImageTk
from firebase import firebase
from datetime import datetime
from fpdf import FPDF
from PIL import Image # Notice the 'from PIL' at the start of the line

number = [0,1,2,3,4]
count = 0
total = 0
mcqDict={}
sbqDict={}
sbqnumber=[0,1,2,3,4]
questioncount = 0
questions=[]
printing_list = []

#nidhi@j.com:onMp9Culp

'''*****************************************************GENERATE RESULT************************************************************'''
def FinalResult():
    def checksbq():
             if sbqpercent != None:
                 if sbqpercent < 50 :
                     return "cleared"
                 else:
                     return "not cleared"
             else:
                 return "not attended"
         
    def printpdf():
                 
        
        pdf = FPDF()
     
        pdf.add_page()
       
        pdf.set_font("Arial", size = 15)
        
        pdf.cell(200, 10, txt = "Login time :"+str(printing_list[6]),align = 'R')
        
        pdf.cell(200, 30, txt = "Email :" +printing_list[0],ln = 1, align = 'C')
       
        pdf.cell(200, 10, txt = "Name :"+printing_list[1],ln = 2, align = 'C')
        
        pdf.cell(200, 10, txt = "MCQMarks :"+str(printing_list[2]),ln = 3, align = 'C')
        
        pdf.cell(200,10,txt = "Stage 1:"+printing_list[3],ln = 4, align = 'C')
        
        pdf.cell(200, 10, txt = "SBQPlagerism :"+str(printing_list[4]),ln = 5, align = 'C')
          
        pdf.cell(200,10,txt = "Stage 2:"+str(printing_list[5]),ln = 6, align = "C" )
        
        pdf.cell(10, 140, txt = "Printing time :"+str(printing_list[7]),ln = 7, align = 'L')
        # save the pdf with name .pdf
        pdf.output(retrieved_data['name']+".pdf") 
    
    
    
    FinalResultFrame.place(x=330, y=150, height=500, width=500)
    
    mcqstatus,mcqdata=retrieve.retrievemcqdata(loginemailentry.get())
    
    sbqstatus,sbqpercent = retrieve.retrievesbqdata(loginemailentry.get())
    
    accountstatus,retrieved_data = retrievedatafile.retrievedata(loginemailentry.get())
    
    loginstatus,logintime = retrievedatafile.retrievetime(loginemailentry.get())
    
    StudentEmailDis.configure(text = loginemailentry.get())
    
    StudentNameDis.configure(text=retrieved_data['name'])
    try:
        StudentLoginDis.configure(text=logintime['loginTime'])
        
    except:
        StudentLoginDis.configure(text="NIL")
        
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    c = checksbq()
    
    printing_list = [loginemailentry.get(),retrieved_data['name'],mcqdata['total'],'cleared' if mcqdata['total'] > 3 else 'not cleared',c,sbqpercent,logintime['loginTime'],current_time]
    print(printing_list)
    
    if(mcqstatus):
        StudentMCQAttemptDis.configure(text='ATTEMPTED')
        StudentMCQMarksScoredDis.configure(text=mcqdata['total'])
        
        if(mcqdata['total'] > 3):
            StudentMCQStage1Dis.configure(text = "CLEARED")
            
        else:
            StudentMCQStage1Dis.configure(text = "NIL")
            
    else:
        StudentMCQAttemptDis.configure(text="NOT ATTEMPTED")
        
        
            
    if(sbqstatus):
        StudentSBQAttemptDis.configure(text="Attempted")
        StudentSBQMarksScoredDis.configure(text=str(sbqpercent)+"%")
        
        if(sbqpercent < 50):
            StudentSBQStage2Dis.configure(text="CLEARED")
            
        else:
            StudentSBQStage2Dis.configure(text="NIL")
    else:
        StudentSBQAttemptDis.configure(text="NOT ATTEMPTED")
        
    printButton.configure(command=printpdf)
   
            







'''****************************************************Update Frame Function****************************************************'''


def updateframefunction(email):
    s, retrieved_data = retrievedatafile.retrievedata(email)
    
    dashframe.place(x=350, y=50, height=750, width=850)
    dashboardlabel.configure(text = "DashBoard")
    '''
    try:
        img = Image.open(loginemailentry.get()+".png")
        img = img.resize((150, 150))
        
    except:
        img = Image.open(loginemailentry.get()+".jpg")
        img = img.resize((150,150))'''
    
    if(Image.open(loginemailentry.get()+".png")):  
        img = Image.open(loginemailentry.get()+".png")
        img = img.resize((150,150))
        
    elif(Image.open(loginemailentry.get()+".jpg")):
        img = Image.open(loginemailentry.get()+".jpg")
        img = img.resize((150,150))
       
    else:
        pass
    
    #img.show()
        
    #create a label
    img_label = Label(updateframe, relief = SUNKEN)
    default_photo = ImageTk.PhotoImage(img)
    img_label.configure(image = default_photo)
    
    img_label1 = Label(updateframe,  image = default_photo)
    img_label.place(x = 80, y = 10)
    img_label1.place(x = 80, y = 10)
    '''
    image = Image.open("C:\\Users\\nidhi\\OneDrive\\Desktop\\python application\\Project 1\\modifiedimage.png")
    resize_img = image.resize((150,150))
    img = ImageTk.PhotoImage(resize_img)
    img_label.configure(image = img)
    img_label.place(x = 80,y = 10)'''


    updateframe.place(x=20, y=150, height=500, width=300)
    examframe.place(x=330, y=150, height=500, width=500)

    updateemaillabel = Label(updateframe, text="Emailid",bg="light blue", fg="blue")
    updateemaillabel.place(x=10, y=170)

    updateemaillabel1.configure(text=retrieved_data['email'])

    updatenamelabel = Label(updateframe, text="Name",bg="light blue", fg="blue")
    updatenamelabel.place(x=10, y=200)

    updatenamelabel1.configure(text=retrieved_data['name'])

    updatenationalitylabel = Label(updateframe, text="Nationality", bg="light blue", fg="blue")
    updatenationalitylabel.place(x=10, y=230)

    updatenationalitylabel1.configure(text=retrieved_data['nationality'])

    updatedoblabel = Label(updateframe, text="Date Of Birth", bg="light blue", fg="blue")
    updatedoblabel.place(x=10, y=260)

    updatedoblabel1.configure(text=retrieved_data['DOB'])

    updatebutton = Button(updateframe, text="Update", bg="dark green", fg="black", command=lambda:updatefunction(retrieved_data))
    updatebutton.place(x=100, y=400)


'''**************************************************************UPDATE FUNCTION******************************************************************'''


def updatefunction(data):
    def putdata():
        email = data['email']
        uname = updatedname.get()
        unationality = nationality.get()
        udob = dob.get()

        status, value = connectionfile.connection()
        database_obj = value.database()
        udata = database_obj.child('Account/PersonalData').get()

        flag = 0
        for each_data in udata:
            db_emailid = each_data.val()['email']
            if db_emailid == email:
                flag = 1
                database_obj.child
                # update the name of the individual
                database_obj.child("Account/PersonalData").child(each_data.key()).update({'name': uname,
                                                                                          'nationality': unationality,
                                                                                          'DOB': udob})
        if flag == 1:
            messagebox.showinfo('Updated', 'Information is updated')
            s, retrieved_data = retrievedatafile.retrievedata(email)
            personaldataframe.place_forget()
            updateframefunction(email)

        else:
            messagebox.showwarning('warning', 'Information is not updated')

    def validatesecurityanswer():
        ans = securityanswer.get()
        ques = randomquestion
        if(ans != ""):
            for i in range(len(questions)):
                if(questions[i] == ques):
                    if(ans == data[questions[i]]):
                        messagebox.showinfo('Success', 'Security answer is correct!!!')
                        ubutton['state'] = NORMAL
                    else:
                        messagebox.showwarning('warning', 'Invalid security answer')

    updateframe.place_forget()
    examframe.place_forget()
    FinalResultFrame.place_forget()

    '''**********************************************UPDATE FRAME************************************************'''

    personaldataframe = Frame(dashframe, bg='light blue', relief=SUNKEN, bd=5)
    personaldataframe.place(x=190, y=100, height=500, width=500)
    
    dashboardlabel.configure(text = "Update data")
        
    updatenamelabel = Label(personaldataframe, text="Name", bg="light blue", fg="blue")
    updatenamelabel.place(x=10, y=10)

    updatedname = Entry(personaldataframe)
    updatedname.insert(0, data['name'])
    updatedname.place(x=10, y=40)

    updatenationalitylabel = Label(personaldataframe, text="Nationality", bg="light blue", fg="blue")
    updatenationalitylabel.place(x=10, y=80)

    nationality = ttk.Combobox(personaldataframe)
    nationality['value'] = ['Indian', 'America',
                            'Australia', 'China', 'Russia', 'German', 'France']
    nationality.current(0)
    nationality.place(x=10, y=110)

    updatedoblabel = Label(personaldataframe, text="DOB",
                           bg="light blue", fg="blue")
    updatedoblabel.place(x=10, y=150)

    dob = DateEntry(personaldataframe)
    dob.place(x=10, y=180)

    ubutton = Button(personaldataframe, text="Update",
                     bg="dark green", fg="black", command=putdata)
    ubutton.place(x=120, y=370)

    ubutton['state'] = DISABLED

    updatesecurityanslabel = Label(
        personaldataframe, text="Enter Security answer", bg="light blue", fg="blue")
    updatesecurityanslabel.place(x=10, y=220)

    questions = ['What is your pet name', 'What is your favourite food',
                 'What is your nick name', 'What is your favourite color', 'What is your role model']
    randnumber = random.randint(0, 4)
    randomquestion = questions[randnumber]

    securityquestions = Label(personaldataframe, bg="light blue", fg="blue")
    securityquestions.configure(text=questions[randnumber])
    securityquestions.place(x=10, y=250)

    securityanswer = Entry(personaldataframe)
    securityanswer.place(x=10, y=280)

    validate = Button(personaldataframe, text='validate',bg="dark green", fg="black", command=validatesecurityanswer)
    validate.place(x=200, y=280)


'''**************************************************LOGIN**************************************************'''

status = 0
mcqdata=[]
def logintoaccount():
    global status,mcqdata,total
    email = loginemailentry.get()
    password = loginpasswordentry.get()

    if (logintoaccountfile.logintoaccount(email, password)):
        messagebox.showinfo("Success", "Login Successful")
        if(logintimestorefile.logintimestore(email)):
            print("Login time is stored Successfully")
        else:
            print("Login time is not stored")

        logframe.place_forget()
        updateframefunction(email)

    else:
        messagebox.showwarning('warning', 'Invalid Credentials')
        
    mcqstatus,mcqdata=retrieve.retrievemcqdata(email)
    print(mcqstatus,mcqdata)
    
    
    if(mcqstatus):
        mcqstartbutton['state']=DISABLED
        displaymarkslabel.configure(text=mcqdata['total'])
        if(mcqdata['total'] > 3):
            sbqstartbutton['state']=NORMAL
            
        else:
            generateresultbutton['state'] = NORMAL
            
    else:
       pass
   
    try:
        sbqstatus,sbqpercent = retrieve.retrievesbqdata(email)
        
        if(sbqstatus):
            sbqstartbutton['state'] = DISABLED
            displayplagiarismcent.configure(text = sbqpercent)
            generateresultbutton['state'] = NORMAL
            
    except:
        pass
    
    
'''************************************************SECURITY FUNCTION************************************************'''


def securityFunction():
    def securityadderfunction():
        global securityQADict
        securityQADict = {"What is your pet name": questionentry1.get(),
                          "What is your favourite food": questionentry2.get(),
                          "What is your nick name": questionentry3.get(),
                          "What is your favourite color": questionentry4.get(),
                          "What is your role model": questionentry5.get()}
        q1 = questionentry1.get()
        q2 = questionentry2.get()
        q3 = questionentry3.get()
        q4 = questionentry4.get()
        q5 = questionentry5.get()

        if(q1 != "" and q2 != "" and q3 != "" and q4 != "" and q5 != ""):
            secframe.place_forget()
            secbutton['state'] = DISABLED
            subbutton['state'] = NORMAL

        else:
            messagebox.showwarning(
                "warning", "security questions are incomplete")

    emailid = emailentry.get()
    if(emailid == ""):
        messagebox.showwarning('warning', 'Emailid is not entered')

    else:

        secframe = Frame(w, bg="lightblue")
        secframe.place(x=400, y=50, height=700, width=700)

        questionlabel1 = Label(
            secframe, text="What is your pet name", bg="light blue", fg="blue", font=25)
        questionlabel1.place(x=10, y=10)

        questionentry1 = Entry(secframe)
        questionentry1.place(x=10, y=50)

        questionlabel2 = Label(
            secframe, text="What is your favourite food", bg="light blue", fg="blue", font=25)
        questionlabel2.place(x=10, y=100)

        questionentry2 = Entry(secframe)
        questionentry2.place(x=10, y=140)

        questionlabel3 = Label(
            secframe, text="What is your nick name", bg="light blue", fg="blue", font=25)
        questionlabel3.place(x=10, y=190)

        questionentry3 = Entry(secframe)
        questionentry3.place(x=10, y=230)

        questionlabel4 = Label(
            secframe, text="What is your favourite color", bg="light blue", fg="blue", font=25)
        questionlabel4.place(x=10, y=280)

        questionentry4 = Entry(secframe)
        questionentry4.place(x=10, y=320)

        questionlabel5 = Label(
            secframe, text="Who is your role model", bg="light blue", fg="blue", font=25)
        questionlabel5.place(x=10, y=370)

        questionentry5 = Entry(secframe)
        questionentry5.place(x=10, y=410)

        submitbutton = Button(secframe, text="submit", bg="dark green",
                              fg="black", command=securityadderfunction)
        submitbutton.place(x=100, y=470)


'''***************************************************SUBMITDATA FUNCTION**************************************************'''


def submitdatafunction():

    passwordlist = list(string.ascii_letters + string.digits + "!@#$%^&*")
    emailid = emailentry.get()
    name = nameentry.get()
    nationality = nationalitycombobox.get()
    dob = dobentry.get()

    passwordgenerated = ""
    while(len(passwordgenerated) < 9):
        passwordgenerated += random.choice(passwordlist)

    print(passwordgenerated)
    if(createaccountfile.createaccount(emailid, passwordgenerated)):
        messagebox.showinfo('success', 'Account created successfully')
        lstobj = [emailid, name, nationality, dob]
        preparedobj = prepareobjectfile.prepareobject(lstobj)
        preparedobj.update(securityQADict)
        sframe.place_forget()
        logframe.place(x=400, y=50, height=750, width=750)

        if(insertdetailfile.insertdetail(preparedobj)):
            print("Data sent to real time database")

            if(insertmediafile.insertmedia(imagePath.get())):
                print("Image inserted successfully")

            else:
                print("Image was not inserted")

        else:
            print("Data not sent to Realtime Database")

    else:
        messagebox.showerror('error', 'accound not created')


'''**************************************************UPLOAD FUNCTION**************************************************'''


def uploadFunction():
    '''
    imgselected = askopenfilename(initialdir="",
                                  filetype=(('imgFile', '*jpg'),
                                            ('allfile', '*.*')),
                                  title="choose a file")
    imagePath.set(imgselected)
    #save he image in the server ( Local System)
    img=Image.open(imgselected)
    img.save("modified.png")
    imgbutton['state'] = DISABLED
    secbutton['state'] = NORMAL
    '''
    r_status, value = connectionfile.connection()
    if(r_status):
        email = emailentry.get()
        img_selected = askopenfilename(initialdir = "",
                                       filetype = (('imgfile','*.jpg'), ('allfile', '*.*')),
                                       title = "choose the image") 
            
        
        imgbutton['state'] = DISABLED
        
        imagename = email+".png"
        print(imagename)
        
        img = Image.new("RGB", (200, 30), "#ddd")
        img.save(imagename)
        '''
        img = Image.open(img_selected)
        img.save("media/"+email+".png")'''
        
        imagePath.set(img_selected)
        #create an storage object
        store_obj = value.storage()
        
        #inserting the image into database
        store_obj.child(img_selected).put(img_selected)
        print("Image inserted")
        imgbutton['state'] = DISABLED
        secbutton['state'] = NORMAL
    else:
        print("connection to storage failed")

'''********************************************************SIGNUPFRAME*****************************************************'''


def opensignupframe():
    logframe.place_forget()
    sframe.place(x=400, y=50, height=750, width=750)


'''********************************************************CAPTCHA REFRESH**************************************************'''


def captcharefresh(rhs, lhs, op):
    exp = captchafile.refresh(rhs, lhs, op)
    captchashow.configure(text=exp)


'''*******************************************************CAPTCHA VALIDATE***************************************************'''


def captchavalidate(rhs, lhs, op, e1):
    rhsvalue = rhs.get()
    lhsvalue = lhs.get()
    operator = op.get()

    result = 9999

    if(operator == "+"):
        result = int(lhsvalue) + int(rhsvalue)

    elif(operator == "-"):
        result = int(lhsvalue) - int(rhsvalue)

    else:
        result = int(lhsvalue) * int(rhsvalue)

    actualresult = e1
    if(int(result) != int(actualresult)):
        messagebox.showwarning('warning', 'Invalid Captcha')
    else:
        loginbutton['state'] = NORMAL


'''******************************************************MCQEXAM FUNCTION************************************************************'''

def putmcqdata(randquestion,correctanswer,answer):
    
    global count,mcqDict,total
    print(correctanswer,answer)
    
    savebutton['state']=DISABLED
    nextbutton['state']=NORMAL
    
    if(answer == correctanswer):
        total+=1
        print(total)
    
    mcqDict[randquestion]=answer
    count += 1
   
    if count == 5:
        mcqDict['total']=total
        storefile.mcqstore(loginemailentry.get(),mcqDict)
        MCQQuestionsFrame.place_forget()
        dashframe.place(x=350, y=50, height=750, width=850)
        displaymarkslabel.configure(text=total)
        mcqstartbutton['state']=DISABLED
        
        if(total > 3):
            sbqstartbutton['state']=NORMAL
            
        else:
            generateresultbutton['state'] = NORMAL
            
        

        
def mcqdisplayandstore():
     global number,count,questionlabellist   
       
     ExamInstructionFrame.place_forget()

     MCQQuestionsFrame.place(x=350, y=50, height=750, width=850)
     
     #MCQQuestionDisplayFrame.place(x=1250,y=50,height = 500,width = 100)
        
     randquestion, randoption, randans, randomnumber = choosequestionfile.choosequestion(number)
     QuestionsLabel.configure(text=randquestion)
     #print(randomnumber)
     number.remove(randomnumber)
     print(number)
     
     AnsOption1.configure(text=randoption[0],value=randoption[0])
     AnsOption2.configure(text=randoption[1],value=randoption[1])
     AnsOption3.configure(text=randoption[2],value=randoption[2])
     AnsOption4.configure(text=randoption[3],value=randoption[3])
     
     savebutton.configure(command =lambda:putmcqdata(randquestion,randans,answer.get()))
     savebutton['state']=NORMAL
     if(count == 4):
         savebutton['state']=DISABLED
     savebutton.place(x=400,y=500)
     
     nextbutton.configure(text="Next",command = mcqdisplayandstore)
     nextbutton.place(x=400,y=540)
     
     nextbutton['state']=DISABLED
     
     if(number == []):
         nextbutton.configure(text="Finish",command=lambda:putmcqdata(randquestion,randans,answer.get()))
         nextbutton['state']=NORMAL
         
def mcqexamfunction():
          
    dashframe.place_forget()

    w.attributes("-fullscreen", True)
    startbutton.configure(command=mcqdisplayandstore)
    ExamInstructionFrame.place(x=350, y=50, height=750, width=850)
    '''
    x1 = 10
    y1 = 0
    for i in range(questionlabellist):
        questionlabellist[i] = Label(MCQQuestionDisplayFrame,bg = "red")
        y1 += 1'''
    
    
'''*******************************************************************SBQ EXAM FUNCTION*******************************************'''
sbqcount = 0
objfirebase = {}
sbqAnsList = [None,None,None,None,None]

def databaseconnection():
    
    try:
        objfirebase = firebase.FirebaseApplication("https://firstapplication-e50c5-default-rtdb.firebaseio.com")
        
        return objfirebase
    
    except:

        return "null"

def sbqstore(objfirebase,plagiarism):
    global sbqDict,SBQQuesAndAns
    email = loginemailentry.get()
    
    sbqAnsList.insert(0,email)
    sbqAnsList.insert(6,plagiarism)
    print(sbqAnsList,sbqAnsList[6])
    
    try: 
        print("inside try")
        objfirebase.post('Account/EXAM/SBQ',sbqAnsList)
        print("after posting")
        return True
    
    except:
        print("false")
        return False
     

def postsbqdata():
    global objfirebase
    objfirebase = databaseconnection()
    print(objfirebase)
    
    sbqstatus,sbqpercent = retrieve.beforeuploading(loginemailentry.get(),sbqAnsList)
    
    if(sbqstore(objfirebase,sbqpercent)):
        SBQQuestionsFrame.place_forget()
        dashframe.place(x=350, y=50, height=750, width=850)
        sbqstartbutton['state'] =  DISABLED
        
    if(sbqstatus):
        sbqstartbutton['state'] = DISABLED
        displayplagiarismcent.configure(text = sbqpercent)
        generateresultbutton['state'] = NORMAL
        
        
    

def savesbqdata(questions):
    global sbqcount
    sbqAnsList[sbqcount] = SBQAnswerText.get("1.0","end-1c")
    SBQsavebutton['state']=DISABLED
    SBQnextbutton['state']=NORMAL
    print(SBQAnswerText.get("1.0","end-1c"),sbqDict)
    sbqcount += 1
    if(sbqcount == 5):
        SBQnextbutton['state']=DISABLED
        SBQFinishButton.configure(text="finish",command=postsbqdata)
        SBQFinishButton.place(x=400,y=660)
   

def displayquestions(questions):
    global sbqcount,sbqDict
    SBQAnswerText.delete('1.0','end')
    
    SBQQuestionLabel.configure(text=questions[sbqcount])
        
    SBQAnswerText.place(x=30,y=120)
    
    SBQsavebutton.place(x=400,y=600)
    SBQnextbutton.place(x=400,y=630)
    
    SBQsavebutton['state']=NORMAL
    SBQnextbutton['state']=DISABLED
   
    SBQsavebutton.configure(text="save",command=lambda:savesbqdata(questions)) 
    
    SBQnextbutton.configure(text="next",command=lambda:displayquestions(questions))
    
    

def sbqdisplayandstore():
    global questions
    ExamInstructionFrame.place_forget()

    SBQQuestionsFrame.place(x=350, y=50, height=750, width=850)
    
    questions=['What is your weird thought','Is timetravel possible','If you had superpower which one you like it to be',
               'Do aliens exist.Justify','Do you like Marvel Movies?']
    
    displayquestions(questions)
        
    
    
def sbqexamfunction():
    dashframe.place_forget()

    w.attributes("-fullscreen", True)
    startbutton.configure(command=sbqdisplayandstore)
    ExamInstructionFrame.place(x=350, y=50, height=750, width=850)

        
    


'''*****************************************************************WINDOW***************************************************************'''
w = Tk()
w.geometry('1250x1250')
w.state("zoomed")
w.resizable(0, 0)
w.configure(background="dark blue")
w.title("Project1")

'''*******************************************************SIGNUP FRAME*****************************************************************'''

sframe = Frame(w, bg="light blue", relief=SUNKEN)
sframe.place(x=400, y=50, height=750, width=750)

emaillabel = Label(sframe, text="Email id",bg="light blue", fg="blue", font=30)
emaillabel.place(x=20, y=50)

emailentry = Entry(sframe)
emailentry.place(x=20, y=90, width=200)

namelabel = Label(sframe, text="Name", bg="light blue", fg="blue", font=30)
namelabel.place(x=20, y=140)

nameentry = Entry(sframe)
nameentry.place(x=20, y=180, width=200)

nationalitylabel = Label(sframe, text="Nationality",bg="light blue", fg="blue", font=30)
nationalitylabel.place(x=20, y=230)

nationalitycombobox = ttk.Combobox(sframe)
nationalitycombobox['value'] = ['India', 'America','Australia', 'China', 'Russia', 'German', 'France']
nationalitycombobox.current(0)
nationalitycombobox.place(x=20, y=270, width=200)

doblabel = Label(sframe, text="D.O.B", bg="light blue", fg="blue", font=30)
doblabel.place(x=20, y=310)

dobentry = DateEntry(sframe)
dobentry.place(x=20, y=350, width=200)

imglabel = Label(sframe, text="Upload image",bg="light blue", fg="blue", font=30)
imglabel.place(x=20, y=390)

imgbutton = Button(sframe, text="Upload", bg="dark green",fg="black", command=uploadFunction)
imgbutton.place(x=60, y=420)

secbutton = Button(sframe, text="Security Question?",bg="light blue", fg='blue', command=securityFunction)
secbutton.place(x=20, y=490)
secbutton['state'] = DISABLED

subbutton = Button(sframe, text="submit", bg="dark green",fg="black", command=submitdatafunction)
subbutton.place(x=320, y=570)
subbutton['state'] = DISABLED

sframe.place_forget()


'''******************************************************LOGIN FRAME****************************************************************'''

logframe = Frame(w, bg="light blue", relief=SUNKEN)
logframe.place(x=400, y=50, height=750, width=750)

loginemaillabel = Label(logframe, text="Email id",
                        bg="light blue", fg="blue", font=30)
loginemaillabel.place(x=20, y=50)

loginemailentry = Entry(logframe)
loginemailentry.place(x=20, y=90, width=200)

loginpasswordlabel = Label(logframe, text="Password",
                           bg="light blue", fg="blue", font=30)
loginpasswordlabel.place(x=20, y=140)

loginpasswordentry = Entry(logframe)
loginpasswordentry.place(x=20, y=180, width=200)

captcha = Label(logframe, text="Captcha")
captcha.place(x=20, y=230)

captchashow = Label(logframe)
rhs, lhs, op, expression = captchafile.captcha()
captchashow.configure(text=expression)
captchashow.place(x=20, y=270)

refreshbutton = Button(logframe, text="refresh",command=lambda: captcharefresh(rhs, lhs, op))
refreshbutton.place(x=60, y=270)

captchaentry = Entry(logframe)
captchaentry.place(x=20, y=310)

validate = Button(logframe, text="validate", command=lambda: captchavalidate(rhs, lhs, op, captchaentry.get()))
validate.place(x=20, y=350)


loginbutton = Button(logframe, text="Login", bg="dark green",fg="black", command=logintoaccount)
loginbutton.place(x=60, y=400)
loginbutton['state'] = DISABLED

newuserbutton = Button(logframe, text="New User?",bg="light blue", fg="blue", command=opensignupframe)
newuserbutton.place(x=60, y=440)


'''******************************************************DASHBOARD FRAME**************************************************************'''

dashframe = Frame(w, bg="dark blue", relief=RAISED, bd=5)


dashboardlabel = Label(dashframe, bg="dark blue", fg="light blue")
dashboardlabel.configure(text="DashBoard", font=('fira-code',40))
dashboardlabel.place(x=330, y=20)


'''******************************************************UPDATE FRAME****************************************************************'''

updateframe = Frame(dashframe, bg='light blue', relief=SUNKEN, bd=5)

imagePath = StringVar()
'''
uphoto = Label(updateframe)
uphotoimg = Image.open("modifiedimage.png")
height_uphotoimg, width_uphotoimg = uphotoimg.size

uphotoimg = uphotoimg.resize((150, 150))
height_uphotoimg, width_uphotoimg = uphotoimg.size

uphotoimg = ImageTk.PhotoImage(uphotoimg)
uphoto.configure(image=uphotoimg)
uphoto.place(x=80, y=10, height=height_uphotoimg, width=width_uphotoimg)
'''
updateemaillabel1 = Label(updateframe, bg="light blue")
updateemaillabel1.place(x=100, y=170)

updatenamelabel1 = Label(updateframe, bg="light blue")
updatenamelabel1.place(x=100, y=200)

updatenationalitylabel1 = Label(updateframe, bg="light blue")
updatenationalitylabel1.place(x=100, y=230)

updatedoblabel1 = Label(updateframe, bg="light blue")
updatedoblabel1.place(x=100, y=260)

'''*****************************************************EXAM FRAME**************************************************************'''

examframe = Frame(dashframe, bg="light blue", relief=SUNKEN, bd=5)
examframe.place(x=330, y=150, height=500, width=500)

generateresultbutton = Button(examframe, text="Generate Result", bg="dark green", fg="black", font=25,command=FinalResult)
generateresultbutton.place(x=150, y=400)
    

'''******************************************************MCQ FRAME******************************************************************'''
mcqframe = Frame(examframe, bg="#65BDE9", relief=FLAT, bd=5)
mcqframe.place(x=25, y=40, height=300, width=200)

mcqlabel = Label(mcqframe, text="MCQ", bg="#65BDE9", fg="blue", font=50)
mcqlabel.place(x=60, y=50)

mcqstartbutton = Button(mcqframe, text="Start", bg="dark green",fg="black", font=30, command=mcqexamfunction)
mcqstartbutton.place(x=60, y=130, height=40, width=50)


totalmarkslabel = Label(mcqframe, text="Total Marks",bg="#65BDE9", fg="blue", font=50)
totalmarkslabel.place(x=40, y=200)

displaymarkslabel = Label(mcqframe, bg="#65bde9", fg="blue", font=30)
displaymarkslabel.configure(text="0")
displaymarkslabel.place(x=70, y=230)

 
'''***************************************************************SBQ FRAME***********************************************************'''

sbqframe = Frame(examframe, bg="#65bde9", relief=FLAT, bd=5)
sbqframe.place(x=250, y=40, height=300, width=200)

sbqlabel = Label(sbqframe, text="SBQ", bg="#65bde9", fg="blue", font=50)
sbqlabel.place(x=60, y=50)

sbqstartbutton = Button(sbqframe, text="Start",bg="dark green", fg="black", font=30,command=sbqexamfunction)
sbqstartbutton.place(x=60, y=130, height=40, width=50)
sbqstartbutton['state'] = DISABLED

plagiarismlabel = Label(sbqframe, text="Plagiarism",bg="#65bde9", fg="blue", font=50)
plagiarismlabel.place(x=40, y=200)

displayplagiarismcent = Label(sbqframe,bg="#65bde9",fg="blue", font=30)
displayplagiarismcent.configure(text="0%")
displayplagiarismcent.place(x=70, y=230)

'''************************************************************EXAM INSTRUCTION FRAME*************************************************************'''

ExamInstructionFrame = Frame(w, bg="light blue")

instructionlabel = Label(ExamInstructionFrame, text="INSTRUCTIONS",bg="light blue", fg="blue", font=('fira-code', 30))
instructionlabel.place(x=300, y=100)

firstinstruction = Label(ExamInstructionFrame, text="1.There will be 5 questions",bg="light blue", fg="blue", font=('fira-code', 15))
firstinstruction.place(x=10, y=230)

secondinstruction = Label(ExamInstructionFrame, text="2.The exam will be for 10 minutes",bg="light blue", fg="blue", font=('fira-code', 15))
secondinstruction.place(x=10, y=260)

thirdinstruction = Label(ExamInstructionFrame, text="3.The exam will start after 20 seconds",bg="light blue", fg="blue", font=('fira-code', 15))
thirdinstruction.place(x=10, y=290)

fourthinstruction = Label(ExamInstructionFrame, text="4.Each question should be submitted before entering to next question",bg="light blue", fg="blue", font=('fira-code', 15))
fourthinstruction.place(x=10, y=320)

startbutton = Button(ExamInstructionFrame,text = "Start",bg ="dark green",fg = "black")
startbutton.place(x=430,y=600,height=30,width=50)

'''**********************************************************MCQ QUESTIONS FRAME********************************************************'''
MCQQuestionsFrame = Frame(w,bg="light blue")
MCQQuestionsFrame.place_forget()
QuestionsLabel = Label(MCQQuestionsFrame, bg="light blue",fg="blue", font=('fira-code'))
QuestionsLabel.place(x=30,y=30)

answer = StringVar()
answer.set(False)

AnsOption1 = Radiobutton(MCQQuestionsFrame,variable=answer,bg="light blue",fg="blue")
AnsOption1.place(x=30,y=60)

AnsOption2 = Radiobutton(MCQQuestionsFrame,variable = answer,bg="light blue",fg="blue")
AnsOption2.place(x=30,y=80)

AnsOption3 = Radiobutton(MCQQuestionsFrame,variable= answer,bg="light blue",fg="blue")
AnsOption3.place(x=30,y=100)

AnsOption4 = Radiobutton(MCQQuestionsFrame,variable = answer,bg="light blue",fg="blue")
AnsOption4.place(x=30,y=120)

savebutton = Button(MCQQuestionsFrame,text="Save",bg="dark green",fg="black")

nextbutton = Button(MCQQuestionsFrame,bg="dark green",fg="black")

MCQQuestionDisplayFrame = Frame(w,bg='light blue')
MCQQuestionDisplayFrame.place_forget()
questionlabellist = ['Q1','Q2','Q3','Q4','Q5']

'''*******************************************************SBQ QUESTIONS FRAME************************************************************'''
SBQQuestionsFrame = Frame(w,bg="light blue")
SBQQuestionsFrame.place_forget()

SBQQuestionLabel = Label(SBQQuestionsFrame,bg="light blue",fg="blue",font=('fira-code'))
SBQQuestionLabel.place(x=30,y=70)

SBQsavebutton = Button(SBQQuestionsFrame,text= "save",bg="dark green",fg = "black")

SBQAnswerText = Text(SBQQuestionsFrame)

SBQnextbutton = Button(SBQQuestionsFrame,bg = "dark green",fg = "black")

SBQFinishButton = Button(SBQQuestionsFrame,bg = "dark green",fg = "black")

'''*****************************************************FINAL RESULT PAGE****************************************************************'''

FinalResultFrame = Frame(dashframe, bg="light blue", relief=SUNKEN, bd=5)
FinalResultFrame.place_forget()

StudentEmail = Label(FinalResultFrame,text="Email :",bg="light blue",fg = "blue")
StudentEmail.place(x=10,y=10)

StudentEmailDis = Label(FinalResultFrame,bg = "light blue",fg = "blue")
StudentEmailDis.place(x=150,y=10)

StudentName = Label(FinalResultFrame,text="Name :",bg="light blue",fg = "blue")
StudentName.place(x=10,y=30)

StudentNameDis = Label(FinalResultFrame,bg="light blue",fg = "blue")
StudentNameDis.place(x=150,y=30)

StudentMCQ = Label(FinalResultFrame,text = "MCQ :",bg = "light blue",fg="blue")
StudentMCQ.place(x=10,y=50)

StudentMCQAttempt = Label(FinalResultFrame,text = "MCQAttempt :",bg = "light blue",fg = "blue")
StudentMCQAttempt.place(x=30,y=70)

StudentMCQAttemptDis = Label(FinalResultFrame,bg = "light blue",fg = "blue")
StudentMCQAttemptDis.place(x=150,y=70)

StudentMCQMarksScored = Label(FinalResultFrame,text="MCQMarksScored :",bg="light blue",fg = "blue")
StudentMCQMarksScored.place(x=30,y=90)

StudentMCQMarksScoredDis = Label(FinalResultFrame,bg="light blue",fg = "blue")
StudentMCQMarksScoredDis.place(x=150,y=90)

StudentMCQStage1 = Label(FinalResultFrame,text="Stage1 :",bg = "light blue",fg = "blue")
StudentMCQStage1.place(x=30,y=110)

StudentMCQStage1Dis = Label(FinalResultFrame,bg = "light blue",fg = "blue")
StudentMCQStage1Dis.place(x=150,y=110)

StudentSBQ = Label(FinalResultFrame,text = "SBQ :",bg = "light blue",fg="blue")
StudentSBQ.place(x=10,y=130)

StudentSBQAttempt = Label(FinalResultFrame,text = "SBQAttempt :",bg = "light blue",fg = "blue")
StudentSBQAttempt.place(x=30,y=150)

StudentSBQAttemptDis = Label(FinalResultFrame,bg = "light blue",fg = "blue")
StudentSBQAttemptDis.place(x=150,y=150)

StudentSBQMarksScored = Label(FinalResultFrame,text="SBQMarksScored :",bg="light blue",fg = "blue")
StudentSBQMarksScored.place(x=30,y=170)

StudentSBQMarksScoredDis = Label(FinalResultFrame,bg="light blue",fg = "blue")
StudentSBQMarksScoredDis.place(x=150,y=170)

StudentSBQStage2 = Label(FinalResultFrame,text="Stage2 :",bg = "light blue",fg = "blue")
StudentSBQStage2.place(x=30,y=190)

StudentSBQStage2Dis = Label(FinalResultFrame,bg = "light blue",fg = "blue")
StudentSBQStage2Dis.place(x=150,y=190)

StudentLogin = Label(FinalResultFrame,text = "Login Time:",bg = "light blue",fg="blue")
StudentLogin.place(x=10,y=220)

StudentLoginDis = Label(FinalResultFrame,bg="light blue",fg = "blue")
StudentLoginDis.place(x=150,y=220)

printButton = Button(FinalResultFrame,text="print",bg="dark green",fg="black")
printButton.place(x=230,y=450)













w.mainloop()
