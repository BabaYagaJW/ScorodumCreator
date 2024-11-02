import json
import os
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow


from Gui_Form.test_form_2 import Ui_Dialog
from Logic_Gui_Question.Setting_Quest import SettingQuest
from NewLogicTest import MainLogic
from Sctrure_Json import JsonStruct


class QuestionLogic():

    def __init__(self, list, round_dict, type_round, count_item_round, save_main_settings):
        super().__init__()

        self.window = QtWidgets.QMainWindow()
        self.quest_logic = Ui_Dialog()
        self.main_logic = MainLogic()
        self.quest_logic.setupUi(self.window)
        self.window.show()
        self.window.closeEvent = self.closeEvent

        self.quest_logic.Add_Quest.clicked.connect(self.on_add_question)
        self.quest_logic.Del_Quest.clicked.connect(self.on_del_question)
        self.quest_logic.All_Question.doubleClicked.connect(self.on_click_question)

        self.list_round_main = list
        self.list_quest = []
        self.quest_dict = {}
        self.result_dict = {}
        self.count_item_round = count_item_round
        self.type_round = type_round
        self.round_dict = round_dict
        self.save_main_settings = save_main_settings
        self.blitz_counter = 0

        if type_round == "Тестовый раунд":
            print('Открыт тестовый раунд')
        elif type_round == "Блитц раунд":
            print('Открыт блитц раунд')
            self.quest_logic.Type_Quest.clear()
            self.quest_logic.Type_Quest.addItem("text")
            self.quest_logic.Type_Quest.setEnabled(False)
        else:
            print('Открыт обычный раунд')


    def show_new_window(self, list, round_dict, type_round, count_item_round):
        self.window = QuestionLogic(list, round_dict, type_round, count_item_round)

    # Кнопка добавления вопроса
    def on_add_question(self):
        if self.quest_logic.Type_Quest.currentText() == "select":
            self.quest_logic.All_Question.insertItem(self.quest_logic.All_Question.count(),
                                                  "С выбором ответа")
        else:
            self.quest_logic.All_Question.insertItem(self.quest_logic.All_Question.count(),
                                                  "Свободный ответ")

        self.save_question_settings()

    # Кнопка удаления вопроса
    def on_del_question(self):
        list_items = self.quest_logic.All_Question.selectedItems()
        self.count_question = self.main_logic.ui.All_Round.currentRow()
        if not list_items: return
        for item in list_items:
            self.quest_logic.All_Question.takeItem(self.quest_logic.All_Question.row(item))
            #self.quest_dict.pop([count_items][self.count_question])
        print("Вопрос удален")

    def on_click_question(self):
        SettingQuest.show_new_window(self, self.quest_logic.All_Question.currentItem().text())

    def save_question_settings(self):
        if self.type_round == "Блитц раунд":
            z = JsonStruct.JsonStruct.structure_blitz_question(self,
                                                self.blitz_counter,
                                                "test",
                                                "test")

            self.list_quest.append(z)

            self.blitz_counter += 1

            if not bool(self.quest_dict.get(self.count_item_round)):
                self.quest_dict[self.count_item_round] = list(z)
            else:
                self.quest_dict.update({self.count_item_round: self.list_quest})
        else:
            z = JsonStruct.JsonStruct.structure_question_settings(self,
                                                       "test",
                                                       "test",
                                                       "test",
                                                       "test",
                                                       "test",
                                                       "test",
                                                       "test")

            self.list_quest.append(z)

            if not bool(self.quest_dict.get(self.count_item_round)):
                self.quest_dict.update({self.count_item_round: self.list_quest})
            else:
                self.quest_dict.update({self.count_item_round: self.list_quest})




    def closeEvent(self, event):
        print(self.quest_dict)
        self.list_quest = []
        print("Закрытие настройки раунда")
        self.main_logic.save_settings_question(self.quest_dict, self.round_dict)