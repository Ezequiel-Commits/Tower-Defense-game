"""A factory class to create orcs, allowing them to continuously storm the gatehouse"""
import orc

class OrcFactory:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
    def createOrc(self):
        # Creates an Orc given the parameters passed
        # newOrc = None
        
        newOrc = orc.Orc(x = self.x, y = self.y, size = self.size)

        return newOrc
