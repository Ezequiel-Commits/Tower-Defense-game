import turtle

import tower
import bullet
import orc
import animationManager
import gatehouse

WINDOW  = None
# X and Y dimensions of the window; measured in pixels
WINX, WINY = 400, 400

def main():
    """Main function"""
    def setupWin(): #Sets up the turtle window
            global WINDOW
            # making the screen
            WINDOW = turtle.Screen()
            # setup the screen size
            WINDOW.setup(WINX,WINY)
            # set the background color
            WINDOW.bgcolor("white")

    setupWin()

    """Basic testing of creating objects and using their methods"""

    myTowerObject = tower.Tower(x = 20, y = 140, size = 10)
    # myTowerObject.draw()

    myOrcObject = orc.Orc(x = 20, y = 50, size = 10)
    # myOrcObject.draw()

    myOrcObject2 = orc.Orc(x = 20, y = 100, size = 10)

    myTowerObject2 = tower.Tower(x = -20, y = 140, size = 10)

    myGatehouse = gatehouse.Gatehouse(x = 150, y = 0, size = 15) #Bit of error with the bounding circle here 
    
    mySpriteList = [myTowerObject, myTowerObject2, myGatehouse]

    # An animation Manager to avoid lag 
    myAnimationManager = animationManager.AnimationManager(spriteList = mySpriteList)
    myAnimationManager.updateScreen()

    def createTowerOnClick(x,y):
          newTower = tower.Tower(x, y, size = 10)
          mySpriteList.append(newTower)
    
    # Place a new tower when the player clicks on the sceen 
    WINDOW.listen()
    WINDOW.onscreenclick(createTowerOnClick)
    WINDOW.mainloop() #Runs the screen

main()