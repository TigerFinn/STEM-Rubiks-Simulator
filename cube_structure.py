from cube_turns import *
from cube_displays import *

#Class for storing the position of pieces and their rotation
#Solved rotation is always 0
#Piece rotation refers to the rotational index of the index 0
#pHom is the solved position, and pCur will change as the cube is turned
class Piece:
    def __init__(self, pCur, pHom, rCur):
        self.pCur = pCur #current position
        self.pHom = pHom #solved position
        self.rCur = rCur #current piece rotation

#Rotation for each face
#This is so it can still track what move to make when a rotation is made
#i.e. if a move is made on an rCur value, the rHom face will be turned
#This could also be seen as the "position" of each face
class Rotation:
    def __init__(self, rCur, rHom):
        self.rCur = rCur #Identifier for the actual position
        self.rHom = rHom #Identifier for move to be made

#Initialises the cube into a solved position
def init():
    #Seperate arrays for corners and edges, 
    corners = [Piece(0,0,0),Piece(1,1,0),Piece(2,2,0),Piece(3,3,0),Piece(4,4,0),Piece(5,5,0),Piece(6,6,0),Piece(7,7,0)]
    edges = [Piece(0,0,0),Piece(1,1,0),Piece(2,2,0),Piece(3,3,0),Piece(4,4,0),Piece(5,5,0),Piece(6,6,0),Piece(7,7,0),Piece(8,8,0),Piece(9,9,0),Piece(10,10,0),Piece(11,11,0)]
    #Rotation is which way the cube is facing
    rotate = [Rotation("U","⬜"),Rotation("F","🟩"),Rotation("R","🟥"),Rotation("B","🟦"),Rotation("L","🟧"),Rotation("D","🟨")]

    return corners, edges, rotate
