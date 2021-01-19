from playsound import playsound
import question_interface
from examples import *
from login_interface import *
import random
import sys
from Main_interface import *
import score


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
        self.M1 = FirstApp(question[0])
        self.M2 = FirstApp(question[1])
        self.M3 = FirstApp(question[2])
        self.M4 = Score()
        self.layout.addWidget(self.M1)
        self.layout.addWidget(self.M2)
        self.layout.addWidget(self.M3)
        self.layout.addWidget(self.M4)
        self.layout.setCurrentWidget(self.M1)
        self.M1.pushButton.clicked.connect(self.toM2)
        self.M2.pushButton.clicked.connect(self.toM3)
        self.M3.pushButton.clicked.connect(self.toM4)
        self.cpt = 0

    def toM2(self):
        if self.M1.radioButton.isChecked():
            self.cpt += 1
        self.layout.setCurrentWidget(self.M2)
        self.showMaximized()

    def toM3(self):
        if self.M2.radioButton.isChecked():
            self.cpt += 1
        self.layout.setCurrentWidget(self.M3)
        self.showMaximized()

    def toM4(self):
        if self.M3.radioButton.isChecked():
            self.cpt += 1
        self.M4.label_2.setText(str(self.cpt)+"/03")
        self.layout.setCurrentWidget(self.M4)
        self.showMaximized()


class Score(QtWidgets.QMainWindow, score.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Score, self).__init__(parent)
        self.setupUi(self)
        self.score = 0


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


def module_Answers(sel module):
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
