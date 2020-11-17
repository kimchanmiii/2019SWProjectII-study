import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        hbox = QHBoxLayout()

        # 각 버튼 label만들어주기
        label_Name = QLabel("Name:", self)
        label_Age = QLabel("Age:", self)
        label_Score = QLabel("Score:", self)
        label_Amount = QLabel("Amount:", self)
        label_Key = QLabel("Key:", self)
        label_Result = QLabel("Result:", self)
        button_Add = QPushButton("Add", self)
        button_Del = QPushButton("Del", self)
        button_Find = QPushButton("Find", self)
        button_Inc = QPushButton("Inc", self)
        button_Show = QPushButton("Show", self)

        # 각 label에 입력하는 칸 만들어주기
        self.line_Name = QLineEdit()
        self.line_Age = QLineEdit()
        self.line_Score = QLineEdit()
        self.line_Amount = QLineEdit()
        self.combo_Key = QComboBox()
        self.text_Result = QTextEdit()

        # label key 값에 선택3가지 추가해주기
        self.combo_Key.addItems(["Name", "Age", "Score"])

        # hbox => 가로의 구성 설정해주기
        # label 옆에 lineedit넣어주기
        hbox.addWidget(label_Name)
        hbox.addWidget(self.line_Name)
        hbox.addWidget(label_Age)
        hbox.addWidget(self.line_Age)
        hbox.addWidget(label_Score)
        hbox.addWidget(self.line_Score)

        # vbox => 세로의 구성 설정해주기
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1) # 세로로 길이 1칸 늘리기

        hbox = QHBoxLayout()
        hbox.addStretch(2)

        hbox.addWidget(label_Amount)
        hbox.addWidget(self.line_Amount)
        hbox.addWidget(label_Key)
        hbox.addWidget(self.combo_Key)

        vbox.addLayout(hbox)
        vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)

        hbox.addWidget(button_Add)
        hbox.addWidget(button_Del)
        hbox.addWidget(button_Find)
        hbox.addWidget(button_Inc)
        hbox.addWidget(button_Show)

        vbox.addLayout(hbox)
        vbox.addStretch(1)

        hbox = QHBoxLayout()

        hbox.addWidget(label_Result)
        hbox.addWidget(self.text_Result)

        vbox.addLayout(hbox)
        vbox.addStretch(1)

        hbox = QHBoxLayout()

        # 버튼이 눌렸을때의 상황 연결해주기 (밑에 다시나옴) - 이벤트함수 연결 
        button_Add.clicked.connect(self.button_Add_Clicked)
        button_Del.clicked.connect(self.button_Del_Clicked)
        button_Find.clicked.connect(self.button_Find_Clicked)
        button_Inc.clicked.connect(self.button_Inc_Clicked)
        button_Show.clicked.connect(self.showScoreDB)

        self.setLayout(vbox)

        # 창이 뜨는 위치 설정해주기
        self.setGeometry(300, 300, 500, 250) # (화면의 x좌표, 화면의 y좌표, 창의 가로길이, 창의 세로길이)
        self.setWindowTitle("Assignment6")
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, "wb")
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.text_Result.clear()
        self.DB = ""
        key = str(self.combo_Key.currentText())
        for j in sorted(self.scoredb, key = lambda person: person[key]):
            for attr in sorted(j):
                self.DB += attr + "=" + str(j[attr]) + "      "
                if attr == "Score":
                    self.text_Result.append((self.DB))
            self.DB += "\n"
        self.text_Result.setText(self.DB)

    #버튼이 눌렸을때의 상황 설정

    def button_Add_Clicked(self):
        try:
            nameText = self.line_Name.text()
            ageText = self.line_Age.text()
            scoreText = self.line_Score.text()
            if nameText == "":
                self.text_Result.setText("No name")
            elif int(ageText) > 0 and int(scoreText) >= 0:
                input = {"Name" : nameText, "Age" : int(ageText), "Score" : int(scoreText)}
                self.scoredb += [input]
                self.showScoreDB()
            else:
                self.text_Result.setTExt("Error: Please enter the positive number.")
        except ValueError:
            self.text_Result.setText("Error")

    def button_Del_Clicked(self):
        try:
            nameText = self.line_Name.text()
            if nameText == "":
                self.text_Result.setText("No name")
            else:
                for i in range(len(self.scoredb) // 2 + 1):
                    for j in self.scoredb:
                        while j["Name"] == nameText:
                            if j["Name"] == nameText:
                                self.scoredb.remove(j)
                                break
                self.showScoreDB()
        except:
            pass

    def button_Find_Clicked(self):
        self.text_Result.clear()
        nameText = self.line_Name.text()
        if nameText == "":
            self.text_Result.setText("No name")
        else:
            for j in self.scoredb:
                if j["Name"] == nameText:
                    result = ""
                    for k in sorted(j):
                        result += str(k) + "=" + str(j[k]) + "      "
                        if k == "Score":
                            self.text_Result.append((result))

    def button_Inc_Clicked(self):
        try:
            nameText = str(self.line_Name.text())
            amountText = int(self.line_Amount.text())
        except ValueError:
            self.text_Result.setText("Error")
        else:
            if nameText == "":
                self.text_Result.setText("No name")
            else:
                for j in self.scoredb:
                    if j["Name"] == nameText:
                        if j["Score"] + amountText < 0:
                            self.text_Result.setText("Please enter the positive number")
                        else:
                            j["Score"] = int(int(j["Score"]) + int(amountText))
                self.showScoreDB()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
