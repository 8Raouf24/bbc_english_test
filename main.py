from playsound import playsound
import question_interface
from examples import *
from login_interface import *
import random
import sys
from Main_interface import *
import score
from PyQt5 import QtPrintSupport


class LoginPage(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)
        self.setupUi(self)
        self.Login.clicked.connect(self.LoginRedirect)
        self.question = question

    def LoginRedirect(self):
        if self.ID.text() == "Admin" and self.Password.text() == "Admin":
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')


class menu(QtWidgets.QWidget):

    def __init__(self, question):
        super().__init__()
        self.showMinimized()
        self.layout = QtWidgets.QStackedLayout()
        self.setLayout(self.layout)
        self.showMaximized()
        self.M = []
        for i in range(len(question)):
            self.M.append(FirstApp(question[i]))
        self.S = Score()
        for i in range(len(self.M)):
            self.layout.addWidget(self.M[i])
        self.layout.addWidget(self.S)
        self.layout.setCurrentWidget(self.M[0])
        self.M[0].pushButton.clicked.connect(lambda: self.toM(1))
        self.M[1].pushButton.clicked.connect(lambda: self.toM(2))
        self.M[2].pushButton.clicked.connect(lambda: self.toM(3))
        self.M[3].pushButton.clicked.connect(lambda: self.toM(4))
        self.M[4].pushButton.clicked.connect(lambda: self.toM(5))
        self.M[5].pushButton.clicked.connect(lambda: self.toM(6))
        self.M[6].pushButton.clicked.connect(lambda: self.toM(7))
        self.M[7].pushButton.clicked.connect(lambda: self.toM(8))
        self.M[8].pushButton.clicked.connect(lambda: self.toM(9))
        """for  in range(len(self.M)-1):
            self.M[i].pushButton.clicked.connect(lambda: self.toM(i+1))"""
        self.M[len(self.M)-1].pushButton.clicked.connect(self.toS)
        self
        self.cpt = 0

    def toM(self, i):
        # if self.M1.radioButton.isChecked():
        #    self.cpt += 1
        key = list(question[i-1].keys())[0]
        quest = question[i-1][key][0]
        answers = question[i-1][key][1]
        if self.M[i-1].radioButton.isChecked():
            ans = 0
        if self.M[i-1].radioButton_2.isChecked():
            ans = 1
        if self.M[i-1].radioButton_3.isChecked():
            ans = 2
        if self.M[i-1].radioButton_4.isChecked():
            ans = 3
        self.cpt = self.cpt + answers[ans][1]
        self.layout.setCurrentWidget(self.M[i])
        self.showMaximized()

    def toS(self):
        # if self.M1.radioButton.isChecked():
        #    self.cpt += 1
        i = len(self.M) - 1
        key = list(question[i-1].keys())[0]
        quest = question[i-1][key][0]
        answers = question[i-1][key][1]
        if self.M[i-1].radioButton.isChecked():
            ans = 0
        if self.M[i-1].radioButton_2.isChecked():
            ans = 1
        if self.M[i-1].radioButton_3.isChecked():
            ans = 2
        if self.M[i-1].radioButton_4.isChecked():
            ans = 3
        self.cpt = self.cpt + answers[ans][1]
        self.S.label_2.setText(str(self.cpt) + "/10")
        self.layout.setCurrentWidget(self.S)
        self.showMaximized()


class Score(QtWidgets.QMainWindow, score.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Score, self).__init__(parent)
        self.setupUi(self)
        self.Button.clicked.connect(self.print_widget)

    def print_widget(self):
        # Create printer
        printer = QtPrintSupport.QPrinter()
        # Create painter
        painter = QtGui.QPainter()
        # Start painter
        painter.begin(printer)
        # Grab a widget you want to print
        screen = self.grab()
        # Draw grabbed pixmap
        painter.drawPixmap(10, 10, screen)
        # End painting
        painter.end()


class FirstApp(QtWidgets.QMainWindow, question_interface.Ui_MainWindow):
    def __init__(self, question, parent=None):
        super(FirstApp, self).__init__(parent)
        self.setupUi(self)
        self.question = question
        key = list(question.keys())[0]
        quest = self.question[key][0]
        answers = self.question[key][1]
        self.change_header_Text(key)
        self.change_Question_Text(quest)
        """ if i == "Compréhension Orale":
            pass """
        # print('possible answers : ')
        self.change_Answers(answers)
        # wait
        # answer = input("what's is your answer: ")
        # return answers[int(answer)-1][1]

    def change_header_Text(self, string):
        self.label.setText(string)

    def change_Header_Text(self, string):
        self.label.setText(string)

    def change_Question_Text(self, string):
        self.label_2.setText(string)

    def change_Answers(self, answers):
        self.radioButton.setText(answers[0][0])
        self.radioButton_2.setText(answers[1][0])
        self.radioButton_3.setText(answers[2][0])
        self.radioButton_4.setText(answers[3][0])

    """def answer_question(self, question):
        question = self.question
        key = list(question.keys())[0]
        quest = question[key][0]
        answers = question[key][1]
        self.change_header_Text(key)
        self.change_Question_Text(quest)
         if i == "Compréhension Orale":
            pass
        # print('possible answers : ')
        self.change_Answers(answers)
        # wait
        # answer = input("what's is your answer: ")
        # return answers[int(answer)-1][1]"""

    """def module_Answers(self, module):
        questions = list(module.values())[0]
        score = 0
        for i in questions:
            score = score + answer_question(i, ui)
        return score"""

    """def run_exam(self, corpus):
        for i in list(corpus.keys()):
            _temp = {i: corpus[i]}
            module_Answers(_temp, ui)"""


def fetch_questions(corpus, Number):  # returns a reduced dic with the same structure
    _corpus = {list(corpus.keys())[i]: random.sample(
        corpus[list(corpus.keys())[i]], k=Number) for i in range(3)}
    return _corpus

# returns the score of one question that it takes as input.


def answer_question(question):
    key = list(question.keys())[0]
    quest = question[key][0]
    answers = question[key][1]
    print(key)
    ui.change_header_Text(key)
    print(quest)
    """ if i == "Compréhension Orale":
        pass """
    print('possible answers : ')
    for i in answers:
        print(i[0])
    # wait
    answer = input("what's is your answer: ")
    return answers[int(answer)-1][1]


def module_Answers(sel, module):
    questions = list(module.values())[0]
    score = 0
    for i in questions:
        score = score + answer_question(i, ui)
    return score


def run_exam(corpus, ui):
    for i in list(corpus.keys()):
        _temp = {i: corpus[i]}
        module_Answers(_temp, ui)


app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
login = LoginPage()
# ui = FirstApp(MainWindow, question)
if login.exec_() == QtWidgets.QDialog.Accepted:
    window = menu(question)
    window.show()
    sys.exit(app.exec_())
sys.exit(app.exec_())
sys.exit(app.exec_())


# print(fetch_questions(corpus, 2))
# print(answer_question(question))
# run_exam(corpus, ui)
