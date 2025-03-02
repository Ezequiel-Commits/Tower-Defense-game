import turtle

import sprite
import tower
import bullet

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

    # Basic testing of creating objects and using their methods
    mySpriteObject = sprite.Sprite(10,20)
    # mySpriteObject.draw()

    myTowerObject = tower.Tower(20,10)
    myTowerObject.draw()
    myTowerObject.updateSelf()

    myBulletObject = bullet.Bullet(x = 5, y = -5, velx = 1, vely = 1)
    # myBulletObject.draw()
    # myBulletObject.updateSelf()

    WINDOW.mainloop() #Runs the screen

main()