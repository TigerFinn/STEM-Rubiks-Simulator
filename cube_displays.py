import cube_structure as cbStr
import display_sets as dspSet #Needed to initialise the cube position if no save is found
#p is used in for loops instead of x because x is a valid move with the cube (X rotations)

'''
These load and save functions need updated drastically. They only track piece position which will just collapse now with a working piece rotation scheme
For some strange reason, when I tried updating these they stopped working
'''

#Loads in the basic save from the next function
#Again it does not track rotation of piece or cube
def load_save():
    c,e,r=cbStr.init()
    try:
        file=open("cube_save.txt","r")
        lst=file.readline().split(" ") #Gets a list of piece positions
        i=0 #Iterator for corners
        o=0 #Iterator for edges
        while i < 20: #20 is the total number of pieces, being 8 corners and 12 edges
            if i < 8: #Implements for corners
                c[c[i].pHom].pCur = int(lst[i][0:1]) #Sets pCur of relevant piece to the desired value
                c[c[i].pHom].rCur = int(lst[i][2:3]) 
            else: #Implements for edges
                #o is used for the position in e[e[o].pCur]].pCur
                #If statement because edge indexes go into double digits so 11.0 doesn't work with [0:1]
                if len(lst[o+8]) > 3:
                    e[e[o].pHom].pCur = int(lst[o+8][0:2]) #Sets pCur of relevant piece to the desire value
                    e[e[o].pHom].rCur = int(lst[o+8][3:4])
                else:
                    e[e[o].pHom].pCur = int(lst[o+8][0:1]) #Sets pCur of relevant piece to the desire value
                    e[e[o].pHom].rCur = int(lst[o+8][2:3])
                o+=1
            i+=1
        file.close()
    except:
        c,e,r=cbStr.init()
    return c,e,r

#A basic save system that will save to the source location, because I don't know the fancy dirpath stuff yet
#This does not save the rotation of the cube, that gets initialised to a green front white top, as is standard
#It also doesn't save the rotation of the pieces, so it won't work very well anymore
def save_test():
    f=open("test.txt","w")
    f.write("Hello There Please Make This Work")

def write_save(c,e):
    print("saved")
    f=open("cube_save.txt","w") #Opens a file
    for p in c: #Loops through each corner piece and records the current position
        f.write(str(p.pCur) + "." + str(p.rCur) + " ")
    for p in e: #Loops through each edge piece and records the current position
        f.write(str(p.pCur) + "." + str(p.rCur) + " ")

    f.close() #Closes a file

#Used each time a set of moves is made to check if the cube is solved
def check_solve(c, e):
    i=0
    for p in c: #Loops for each corner
        if c[i].pCur != c[i].pHom or c[i].rCur != 0: #checks if the piece is in solved position and rotation is 0
            #When one invalid piece is found, the code will break with a negative response
            return False
            break
        i+=1
    #The above code is repeated for edges
    i=0
    for p in e:
        if e[i].pCur != e[i].pHom or e[i].rCur != 0:
            return False
            break
        i+=1
    return True


def display_cube(c,e,r):
    '''
    Cube Displays\n
    This works quite nicely, just need to work on colours now
    The following functions use the Full Net as an indicator for pieces
    '''
    #Alphanumerics are used to indicate the index of each piece, and then the piece face is indicated with the number
    #The second letter indicates if it is a corner or edge
    for p in c:
        if p.pCur==0:
            ac0,ac1,ac2=cornerAssign(p)
        elif p.pCur==1:
            bc0,bc1,bc2=cornerAssign(p)
        elif p.pCur==2:
            cc0,cc1,cc2=cornerAssign(p)
        elif p.pCur==3:
            dc0,dc1,dc2=cornerAssign(p)
        elif p.pCur==4:
            ec0,ec1,ec2=cornerAssign(p)
        elif p.pCur==5:
            fc0,fc1,fc2=cornerAssign(p)
        elif p.pCur==6:
            gc0,gc1,gc2=cornerAssign(p)
        elif p.pCur==7:
            hc0,hc1,hc2=cornerAssign(p)

    for p in e:
        if p.pCur==0:
            ae0,ae1=edgeAssign(p)
        elif p.pCur==1:
            be0,be1=edgeAssign(p)
        elif p.pCur==2:
            ce0,ce1=edgeAssign(p)
        elif p.pCur==3:
            de0,de1=edgeAssign(p)
        elif p.pCur==4:
            ee0,ee1=edgeAssign(p)
        elif p.pCur==5:
            fe0,fe1=edgeAssign(p)
        elif p.pCur==6:
            ge0,ge1=edgeAssign(p)
        elif p.pCur==7:
            he0,he1=edgeAssign(p)
        elif p.pCur==8:
            ie0,ie1=edgeAssign(p)
        elif p.pCur==9:
            je0,je1=edgeAssign(p)
        elif p.pCur==10:
            ke0,ke1=edgeAssign(p)
        elif p.pCur==11:
            le0,le1=edgeAssign(p)

    eLst=[ae0,ae1,be0,be1,ce0,ce1,de0,de1,ee0,ee1,fe0,fe1,ge0,ge1,he0,he1,ie0,ie1,je0,je1,ke0,ke1,le0,le1]
    cLst=[ac0,ac1,ac2,bc0,bc1,bc2,cc0,cc1,cc2,dc0,dc1,dc2,ec0,ec1,ec2,fc0,fc1,fc2,gc0,gc1,gc2,hc0,hc1,hc2]

#Sets the colours for the centre pieces based on positions.
    for p in r:
        if p.rCur == "U":
            up = p.rHom
        elif p.rCur == "F":
            front = p.rHom
        elif p.rCur == "R":
            right = p.rHom
        elif p.rCur == "B":
            back = p.rHom
        elif p.rCur == "L":
            left = p.rHom
        elif p.rCur == "D":
            down = p.rHom

    

    cLst,eLst=colourAssign(cLst,eLst)

    if front=="🟩":
        if up=="⬜":
            dspSet.GW(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟥":
            dspSet.GR(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟨":
            dspSet.GY(up,down,front,back,right,left,eLst,cLst)
        else:
            dspSet.GO(up,down,front,back,right,left,eLst,cLst)
    elif front=="🟥":
        if up=="⬜":
            dspSet.RW(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟦":
            dspSet.RB(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟨":
            dspSet.RY(up,down,front,back,right,left,eLst,cLst)
        else:
            dspSet.RG(up,down,front,back,right,left,eLst,cLst)
    elif front=="🟦":
        if up=="⬜":
            dspSet.BW(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟧":
            dspSet.BO(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟨":
            dspSet.BY(up,down,front,back,right,left,eLst,cLst)
        else:
            dspSet.BR(up,down,front,back,right,left,eLst,cLst)
    elif front=="🟧":
        if up=="⬜":
            dspSet.OW(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟩":
            dspSet.OG(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟨":
            dspSet.OY(up,down,front,back,right,left,eLst,cLst)
        else:
            dspSet.OB(up,down,front,back,right,left,eLst,cLst)
    elif front=="⬜":
        if up=="🟩":
            dspSet.WG(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟧":
            dspSet.WO(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟦":
            dspSet.WB(up,down,front,back,right,left,eLst,cLst)
        else:
            dspSet.WR(up,down,front,back,right,left,eLst,cLst)
    else:
        if up=="🟩":
            dspSet.YG(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟥":
            dspSet.YR(up,down,front,back,right,left,eLst,cLst)
        elif up=="🟦":
            dspSet.YB(up,down,front,back,right,left,eLst,cLst)
        else:
            dspSet.YO(up,down,front,back,right,left,eLst,cLst)


#Corner and edge assignment functions are used for displaying the piece with rotation indicated.
#Both check the value of rotation and sort the pieces as required
#It returns a list for the pieces in the display function
#Each piece is displayed as Index.Rotation, so it displays with reference to the most accurate cube net that I have
def cornerAssign(p):
    if p.rCur==0:
        n0,n1,n2=(str(p.pHom) + ".0"),(str(p.pHom) + ".1"),(str(p.pHom) + ".2")
    elif p.rCur==1:
        n0,n1,n2=(str(p.pHom) + ".2"),(str(p.pHom) + ".0"),(str(p.pHom) + ".1")
    else:
        n0,n1,n2=(str(p.pHom) + ".1"),(str(p.pHom) + ".2"),(str(p.pHom) + ".0")
    return n0,n1,n2

#As above
def edgeAssign(p):
    if p.rCur==0:
        n0,n1=(str(p.pHom) + ".0"),(str(p.pHom) + ".1")
    else:
        n0,n1=(str(p.pHom) + ".1"),(str(p.pHom) + ".0")
    return n0,n1

#Probably a more efficient way, but this assigns individual colours to each piece face.
#It runs through every piece and just assigns the coloured square
def colourAssign(cLst,eLst):
    i=0
    while i < 24:
        #whites
        if cLst[i]=="0.0" or cLst[i]=="3.0" or cLst[i]=="4.0" or cLst[i]=="7.0":
            cLst[i]="⬜"
        #Greens
        elif cLst[i]=="0.2" or cLst[i]=="1.1" or cLst[i]=="2.2" or cLst[i]=="3.1":
            cLst[i]="🟩"
        #Reds
        elif cLst[i]=="0.1" or cLst[i]=="1.2" or cLst[i]=="4.2" or cLst[i]=="5.1":
            cLst[i]="🟥"
        #Blues
        elif cLst[i]=="4.1" or cLst[i]=="5.2" or cLst[i]=="6.1" or cLst[i]=="7.2":
            cLst[i]="🟦"
        #Oranges
        elif cLst[i]=="2.1" or cLst[i]=="3.2" or cLst[i]=="6.2" or cLst[i]=="7.1":
            cLst[i]="🟧"
        #Yellows
        else:
            cLst[i]="🟨"

        #whites
        if eLst[i]=="0.0" or eLst[i]=="4.0" or eLst[i]=="7.0" or eLst[i]=="8.0":
            eLst[i]="⬜"
        #Greens
        elif eLst[i]=="0.1" or eLst[i]=="1.0" or eLst[i]=="2.1" or eLst[i]=="3.0":
            eLst[i]="🟩"
        #Reds
        elif eLst[i]=="1.1" or eLst[i]=="4.1" or eLst[i]=="11.1" or eLst[i]=="5.1":
            eLst[i]="🟥"
        #Blues
        elif eLst[i]=="8.1" or eLst[i]=="9.0" or eLst[i]=="10.1" or eLst[i]=="11.0":
            eLst[i]="🟦"
        #Oranges
        elif eLst[i]=="3.1" or eLst[i]=="6.1" or eLst[i]=="7.1" or eLst[i]=="9.1":
            eLst[i]="🟧"
        #Yellows
        else:
            eLst[i]="🟨"
        i+=1


    return cLst, eLst