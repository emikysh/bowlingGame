'''
Created on Apr 8, 2020

@author: emikysh
'''

class Bowling(object):
    '''
    classdocs
    '''
    
    numOfFrame = 10

    def __init__(self):
        self.game = ""
        self.rolls = []
        self.score = 0

    def startGame(self, game):
        self.game = game

    def checkFrameValue(self, frame):
        frameValue = []
        
        for roll in frame:
            if roll == "-":
                frameValue.append(0)
            elif roll == "X":
                frameValue.append(10)
            elif roll == "/":
                frameValue.append(10 - frameValue[0])
            else:
                frameValue.append(int(roll))
        
        return frameValue
    
    def setRolls(self):
        for frame in self.game.split():
            self.rolls.append(self.checkFrameValue(frame))
        return self.rolls

    def getScore(self):
        for frame in range(self.numOfFrame):
            if self.isSpare(frame):
                self.score += 10 + self.getNextRoll(frame)
            elif self.isStrike(frame):
                self.score += 10 + self.getNextRollTwice(frame)
            else:
                self.score += sum(self.rolls[frame])
            
        return self.score
    
    def getNextRoll(self, frame):
        return self.rolls[frame+1][0]
    
    def getNextRollTwice(self, frame):
        if self.isStrike(frame+1):
            return self.getNextRoll(frame) + self.rolls[frame+2][0]
        else:
            return self.getNextRoll(frame) + self.rolls[frame+1][1]

    def isStrike(self, frame):
        return len(self.rolls[frame]) == 1 and sum(self.rolls[frame]) == 10
        
    def isSpare(self, frame):
        return len(self.rolls[frame]) == 2 and sum(self.rolls[frame]) == 10
    
    
