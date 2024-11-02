from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from Gui_Form.test_form import Ui_Test_Form



class SettingQuest():
    def __init__(self, type_question):
        super().__init__()

        self.window_quest = QtWidgets.QMainWindow()
        self.ui_question = Ui_Test_Form()
        self.ui_question.setupUi(self.window_quest)
        self.window_quest.show()
        self.window_quest.closeEvent = self.closeEvent

        self.ui_question.One_Correct.clicked.connect(self.on_one_correct)
        self.ui_question.Two_Correct.clicked.connect(self.on_two_correct)
        self.ui_question.Three_Correct.clicked.connect(self.on_three_correct)
        self.ui_question.Fourth_Correct.clicked.connect(self.on_fourth_correct)
        #self.ui_question.Save_Question.clicked.connect(self.on_save_question)

        if  type_question == "Свободный ответ":
            self.ui_question.label_26.setVisible(False)
            self.ui_question.label_27.setVisible(False)
            self.ui_question.label_28.setVisible(False)
            self.ui_question.Two_Choise.setVisible(False)
            self.ui_question.Two_Correct.setVisible(False)
            self.ui_question.Three_Correct.setVisible(False)
            self.ui_question.Third_Choise.setVisible(False)
            self.ui_question.Fourth_Correct.setVisible(False)
            self.ui_question.Fourth_Choise.setVisible(False)
            self.ui_question.One_Correct.setChecked(True)
            self.ui_question.One_Correct.setEnabled(False)
            self.window_quest.resize(515,200)
            self.ui_question.Save_Question.setGeometry(220,160,75, 24)

    def show_new_window(self, type_question):
        self.window_quest = SettingQuest(type_question)

    # Нажатие на кнопку с отметкой о правильном ответе

    def on_one_correct(self):
        if self.ui_question.One_Correct.isChecked():
            self.ui_question.Two_Correct.setEnabled(False)
            self.ui_question.Three_Correct.setEnabled(False)
            self.ui_question.Fourth_Correct.setEnabled(False)
        else:
            self.ui_question.Two_Correct.setEnabled(True)
            self.ui_question.Three_Correct.setEnabled(True)
            self.ui_question.Fourth_Correct.setEnabled(True)

    def on_two_correct(self):
        if self.ui_question.Two_Correct.isChecked():
            self.ui_question.One_Correct.setEnabled(False)
            self.ui_question.Three_Correct.setEnabled(False)
            self.ui_question.Fourth_Correct.setEnabled(False)
        else:
            self.ui_question.One_Correct.setEnabled(True)
            self.ui_question.Three_Correct.setEnabled(True)
            self.ui_question.Fourth_Correct.setEnabled(True)

    def on_three_correct(self):
        if self.ui_question.Three_Correct.isChecked():
            self.ui_question.Two_Correct.setEnabled(False)
            self.ui_question.One_Correct.setEnabled(False)
            self.ui_question.Fourth_Correct.setEnabled(False)
        else:
            self.ui_question.Two_Correct.setEnabled(True)
            self.ui_question.One_Correct.setEnabled(True)
            self.ui_question.Fourth_Correct.setEnabled(True)

    def on_fourth_correct(self):
        if self.ui_question.Fourth_Correct.isChecked():
            self.ui_question.Two_Correct.setEnabled(False)
            self.ui_question.Three_Correct.setEnabled(False)
            self.ui_question.One_Correct.setEnabled(False)
        else:
            self.ui_question.Two_Correct.setEnabled(True)
            self.ui_question.Three_Correct.setEnabled(True)
            self.ui_question.One_Correct.setEnabled(True)


    def closeEvent(self, event):
        print("Закрытие окна с настройками вопросов")