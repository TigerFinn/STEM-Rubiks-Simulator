from cube_structure import *

def rotate(Pos, n1, n2, n3, n4):
    tempPos = Pos
    #Loops through and finds the necessary face and changes it
    i=0
    while i < len(Pos):
        if tempPos[i].rCur==n1:
            Pos[i].rCur = n2
        elif tempPos[i].rCur==n2:
            Pos[i].rCur=n3
        elif tempPos[i].rCur==n3:
            Pos[i].rCur=n4        
        elif tempPos[i].rCur==n4:
            Pos[i].rCur=n1
        i+=1
    return Pos

def rotate2(Pos, n1, n2, n3, n4):
    tempPos = Pos
    #Loops through and finds the necessary face and changes it
    i=0
    while i < len(Pos):
        if tempPos[i].rCur==n1:
            Pos[i].rCur = n3
        elif tempPos[i].rCur==n2:
            Pos[i].rCur=n4
        elif tempPos[i].rCur==n3:
            Pos[i].rCur=n1        
        elif tempPos[i].rCur==n4:
            Pos[i].rCur=n2
        i+=1
    return Pos

#Basic Rotations
def x(r):
    r=rotate(r,"F","U","B","D")
    return r
def y(r):
    r=rotate(r,"L","B","R","F")
    return r
def z(r):
    r=rotate(r,"U","R","D","L")
    return r

#Inverted Rotations
def xi(r):
    r=rotate(r,"D","B","U","F")
    return r
def yi(r):
    r=rotate(r,"F","R","B","L")
    return r
def zi(r):
    r=rotate(r,"L","D","R","U")
    return r

#Double Rotations
def x2(r):
    r=rotate2(r,"F","U","B","D")
    return r
def y2(r):
    r=rotate2(r,"F","R","B","L")
    return r
def z2(r):
    r=rotate2(r,"U","R","D","L")
    return r
    