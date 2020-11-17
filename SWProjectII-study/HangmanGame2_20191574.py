import unittest

from hangman import Hangman
from word import Word
from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.h1=Hangman()
        self.w1=Word('words.txt')
        self.g1 = Guess('default')


    def tearDown(self):
        pass


    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u l t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a d e l n t u ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l n t u ')

    def testDecreaseLife(self):
        i= self.h1.remainingLives
        self.h1.decreaseLife()
        self.assertTrue(i==self.h1.remainingLives+1)

    def testCurrentShape(self):
        while 0<self.h1.remainingLives:
            self.assertEqual(self.h1.currentShape(), self.h1.text[self.h1.remainingLives])
            self.h1.remainingLives-=1
    def testRandFromDB(self):
        for i in range(100):
            self.assertTrue(self.w1.randFromDB() in self.w1.words)


if __name__ == '__main__':
    unittest.main()
