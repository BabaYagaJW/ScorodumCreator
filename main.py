import sys
import json

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from Gui_Form.ui_main import Ui_MainWindow
from Gui_Form.ui_question_round import Ui_Ques_Round


class JSONTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui_quest = Ui_Ques_Round()
        self.ui.setupUi(self)
        #self.ui.Save_json.clicked.connect(self.on_save_json)
        self.ui.Add_Round.clicked.connect(self.on_add_round)
        self.ui.Del_Round.clicked.connect(self.on_del_round)
        self.ui.All_Round.doubleClicked.connect(self.on_double_click_round)
        #self.ui.tabWidget.currentChanged.connect(self.tabChanged)
        self.round_count = 0
        self.quest_select_count = 0
        self.quest_text_count = 0
        self.count_round = 0


    def on_double_click_round(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_quest.setupUi(self.window)
        self.window.show()
        self.ui_quest.Add_Quest.clicked.connect(self.on_add_question)
        self.ui_quest.Del_Quest.clicked.connect(self.on_del_question)

    def on_add_question(self):
        if self.ui_quest.Type_Quest.currentText() == "select":
            self.quest_select_count += 1
            self.ui_quest.All_Question.insertItem(self.ui_quest.All_Question.count(),
                                                  "Вопрос вариант ответа " + str(self.quest_select_count))
        else:
            self.quest_text_count += 1
            self.ui_quest.All_Question.insertItem(self.ui_quest.All_Question.count(),
                                                  "Свободный ответ " + str(self.quest_text_count))

    def on_del_question(self):
        print("del")
        list_items = self.ui_quest.All_Question.selectedItems()
        if not list_items: return
        for item in list_items:
            self.ui_quest.All_Question.takeItem(self.ui_quest.All_Question.row(item))

    def on_add_round(self):
        print(self.ui.All_Round.count())


        if self.ui.Type_Round.currentText() == "classical":
            if self.ui.Test_Round.isChecked():
                self.ui.All_Round.insertItem(0, "Тестовый раунд")
            else:
                self.round_count += 1
                self.ui.All_Round.insertItem(self.ui.All_Round.count(), "Раунд " + str(self.round_count))
        else:
            self.ui.All_Round.insertItem(self.ui.All_Round.count(), "Блитц Раунд")

    def on_del_round(self):
        list_items = self.ui.All_Round.selectedItems()
        if not list_items: return
        for item in list_items:
            self.ui.All_Round.takeItem(self.ui.All_Round.row(item))
            self.round_count -= 1

    #def on_save_json(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JSONTest()
    window.show()

    app.exec()
