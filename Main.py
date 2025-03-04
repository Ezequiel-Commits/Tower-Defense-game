import turtle

import sprite
import tower
import bullet
import orc
import animationManager
import collisionManager

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

    myBulletObject = bullet.Bullet(x = 20, y = 10, velX = 0, velY = 1, size = 5)
    myBulletObject2 = bullet.Bullet(x = 20, y = 120, velX = 0, velY = -1, size = 5)

    myTowerObject = tower.Tower(x = 20, y = 140, size = 10, bullet = myBulletObject)
    # myTowerObject.draw()

    myOrcObject = orc.Orc(x = 20, y = 50, size = 10)
    # myOrcObject.draw()

    myOrcObject2 = orc.Orc(x = 20, y = 100, size = 10)

    myTowerObject2 = tower.Tower(x = 20, y = 10, size = 10, bullet = myBulletObject2)
    
    mySpriteList = [myTowerObject, myOrcObject, myBulletObject, myOrcObject2, myTowerObject2, myBulletObject2]

    # An animation Manager to avoid lag 
    myAnimationManager = animationManager.AnimationManager(spriteList = mySpriteList)
    myAnimationManager.updateScreen()




    WINDOW.mainloop() #Runs the screen

main()