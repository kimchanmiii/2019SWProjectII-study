이번 행맨게임은 기존에 만들었던 코드를 GUI방식으로 실행시켜주는 것이다.
먼저 행맨 디스플레이 모습을 설정해준다. 

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize word database        
        self.word = Word('words.txt')

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        self.charInput.returnPressed.connect(self.guessButton.click)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)
        
 행맨게임이 실행됐을때 화면의 위치, 그 화면 안에서의 행맨그림과 단어를 입력하는 칸, 이미 입력이 된 단어들이 들어간 칸, 등 모든 화면의 레이아웃을 설정해준다. 
 이런 화면 모습들을 모두 설정해주고나면, 이전에 게임을 실행할 때 하던 코드와 비슷하게 만들어주면 된다. 
 
 이전 코드와 크게 달라진게 있다면 GUI를 실행시켜주고 원래는 실행결과창에서 하던 게임을 GUI에서 할 수 있도록 만들어주면 된다. 
 위의 설정을 모두 완료해주고 그 전의 게임실행코드와 잘 이어준다면, GUI행맨 게임은 완성된다.
