def rPiece(c,e,face):
    i=0
    c1,c2,c3,c4=cornerAssign(face)
    while i < len(c):
        if c[i].pCur==c1 or c[i].pCur==c2:
            c[i].rCur+=1
        if c[i].pCur==c3 or c[i].pCur==c4:
            c[i].rCur+=2
        i+=1
    c=check(c,3)
    if face=="F" or face=="B":
        e1,e2,e3,e4 = edgeAssign(face)
        i=0
        while i < len(e):
            if e[i].pCur==e1 or e[i].pCur==e2 or e[i].pCur==e3 or e[i].pCur==e4:
                e[i].rCur+=1
            i+=1
        e=check(e,2)
    return c,e

def cornerAssign(face):
    if face=="R":
        c1,c2,c3,c4=0,5,1,4
    elif face=="L":
        c1,c2,c3,c4=7,2,3,6
    elif face=="F":
        c1,c2,c3,c4=3,1,0,2
    elif face=="B":
        c1,c2,c3,c4=6,4,5,7
    return c1, c2, c3, c4

def edgeAssign(face):
    if face=="F":
        e1,e2,e3,e4=0,1,2,3
    elif face=="B":
        e1,e2,e3,e4=8,9,10,11
    return e1,e2,e3,e4

def check(r,n):
    i=0
    while i < len(r):
        if r[i].rCur < 0:
            r[i].rCur+=n
        elif r[i].rCur > n-1:
            r[i].rCur-=n
        i+=1
    return r