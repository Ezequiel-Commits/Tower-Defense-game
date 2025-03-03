import turtle

import sprite
import tower
import bullet
import orc
import animationManager

WINDOW  = None
# X and Y dimensions of the window; measured in pixels
WINX, WINY = 400, 350

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


    myTowerObject = tower.Tower(20,10)

    myBulletObject = bullet.Bullet(x = 5, y = -5, velX = 1, velY = 1)

    myOrcObject = orc.Orc(x = 0, y = 20)

    # An animation Manager to avoid lag 
    mySpriteList = [myTowerObject, myOrcObject]
    myAnimationManager = animationManager.AnimationManager(spriteList = mySpriteList)
    myAnimationManager.updateScreen()

    WINDOW.mainloop() #Runs the screen

main()