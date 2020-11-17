행맨게임은 기존에 많이 알려졌다 싶이 정해진 단어를 맞추는 게임이다. 
같은 디렉토리에 많은 단어들이 적힌 파일을 넣어주고, 거기에 해당되는 단어를 맞추면 된다.
글자를 하나 넣었을 때, 맞췄을 경우엔 밑줄에 해당 글자가 입력되고,
틀렸을 경우엔 행맨의 그림이 하나씩 그려지면서 기회는 한번 줄어들게 된다. 
앞에서는 이 게임을 실행시키는 코드를 구현했다면, 이번 코드는 단위테스트 코드를 구현하였다.
단위테스트란, 모듈이나 애플리케이션 안에 있는 개별적인 코드 단위가 예상대로 작동하는지 확인하는 반복적인 행위이다.

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

위의 코드가 단위테스트를 실행시킨 코드이다.
이 코드를 실행시키면 아래와 같은 결과가 출력된다.

19184 words in DB
..19184 words in DB
19184 words in DB
.19184 words in DB
.19184 words in DB
.
----------------------------------------------------------------------
Ran 5 tests in 0.057s

OK

이는 코드에 적혀있는 코드가 실행되는데에 걸린시간이 0.057초 라는 뜻이다. 
위와 같이 코드가 출력된다면 코드가 올바르게 작성됐다는 의미이다. 
