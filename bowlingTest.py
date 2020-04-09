'''
Created on Apr 8, 2020

@author: emikysh
'''
import unittest
from bowling import Bowling

class TestBowling(unittest.TestCase):

    def setUp(self):
        self.bowlingGame = Bowling()

    def testGutterGame(self):
        self.bowlingGame.startGame('-- -- -- -- -- -- -- -- -- --')
        self.bowlingGame.setRolls()
        score = self.bowlingGame.getScore()
        self.assertEqual(0, score)
 
    def testOnePinDown(self):
        self.bowlingGame.startGame('11 11 11 11 11 11 11 11 11 11')
        self.bowlingGame.setRolls()
        score = self.bowlingGame.getScore()
        self.assertEqual(20, score)
      
    def testOnePinDownAndSpareInFirstRoll(self):
        self.bowlingGame.startGame('9/ 11 11 11 11 11 11 11 11 11 11')
        self.bowlingGame.setRolls()
        score = self.bowlingGame.getScore()
        self.assertEqual(29, score)
       
    def testOnePinDownAndSpareInLastRoll(self):
        self.bowlingGame.startGame('11 11 11 11 11 11 11 11 11 9/1')
        self.bowlingGame.setRolls()
        score = self.bowlingGame.getScore()
        self.assertEqual(29, score)
            
    def testOnePinDownAndStrikeInFirstRoll(self):
        self.bowlingGame.startGame('X 11 11 11 11 11 11 11 11 11')
        self.bowlingGame.setRolls()
        score = self.bowlingGame.getScore()
        self.assertEqual(30, score)
    
    def testOnePinDownAndStrikeInLastRoll(self):
        self.bowlingGame.startGame('11 11 11 11 11 11 11 11 11 X11')
        self.bowlingGame.setRolls()
        score = self.bowlingGame.getScore()
        self.assertEqual(30, score)
    
    def testGoldenGame(self):
        self.bowlingGame.startGame('X X X X X X X X X X X X')
        self.bowlingGame.setRolls()
        score = self.bowlingGame.getScore()
        self.assertEqual(300, score)
            
    def testTenPairsOfNineAndMiss(self):
        self.bowlingGame.startGame('9- 9- 9- 9- 9- 9- 9- 9- 9- 9-')
        self.bowlingGame.setRolls()
        score = self.bowlingGame.getScore()
        self.assertEqual(90, score)
            
    def testTenPairsOfFive(self):
        self.bowlingGame.startGame('5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5')
        self.bowlingGame.setRolls()
        score = self.bowlingGame.getScore()
        self.assertEqual(150, score)

if __name__ == "__main__":
    unittest.main()
