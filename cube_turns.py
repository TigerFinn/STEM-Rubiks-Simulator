from distutils.util import rfc822_escape
import cube_rotations as rtte
import piece_rotations as pcRt

#Movement for single turns
def turn(pcs, n1, n2, n3, n4):
    tempPcs = pcs
    #Loops through and finds the necessary piece and changes it
    i=0
    while i < len(pcs):
        if tempPcs[i].pCur==n1:
            pcs[i].pCur = n2
        elif tempPcs[i].pCur==n2:
            pcs[i].pCur=n3
        elif tempPcs[i].pCur==n3:
            pcs[i].pCur=n4        
        elif tempPcs[i].pCur==n4:
            pcs[i].pCur=n1
        i+=1
    return pcs

#Movement for double turns
def turn2(pcs, n1, n2, n3, n4):
    tempPcs = pcs
    #Loops through and finds the necessary piece and changes it
    i=0
    while i < len(pcs):
        if tempPcs[i].pCur==n1:
            pcs[i].pCur = n3
        elif tempPcs[i].pCur==n2:
            pcs[i].pCur=n4
        elif tempPcs[i].pCur==n3:
            pcs[i].pCur=n1           
        elif tempPcs[i].pCur==n4:
            pcs[i].pCur=n2
        i+=1   
    return pcs

'''
Calls User Input
'''

def call_Prime(p,c,e,rt):
    if p[0:1]==rt[2].rCur:
        c,e=Ri(c,e)
    elif p[0:1]==rt[4].rCur:
        c,e=Li(c,e)
    elif p[0:1]==rt[1].rCur:
        c,e=Fi(c,e)
    elif p[0:1]==rt[3].rCur:
        c,e=Bi(c,e)
    elif p[0:1]==rt[0].rCur:
        c,e=Ui(c,e)
    elif p[0:1]==rt[5].rCur:
        c,e=Di(c,e)
    elif p[0:1].upper()=="X":
        rt=rtte.xi(rt)
    elif p[0:1].upper()=="Y":
        rt=rtte.yi(rt)
    elif p[0:1].upper()=="Z":
        rt=rtte.zi(rt)
    elif p[0:1]==rt[2].rCur.lower():
        c,e,rt=ri(c,e,rt)
    elif p[0:1]==rt[4].rCur.lower():
        c,e,rt=li(c,e,rt)
    elif p[0:1]==rt[1].rCur.lower():
        c,e,rt=fi(c,e,rt)
    elif p[0:1]==rt[3].rCur.lower():
        c,e,rt=bi(c,e,rt)
    elif p[0:1]==rt[0].rCur.lower():
        c,e,rt=ui(c,e,rt)
    elif p[0:1]==rt[5].rCur.lower():
        c,e,rt=di(c,e,rt)
    elif p[0:1].upper()=="M":
        c,e,rt=Mi(c,e,rt)
    elif p[0:1].upper()=="E":
        c,e,rt=Ei(c,e,rt)
    elif p[0:1].upper()=="S":
        c,e,rt=Si(c,e,rt)
    return c,e,rt

def call_Double(p,c,e,rt):
    if p[0:1]==rt[2].rCur:
        c,e=R2(c,e)
    elif p[0:1]==rt[4].rCur:
        c,e=L2(c,e)
    elif p[0:1]==rt[1].rCur:
        c,e=F2(c,e)
    elif p[0:1]==rt[3].rCur:
        c,e=B2(c,e)
    elif p[0:1]==rt[0].rCur:
        c,e=U2(c,e)
    elif p[0:1]==rt[5].rCur:
        c,e=D2(c,e)
    elif p[0:1].upper()=="X":
        rt=rtte.x2(rt)
    elif p[0:1].upper()=="Y":
        rt=rtte.y2(rt)
    elif p[0:1].upper()=="Z":
        rt=rtte.z2(rt)
    elif p[0:1]==rt[2].rCur.lower():
        c,e,rt=r2(c,e,rt)
    elif p[0:1]==rt[4].rCur.lower():
        c,e,rt=l2(c,e,rt)
    elif p[0:1]==rt[1].rCur.lower():
        c,e,rt=f2(c,e,rt)
    elif p[0:1]==rt[3].rCur.lower():
        c,e,rt=b2(c,e,rt)
    elif p[0:1]==rt[0].rCur.lower():
        c,e,rt=u2(c,e,rt)
    elif p[0:1]==rt[5].rCur.lower():
        c,e,rt=d2(c,e,rt)
    elif p[0:1].upper()=="M":
        c,e,rt=M2(c,e,rt)
    elif p[0:1].upper()=="E":
        c,e,rt=E2(c,e,rt)
    elif p[0:1].upper()=="S":
        c,e,rt=S2(c,e,rt)
    return c,e,rt

def call_Single(p,c,e,rt):
    if p==rt[2].rCur:
        c,e=R(c,e)
    elif p==rt[4].rCur:
        c,e=L(c,e)
    elif p==rt[1].rCur:
        c,e=F(c,e)
    elif p==rt[3].rCur:
        c,e=B(c,e)
    elif p==rt[0].rCur:
        c,e=U(c,e)
    elif p==rt[5].rCur:
        c,e=D(c,e)
    elif p.upper()=="X":
        rt=rtte.x(rt)
    elif p.upper()=="Y":
        rt=rtte.y(rt)
    elif p.upper()=="Z":
        rt=rtte.z(rt)
    elif p==rt[2].rCur.lower():
        c,e,rt=r(c,e,rt)
    elif p==rt[4].rCur.lower():
        c,e,rt=l(c,e,rt)
    elif p==rt[1].rCur.lower():
        c,e,rt=f(c,e,rt)
    elif p==rt[3].rCur.lower():
        c,e,rt=b(c,e,rt)
    elif p==rt[0].rCur.lower():
        c,e,rt=u(c,e,rt)
    elif p==rt[5].rCur.lower():
        c,e,rt=d(c,e,rt)
    elif p.upper()=="M":
        c,e,rt=M(c,e,rt)
    elif p.upper()=="E":
        c,e,rt=E(c,e,rt)
    elif p.upper()=="S":
        c,e,rt=S(c,e,rt)
    return c,e,rt


'''
All the following functions run ... something?

'''


"""
#Standard Layer Rotations
"""
#Clock wise turns
def R(c,e): #turn red face
    c,e=pcRt.rPiece(c,e,"R")
    e=turn(e,4,11,5,1)
    c=turn(c,4,5,1,0)
    return c,e
def L(c,e): #turn orange face
    c,e=pcRt.rPiece(c,e,"L")
    e=turn(e,7,3,6,9)
    c=turn(c,3,2,6,7)
    return c,e
def F(c,e): #turn green face
    c,e=pcRt.rPiece(c,e,"F")
    e=turn(e,0,1,2,3)
    c=turn(c,0,1,2,3)
    return c,e
def B(c,e): #turn blue face
    c,e=pcRt.rPiece(c,e,"B")
    e=turn(e,8,9,10,11)
    c=turn(c,7,6,5,4)
    return c,e
def U(c,e): #turn white face
    e=turn(e,8,4,0,7)
    c=turn(c,4,0,3,7)
    return c,e
def D(c,e): #turn rtte.yellow face
    e=turn(e,2,5,10,6)
    c=turn(c,1,5,6,2)
    return c,e

#Anti-clock wise turns
def Ri(c,e): #turn red face
    c,e=pcRt.rPiece(c,e,"R")
    e=turn(e,1,5,11,4)
    c=turn(c,0,1,5,4)
    return c,e
def Li(c,e): #turn orange face
    c,e=pcRt.rPiece(c,e,"L")
    e=turn(e,9,6,3,7)
    c=turn(c,7,6,2,3)
    return c,e
def Fi(c,e): #turn green face
    c,e=pcRt.rPiece(c,e,"F")
    e=turn(e,3,2,1,0)
    c=turn(c,3,2,1,0)
    return c,e
def Bi(c,e): #turn blue face
    c,e=pcRt.rPiece(c,e,"B")
    e=turn(e,11,10,9,8)
    c=turn(c,4,5,6,7)
    return c,e
def Ui(c,e): #turn white face
    e=turn(e,7,0,4,8)
    c=turn(c,7,3,0,4)
    return c,e
def Di(c,e): #turn yellow face
    e=turn(e,6,10,5,2)
    c=turn(c,2,6,5,1)
    return c,e

#Double turns
def R2(c,e): #turn red face
    e=turn2(e,4,11,5,1)
    c=turn2(c,4,5,1,0)
    return c,e
def L2(c,e): #turn orange face
    e=turn2(e,7,3,6,9)
    c=turn2(c,3,2,6,7)
    return c,e
def F2(c,e): #turn green face
    e=turn2(e,0,1,2,3)
    c=turn2(c,0,1,2,3)
    return c,e
def B2(c,e): #turn blue face
    e=turn2(e,8,9,10,11)
    c=turn2(c,7,6,5,4)
    return c,e
def U2(c,e): #turn white face
    e=turn2(e,8,4,0,7)
    c=turn2(c,4,0,3,7)
    return c,e
def D2(c,e): #turn rtte.yellow face
    e=turn2(e,2,5,10,6)
    c=turn2(c,1,5,6,2)
    return c,e

"""
#Complex Turns (Slices)
"""
#Clockwise
def M(c,e,r): #turn middle slice
    r=rtte.xi(r)
    c,e,r=call_Prime("Li",c,e,r)
    c,e,r=call_Single("R",c,e,r)
    return c,e,r
def E(c,e,r): #turn equator slice
    r=rtte.yi(r)
    c,e,r=call_Prime("Di",c,e,r)
    c,e,r=call_Single("U",c,e,r)
    return c,e,r
def S(c,e,r): #turn side slice
    r=rtte.z(r)
    c,e,r=call_Prime("Fi",c,e,r)
    c,e,r=call_Single("B",c,e,r)
    return c,e,r

#Anticlockwise
def Mi(c,e,r):
    r=rtte.x(r)
    c,e,r=call_Single("L",c,e,r)
    c,e,r=call_Prime("Ri",c,e,r)
    return c,e,r
def Ei(c,e,r):
    r=rtte.y(r)
    c,e,r=call_Single("D",c,e,r)
    c,e,r=call_Prime("Ui",c,e,r)
    return c,e,r
def Si(c,e,r):
    r=rtte.zi(r)
    c,e,r=call_Single("F",c,e,r)
    c,e,r=call_Prime("Bi",c,e,r)
    return c,e,r

#Double
def M2(c,e,r):
    r=rtte.x2(r)
    c,e,r=call_Double("L",c,e,r)
    c,e,r=call_Double("R",c,e,r)
    #c,e=L2(c,e)
    #c,e=R2(c,e)
    return c,e,r
def E2(c,e,r):
    r=rtte.y2(r)
    c,e,r=call_Double("U",c,e,r)
    c,e,r=call_Double("D",c,e,r)
    return c,e,r
def S2(c,e,r):
    r=rtte.z2(r)
    c,e,r=call_Double("F",c,e,r)
    c,e,r=call_Double("B",c,e,r)
    #c,e=F2(c,e)
   # c,e=B2(c,e)
    return c,e,r

"""
#Complex Turns (Wides)
"""
#Clockwise
def r(c,e,r):
    r=rtte.x(r)
    c,e=L(c,e)
    return c,e,r
def l(c,e,r):
    r=rtte.xi(r)
    c,e=R(c,e)
    return c,e,r
def f(c,e,r):
    r=rtte.z(r)
    c,e=B(c,e) 
    return c,e,r
def b(c,e,r):
    r=rtte.zi(r)
    c,e=F(c,e)
    return c,e,r
def u(c,e,r):
    r=rtte.y(r)
    c,e=D(c,e)
    return c,e,r
def d(c,e,r):
    r=rtte.yi(r)
    c,e=U(c,e)
    return c,e,r

#Anti-clockwise 
def ri(c,e,r):
    r=rtte.xi(r)
    c,e=Li(c,e)
    return c,e,r
def li(c,e,r):
    r=rtte.x(r)
    c,e=Ri(c,e)
    return c,e,r
def fi(c,e,r):
    r=rtte.zi(r)
    c,e=Bi(c,e)
    return c,e,r
def bi(c,e,r):
    r=rtte.z(r)
    c,e=Fi(c,e)
    return c,e,r
def ui(c,e,r):
    r=rtte.yi(r)
    c,e=Di(c,e)
    return c,e,r
def di(c,e,r):
    r=rtte.y(r)
    c,e=Ui(c,e)
    return c,e,r

#Doubles
def r2(c,e,r):
    r=rtte.x2(r)
    c,e=L2(c,e)
    return c,e,r
def l2(c,e,r):
    r=rtte.x2(r)
    c,e=R2(c,e)
    return c,e,r
def f2(c,e,r):
    r=rtte.z2(r)
    c,e=B2(c,e)
    return c,e,r
def b2(c,e,r):
    r=rtte.z2(r)
    c,e=F2(c,e)
    return c,e,r
def u2(c,e,r):
    r=rtte.y2(r)
    c,e=D2(c,e)
    return c,e,r
def d2(c,e,r):
    r=rtte.y2(r)
    c,e=U2(c,e)
    return c,e,r
    