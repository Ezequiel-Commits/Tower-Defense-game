import turtle

import tower
import bullet
import orc
import animationManager
import gatehouse
import graphical

WINDOW  = None
# X and Y dimensions of the window; measured in pixels
WINX, WINY = 400, 400

def main():
    """Main function"""
    def setupWindow(): 
            global WINDOW
            # making the screen
            WINDOW = turtle.Screen()
            # setup the screen size
            WINDOW.setup(WINX,WINY)
            # set the background color
            WINDOW.bgcolor("white")

    setupWindow()

    """Have the locations of sprite move with the location of the gui."""

    myTowerObject = tower.Tower(x = 20, y = 140, size = 10)
    # myTowerObject.draw()

    myOrcObject = orc.Orc(x = 20, y = 50, size = 10)
    # myOrcObject.draw()

    myOrcObject2 = orc.Orc(x = 20, y = 100, size = 10)

    myTowerObject2 = tower.Tower(x = -20, y = 140, size = 10)

    myGraphicalObject = graphical.Graphical1()
    myGraphicalObject.draw()

    myGatehouse = gatehouse.Gatehouse(x = 150, y = 0, size = 15) 
    
    mySpriteList = [myTowerObject, myTowerObject2, myGatehouse]


    # An animation Manager to avoid lag(Still lags after enough time has run, making me think I'm not eliminating enough sprites)
    myAnimationManager = animationManager.AnimationManager(spriteList = mySpriteList)
    myAnimationManager.updateScreen()

    def createTowerOnClick(x,y): #Feels like this should go elsewhere. However, a tower can't be added to the spritelist from the class, and the onscreenclick function only works in the main file(?)
        clickCount = myGraphicalObject.checkForClicks(x,y)
        print(clickCount)
        if clickCount % 2 == 0: #If the clickCount is even, place the tower
            newTower = tower.Tower(x, y, size = 10)
            mySpriteList.append(newTower)
        else:
            pass
    
    # Place a new tower when the player clicks on the sceen 
    WINDOW.listen()
    WINDOW.onscreenclick(createTowerOnClick) # Don't believe I could get lambda to work here. 
    WINDOW.mainloop() #Runs the screen

main()