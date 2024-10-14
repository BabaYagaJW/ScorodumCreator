import sys
import json
from xml.etree.ElementPath import xpath_tokenizer

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from Gui_Form.ui_main import Ui_MainWindow
from Gui_Form.ui_question_round import Ui_Ques_Round
from Sctrure_Json.Json_Sctruct import work_to_json


class Logic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui_quest = Ui_Ques_Round()
        self.w_json = work_to_json()
        self.ui.setupUi(self)
        self.ui.Add_Round.clicked.connect(self.on_add_round)
        self.ui.Del_Round.clicked.connect(self.on_del_round)
        self.ui.All_Round.doubleClicked.connect(self.on_double_click_round)
        self.ui.Save_json.clicked.connect(self.on_save_json)
        self.ui.tabWidget.currentChanged.connect(self.tabChanged)
        self.round_count = 0
        self.quest_select_count = 0
        self.list_round = []
        self.count_question = 0
        self.count_round = 0

    def tabChanged(self):
        if self.ui.tabWidget.currentIndex() == 1:
            #print("1")
            x = self.structure_main_settings()
            with open("test.json", "w") as f:
                json.dump(x, f, indent=4)
            print("correct")

        else:
            pass#print(self.save_round_settings())

    #Двойное нажатие и открытие меню с каждым раундом
    def on_double_click_round(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_quest.setupUi(self.window)
        self.window.show()
        self.ui_quest.Add_Quest.clicked.connect(self.on_add_question)
        self.ui_quest.Del_Quest.clicked.connect(self.on_del_question)

    #Кнопка добавления вопроса
    def on_add_question(self):
        if self.ui_quest.Type_Quest.currentText() == "select":
            self.quest_select_count += 1
            self.ui_quest.All_Question.insertItem(self.ui_quest.All_Question.count(),
                                                  "Вопрос вариант ответа " + str(self.quest_select_count))
        else:
            self.quest_text_count += 1
            self.ui_quest.All_Question.insertItem(self.ui_quest.All_Question.count(),
                                                  "Свободный ответ " + str(self.quest_text_count))

        self.save_question_settings()

    #Кнопка удаления вопроса
    def on_del_question(self):
        print("del")
        list_items = self.ui_quest.All_Question.selectedItems()
        if not list_items: return
        for item in list_items:
            self.ui_quest.All_Question.takeItem(self.ui_quest.All_Question.row(item))


    #Кнопка добавления раунда
    def on_add_round(self):
        #print(self.ui.All_Round.count())


        if self.ui.Type_Round.currentText() == "classical":
            if self.ui.Test_Round.isChecked():
                self.ui.All_Round.insertItem(0, "Тестовый раунд")
            else:
                self.round_count += 1
                self.ui.All_Round.insertItem(self.ui.All_Round.count(), "Раунд " + str(self.round_count))
        else:
            self.ui.All_Round.insertItem(self.ui.All_Round.count(), "Блитц Раунд")

        self.save_round_settings()


    #Кнопка удаления раунда
    def on_del_round(self):
        list_items = self.ui.All_Round.selectedItems()
        if not list_items: return
        for item in list_items:
            self.ui.All_Round.takeItem(self.ui.All_Round.row(item))
            self.round_count -= 1

    def on_save_json(self):
        print(self.ui.Name_Game.text())
        print("test")
        self.structure_main_settings()

    def structure_main_settings(self):
        structure_main = {
            "game": {
                "game_info": {
                    "name": self.ui.Name_Game.text(),
                    "theme": self.ui.Theme_Game.text(),
                    "client": self.ui.Client_Game.text(),
                    "date": self.ui.Date_Game.text(),
                },
                "game_settings": {
                    "tactics": {
                        "remove_answer": self.ui.remove_answer.value(),
                        "one_for_all": self.ui.one_for_all.value(),
                        "question_bet": self.ui.question_bet.value(),
                        "all_in": self.ui.all_in.value(),
                        "team_bet": self.ui.team_bet.value()
                    },
                    "skip_emails": self.ui.Mail_OnClick.isChecked()
                }
            }
        }

        return structure_main


    def structure_round_settings(self):
        structure_answer = {
            "rounds": []
        }

        return structure_answer


    def save_round_settings(self):
        x = self.structure_main_settings()
        y = self.structure_round_settings()
        z = self.structure_question_settings()

        if self.ui.Test_Round.isChecked():
            self.list_round.insert(0, z)

        else:
            self.list_round.append(z)
            
        print(self.list_round)     

        y["rounds"].append(self.list_round)

        x["game"].update(y)

        with open("test.json", "w") as f:
                json.dump(x, f, indent=4)


    def del_round_settings(self):
        x = self.structure_main_settings()
        y = self.structure_round_settings()
        z = self.structure_question_settings()
        


    def save_question_settings(self):
        pass








    def structure_question_settings(self):
        structure_settings_round = {
            "type": self.ui.Type_Round.currentText(),
            "settings": {
                "is_test": self.ui.Test_Round.isChecked(),
                "name": "round_name",
                "display_name": False,
                "time_to_answer": self.ui.Second_Round.value(),
                "use_special_tactics": True
            }
        }

        return structure_settings_round

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Logic()
    window.show()

    app.exec()
