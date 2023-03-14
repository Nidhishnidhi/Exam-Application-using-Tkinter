from tkinter import *
import random

def refresh(RHS,LHS,op):
    LHS.set(str(random.randint(1,10)))
    RHS.set(str(random.randint(1,10)))
    operator = random.choice('+-*')
    op.set(operator)
    expression = LHS.get()+op.get()+RHS.get()
    return expression
    
def captcha():
    LHS = StringVar()
    LHS.set(str(random.randint(1,10)))
    
    RHS = StringVar()
    RHS.set(str(random.randint(1,10)))
    
    op = StringVar()
    operator = random.choice('+-*')
    op.set(operator)
    
    expression = LHS.get()+op.get()+RHS.get()
    return RHS,LHS,op,expression




