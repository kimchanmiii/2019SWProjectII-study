기존의 코드는 행맨게임이 끝나면 NewGame버튼을 눌러서 새로 게임을 시작했다면, 이번 코드에서 개선한 점은 게임이 끝남과 동시에 사용자에게 게임을 더 진행할건지 묻는 방식이다.
게임이 끝나면 결과가 화면에 보여지고, 게임을 더 할건지 그만 할건지 사용자에게 묻는다.
사용자가 "Yes"를 고르면 게임이 리셋되면서 다시 시작하고, 
사용자가 "No"를 고르면 게임은 종료된다.
이전 코드보다 이번 코드가 더 편리한점은 사용자가 게임이 하기싫은 경우, 직접 종료하지 않아도 된다는 점이다. 
사용자가 "No"를 선택함으로써 게임은 자동으로 종료된다. 
이 코드를 실행시키기 위해서 게임이 종료되었때 게임을 진행할 것인지 선택할 수 있는 창을 띄우도록 연결해준다.

        if self.guess.finished():
            # 메시지 ("Success!") 출력하고, self.gameOver 는 False 로
            self.message.setText('Success!')
            #실행창으로 연결
            self.showWin()
            self.gameOver = False
        elif self.hangman.getRemainingLives() == 0:
            # 메시지 ("Fail!" + 비밀 단어) 출력하고, self.gameOver 는 False 로
            self.message.setText('Fail!  ' + self.guess.getSecretWord())
            #실행창으로 연결
            self.showLose()
            self.gameOver = False
      
이를 연결했으면, 각 창에서 선택하도록하는 화면을 실행시켜준다.

    # 이기면 더 할건지 창 띄우기
    def showWin(self):
        items = ('Yes', 'No')
        item, ok = QInputDialog.getItem(self, 'You Win! Play again?', 'Choice:', items, 0, False)
        if ok and item == 'Yes':
            self.startGame()
        else:
            QCoreApplication.instance().quit()

    # 지면 더 할건지 창 띄우기
    def showLose(self):
        items = ('Yes', 'No')
        item, ok = QInputDialog.getItem(self, 'You Lost! Play again?', 'Choice:', items, 0, False)
        if ok and item == 'Yes':
            self.startGame()
        else:
            QCoreApplication.instance().quit()
            
 결과창을 보여줌과 동시에 더 할건지 그만 할건지 물어보면서, 더하고싶다면 다시 startGame()으로 연결시켜준다.
 게임을 그만둔다는 선택을 할 경우, quit()를 사용해 게임을 종료해준다.
