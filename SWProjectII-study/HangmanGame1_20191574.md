행맨게임은 기존에 많이 알려졌다 싶이 정해진 단어를 맞추는 게임이다. 
같은 디렉토리에 많은 단어들이 적힌 파일을 넣어주고, 거기에 해당되는 단어를 맞추면 된다.
글자를 하나 넣었을 때, 맞췄을 경우엔 밑줄에 해당 글자가 입력되고,
틀렸을 경우엔 행맨의 그림이 하나씩 그려지면서 기회는 한번 줄어들게 된다. 

    def guess(self, character):
        self.guessedChars.add(character)
        if character not in self.secretWord:
            self.numTries += 1
            return False
        for i in range(len(self.secretWord)):
            if self.secretWord[i] == character:
                self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i + 1:]
        if self.currentStatus!=self.secretWord:
            return False
        return True

위의 코드가 예제코드에서 발전시킨 코드이다. 
if문을 사용해서 글자가 단어에 포함되는 경우엔 해당단어를 입력해주고
포함되지 않는 경우엔 numTries가 하나씩 추가되는 코드를 구현했다. 
만약에 주어진 모든 기회를 사용했을 경우엔 실패라는 문구가 뜨면서 정답은 어떤 단어였는지 밝혀지게끔 코드를 만들었다.
이렇게 코드를 만들어주면 행맨게임이 완성된다.
이 guess.py코드를 완성시켜주고 game.py에서 실행시켜주면 행맨 게임이 시작된다.
