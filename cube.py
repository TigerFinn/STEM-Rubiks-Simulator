"""
Things I've done:
-Solved the problem of reading in as an a string which stopped it from turning
-I decided it was more efficient to create new functions for prime turns, rather than using standards 3 times - doubles have a seperate function to make it more efficient
-Created a display which shows the net cube with piece index numbers
-CUBE ROTATIONS WORK!
-Abnormal/Complex turns such as wides and slices now work - this was done by creating functions that implemented standard turns and cube rotations - Turns out there was a bug where it always turn from base position (Green Front, White Top)
-Fixed problem so Complex turns actually work now!
-PIECE ROTATIONS WORK!
    These were a lot simpler than I thought.
    Assigned each piece a home rotation, and each face of a piece value 0, 1, or 2
    Becaue of the way home rotations were facing, pieces only "rotated" on certain turns R, L, F & B for corners; F & B for edges
    So I created functions that switch the rotation accordingly
    -Combined all piece rotations into one function
-UI Advancements
    Each face of a piece now shows it's individual rotation, so it matches up better with the real cube :)
-27/05/2022
    Colours show for centre pieces
    Finally got the dynamic display working!
        This was done by coding all 24 possible rotation positions - it probably could have been done easier but I was pressed for time and this worked 
-30/05/2022
    COLOUR, WOOOOOO
    We actually know have something which is recognisably(?) a Rubik's cube

    Colours are now using Unicode large coloured squares, and the UI is actually intelligeble (ish)
        it took a while to get this working, I had to go through display_sets and alter all the spacings as well as having a hassle changing the cube structure
-01/06/2022
    It now saves piece rotation as well as piece position, so saving works :)
"""

#Welcome to the cube structure - it's fairly illegible, but I've tried to add in some comments
import cube_structure as cbStr #Imports the arrays for holding pieces
import cube_displays as cbDis #Imports the functions for displaying the cube
import cube_turns as cbTrn #Imports the functions for turning the cube

#The base program
def main():
    #Sees if there is a saved cube, else loads in the initial positions
    c,e,rt=cbDis.load_save() #c is the list of corners, e is the list of edges and rt is the list of face positions

    #Initial cube display
    cbDis.display_cube(c,e,rt)

    #Takes first input
    userInput=input("What move do you want to make? ")
    #This loops continuosly until the user decides to stop
    while userInput.upper() != "Q":
        lst=userInput.split(" ") #Users can put in a string of moves, this splits them so it can loop through and carry out each
        #Will loop through each move
        for p in lst:
            #This will check the move type before checking what move to make
            if p[1:2]=="'" or p[1:2].upper()=="I": #Calls turn movements if it's an anti-clockwise move
                c,e,rt=cbTrn.call_Prime(p,c,e,rt)
            elif p[1:2]=="2": #Calls turn movements if it's a double turn
                c,e,rt=cbTrn.call_Double(p,c,e,rt)
            elif p=="solve": #Returns the cube to solve - uses initial function from cube_structure
                c,e,rt=cbStr.init()
            else: #Will try for a single turn if other criteria is not met
                c,e,rt=cbTrn.call_Single(p,c,e,rt) 

        
        cbDis.display_cube(c,e,rt) #Displays cube after each iteration
        if cbDis.check_solve(c,e)==True: #Displays a message to say if the cube is solved (helps with the bad UI)
            print("The Cube is Solved")
        #Gets the input again
        userInput=input("What move do you want to make? (enter q to save and exit) ")
    #Saves the cube for next time
    cbDis.write_save(c,e)
 
if __name__=="__main__":
    main()