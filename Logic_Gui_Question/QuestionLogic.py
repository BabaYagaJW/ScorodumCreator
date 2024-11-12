import json
import os
import sys
from ast import Index

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from Gui_Form.test_form import Ui_Test_Form
from Gui_Form.test_form_2 import Ui_Dialog
from Logic_Gui_Question.Setting_Quest import SettingQuest
from NewLogicTest import MainLogic
from Sctrure_Json import JsonStruct


class QuestionLogic():

    def __init__(self, list, quest_dict, round_dict, type_round, count_item_round, save_main_settings, second_round, del_quest_dict):
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

        self.second_round = second_round
        self.list_round_main = list
        self.quest_dict = quest_dict
        self.list_quest = []
        self.del_quest_dict = del_quest_dict
        self.result_dict = {}
        self.count_item_round = count_item_round
        self.type_round = type_round
        self.round_dict = round_dict
        self.save_main_settings = save_main_settings
        self.blitz_counter = 0
        self.Type_Quest = ""
        self.quest_text = ""
        self.First_Choise = ""
        self.Two_Choise = ""
        self.Third_Choise = ""
        self.Fourth_Choise = ""
        self.correct_answer = ""

        if type_round == "Тестовый раунд":
            print('Открыт тестовый раунд')
        elif type_round == "Блитц раунд":
            print('Открыт блитц раунд')
            self.quest_logic.Type_Quest.clear()
            self.quest_logic.Type_Quest.addItem("text")
            self.quest_logic.Type_Quest.setEnabled(False)
        else:
            print('Открыт обычный раунд')

        #исправлено
        self.all_vision_question()

    def show_new_window(self, list, round_dict, type_round, count_item_round):
        self.window = QuestionLogic(list, round_dict, type_round, count_item_round)

    def all_vision_question(self):
        self.quest_logic.All_Question.clear()
        if self.quest_dict.get(self.count_item_round):
            for i in self.quest_dict.get(self.count_item_round):
                if i.get("type") == "select":
                    self.quest_logic.All_Question.insertItem(self.quest_logic.All_Question.count(), "С выбором ответа")
                else:
                    self.quest_logic.All_Question.insertItem(self.quest_logic.All_Question.count(), "Свободный ответ")
            self.list_quest = self.quest_dict.get(self.count_item_round)

    # Кнопка добавления вопроса
    def on_add_question(self):
        if self.quest_logic.Type_Quest.currentText() == "select":
            self.quest_logic.All_Question.insertItem(self.quest_logic.All_Question.count(),
                                                  "С выбором ответа")
        else:
            self.quest_logic.All_Question.insertItem(self.quest_logic.All_Question.count(),
                                             "Свободный ответ")

    # Кнопка удаления вопроса (исправить, чтоб удалял и пустые строки, а не выдавал ошибку)
    def on_del_question(self):
        list_items = self.quest_logic.All_Question.selectedItems()
        count_question = self.quest_logic.All_Question.currentRow()
        if not list_items: return
        for item in list_items:
                self.quest_logic.All_Question.takeItem(self.quest_logic.All_Question.row(item))
                del(self.quest_dict[self.count_item_round][count_question])
        print("Вопрос удален")

    def on_click_question(self):
        self.window_quest = QtWidgets.QMainWindow()
        self.ui_question = Ui_Test_Form()
        self.ui_question.setupUi(self.window_quest)
        self.window_quest.show()
        #self.window_quest.closeEvent = self.closeEvent

        self.ui_question.One_Correct.clicked.connect(self.on_one_correct)
        self.ui_question.Two_Correct.clicked.connect(self.on_two_correct)
        self.ui_question.Three_Correct.clicked.connect(self.on_three_correct)
        self.ui_question.Fourth_Correct.clicked.connect(self.on_fourth_correct)
        self.ui_question.Save_Question.clicked.connect(self.save_question_settings)

        self.Type_Quest = ""
        self.quest_text = ""
        self.First_Choise = ""
        self.Two_Choise = ""
        self.Third_Choise = ""
        self.Fourth_Choise = ""
        self.correct_answer = ""

        if self.quest_logic.All_Question.currentItem().text() == "Свободный ответ":
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
            self.window_quest.resize(515, 200)
            self.ui_question.Save_Question.setGeometry(220, 160, 75, 24)

        self.ui_question.edit_type_quest.setVisible(False)
        self.ui_question.edit_label.setVisible(False)
        count_question = self.quest_logic.All_Question.currentRow()
        try:
            x = self.quest_dict[self.count_item_round][count_question]
            print(self.quest_dict)
        except KeyError:
            pass
        except IndexError:
            pass
        else:
            if self.type_round == "Блитц раунд":
                self.ui_question.quest_text.setText(x.get("question"))
                self.ui_question.First_Choise.setText(x.get("correct_answer"))
                self.ui_question.One_Correct.setChecked(True)
                self.ui_question.One_Correct.setEnabled(False)
            else:
                if self.quest_logic.All_Question.currentItem().text() == "Свободный ответ":
                    self.ui_question.edit_type_quest.setVisible(True)
                    self.ui_question.edit_label.setVisible(True)
                    self.ui_question.edit_label.setGeometry(251, 10, 70, 28)
                    self.ui_question.edit_type_quest.setGeometry(170, 10, 71, 28)
                    self.ui_question.label_23.setGeometry(50, 50, 70, 28)
                    self.ui_question.quest_text.setGeometry(110, 50, 311, 31)
                    self.ui_question.label_25.setGeometry(50, 130, 51, 28)
                    self.ui_question.One_Correct.setGeometry(440, 130, 51, 20)
                    self.ui_question.First_Choise.setGeometry(110, 130, 311, 22)
                    self.window_quest.resize(515, 210)
                    self.ui_question.Save_Question.setGeometry(220, 160, 75, 24)
                    self.ui_question.label_24.setGeometry(200, 90, 101, 28)
                    self.ui_question.label_29.setGeometry(400, 90, 111, 28)
                else:
                    self.window_quest.resize(515, 320)
                    self.ui_question.edit_type_quest.setVisible(True)
                    self.ui_question.edit_label.setVisible(True)
                    self.ui_question.edit_label.setGeometry(251, 10, 70, 28)
                    self.ui_question.edit_type_quest.setGeometry(170, 10, 71, 28)
                    self.ui_question.label_23.setGeometry(50, 50, 70, 28)
                    self.ui_question.quest_text.setGeometry(110, 50, 311, 31)
                    self.ui_question.label_24.setGeometry(200, 90, 101, 28)
                    self.ui_question.label_29.setGeometry(400, 90, 111, 28)
                    self.ui_question.label_25.setGeometry(50, 130, 51, 28)
                    self.ui_question.One_Correct.setGeometry(440, 130, 51, 20)
                    self.ui_question.First_Choise.setGeometry(110, 130, 311, 22)
                    self.ui_question.label_26.setGeometry(50, 170, 51, 28)
                    self.ui_question.Two_Choise.setGeometry(110, 170, 311, 22)
                    self.ui_question.Two_Correct.setGeometry(440, 170, 51, 20)
                    self.ui_question.label_27.setGeometry(50, 210, 51, 28)
                    self.ui_question.Third_Choise.setGeometry(110, 210, 311, 22)
                    self.ui_question.Three_Correct.setGeometry(440, 210, 51, 20)
                    self.ui_question.label_28.setGeometry(40, 250, 61, 28)
                    self.ui_question.Fourth_Correct.setGeometry(440, 250, 51, 20)
                    self.ui_question.Fourth_Choise.setGeometry(110, 250, 311, 22)
                    self.ui_question.Save_Question.setGeometry(210, 290, 75, 24)

                y = x.get("answers")

                print(y)
                if(x.get("type") == "select"):
                    self.ui_question.edit_type_quest.setItemText(0, x.get("type"))
                    self.ui_question.edit_type_quest.setItemText(1, "text")
                else:
                    self.ui_question.edit_type_quest.setItemText(0, x.get("type"))
                    self.ui_question.edit_type_quest.setItemText(1, "select")

                self.ui_question.quest_text.setText(x.get("question"))
                self.ui_question.First_Choise.setText(y[0])
                self.ui_question.Two_Choise.setText(y[1])
                self.ui_question.Third_Choise.setText(y[2])
                self.ui_question.Fourth_Choise.setText(y[3])

                if x.get("correct_answer") == y[0]:
                    self.ui_question.One_Correct.setChecked(True)
                    self.ui_question.Two_Correct.setEnabled(False)
                    self.ui_question.Three_Correct.setEnabled(False)
                    self.ui_question.Fourth_Correct.setEnabled(False)
                elif x.get("correct_answer") == y[1]:
                    self.ui_question.Two_Correct.setChecked(True)
                    self.ui_question.One_Correct.setEnabled(False)
                    self.ui_question.Three_Correct.setEnabled(False)
                    self.ui_question.Fourth_Correct.setEnabled(False)
                elif x.get("correct_answer") == y[2]:
                    self.ui_question.Three_Correct.setChecked(True)
                    self.ui_question.Two_Correct.setEnabled(False)
                    self.ui_question.One_Correct.setEnabled(False)
                    self.ui_question.Fourth_Correct.setEnabled(False)
                else:
                    self.ui_question.Fourth_Correct.setChecked(True)
                    self.ui_question.Two_Correct.setEnabled(False)
                    self.ui_question.Three_Correct.setEnabled(False)
                    self.ui_question.One_Correct.setEnabled(False)

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

    def save_question_settings(self):
        count_question = self.quest_logic.All_Question.currentRow()

        try:
            x = self.quest_dict[self.count_item_round][count_question]
        except KeyError:
            if self.type_round == "Блитц раунд":
                z = JsonStruct.JsonStruct.structure_blitz_question(self.blitz_counter,
                                                                   self.ui_question.quest_text.text(),
                                                                   self.ui_question.First_Choise.text())
                self.list_quest.append(z)

                if not bool(self.quest_dict.get(self.count_item_round)):
                    self.quest_dict[self.count_item_round] = self.list_quest
                else:
                    self.quest_dict.update({self.count_item_round: self.list_quest})

                print(self.quest_dict)
                self.blitz_counter += 1
            else:
                if self.ui_question.One_Correct.isChecked():
                    self.correct_answer = self.ui_question.First_Choise.text()
                elif self.ui_question.Two_Correct.isChecked():
                    self.correct_answer = self.ui_question.Two_Choise.text()
                elif self.ui_question.Three_Correct.isChecked():
                    self.correct_answer = self.ui_question.Third_Choise.text()
                else:
                    self.correct_answer = self.ui_question.Fourth_Choise.text()

                z = JsonStruct.JsonStruct.structure_question_settings(self.quest_logic.Type_Quest.currentText(),
                                                                      self.ui_question.quest_text.text(),
                                                                      self.ui_question.First_Choise.text(),
                                                                      self.ui_question.Two_Choise.text(),
                                                                      self.ui_question.Third_Choise.text(),
                                                                      self.ui_question.Fourth_Choise.text(),
                                                                      self.correct_answer,
                                                                      self.second_round)

                self.list_quest.append(z)

                if not bool(self.quest_dict.get(self.count_item_round)):
                    self.quest_dict.update({self.count_item_round: self.list_quest})
                else:
                    self.quest_dict.update({self.count_item_round: self.list_quest})
        except IndexError:
            if self.type_round == "Блитц раунд":
                z = JsonStruct.JsonStruct.structure_blitz_question(self.blitz_counter,
                                                                   self.ui_question.quest_text.text(),
                                                                   self.ui_question.First_Choise.text())
                self.list_quest.append(z)

                if not bool(self.quest_dict.get(self.count_item_round)):
                    self.quest_dict[self.count_item_round] = dict(z)
                else:
                    self.quest_dict.update({self.count_item_round: self.list_quest})

                print(self.quest_dict)
                self.blitz_counter += 1
            else:
                if self.ui_question.One_Correct.isChecked():
                    self.correct_answer = self.ui_question.First_Choise.text()
                elif self.ui_question.Two_Correct.isChecked():
                    self.correct_answer = self.ui_question.Two_Choise.text()
                elif self.ui_question.Three_Correct.isChecked():
                    self.correct_answer = self.ui_question.Third_Choise.text()
                else:
                    self.correct_answer = self.ui_question.Fourth_Choise.text()

                z = JsonStruct.JsonStruct.structure_question_settings(self.quest_logic.Type_Quest.currentText(),
                                                                      self.ui_question.quest_text.text(),
                                                                      self.ui_question.First_Choise.text(),
                                                                      self.ui_question.Two_Choise.text(),
                                                                      self.ui_question.Third_Choise.text(),
                                                                      self.ui_question.Fourth_Choise.text(),
                                                                      self.correct_answer,
                                                                      self.second_round)

                self.list_quest.append(z)

                if not bool(self.quest_dict.get(self.count_item_round)):
                    self.quest_dict.update({self.count_item_round: self.list_quest})
                else:
                    self.quest_dict.update({self.count_item_round: self.list_quest})
        else:
            if self.type_round == "Блитц раунд":

                x["question"] = self.ui_question.quest_text.text()
                x["correct_answer"] = self.ui_question.First_Choise.text()
            else:
                y = x.get("answers")

                x["type"] = self.ui_question.edit_type_quest.currentText()
                print(x["type"])
                x["question"] = self.ui_question.quest_text.text()
                y[0] = self.ui_question.First_Choise.text()
                y[1] = self.ui_question.Two_Choise.text()
                y[2] = self.ui_question.Third_Choise.text()
                y[3] = self.ui_question.Fourth_Choise.text()
                if self.ui_question.One_Correct.isChecked():
                    x["correct_answer"] = self.ui_question.First_Choise.text()
                elif self.ui_question.Two_Correct.isChecked():
                    x["correct_answer"] = self.ui_question.Two_Choise.text()
                elif self.ui_question.Three_Correct.isChecked():
                    x["correct_answer"] = self.ui_question.Third_Choise.text()
                else:
                    x["correct_answer"] = self.ui_question.Fourth_Choise.text()

        self.window_quest.close()
        self.all_vision_question()

    def set_del_quest_round(self):
        pass

    def del_round(self, count_del_round):
            try:
                self.quest_dict.pop(count_del_round)
                for i in list(self.quest_dict):
                    print(i)
                    if i > count_del_round:
                        self.del_quest_dict[i - 1] = self.quest_dict[i]
                    else:
                        self.del_quest_dict[i] = self.quest_dict[i]

                self.quest_dict = dict(self.del_quest_dict)
                print(self.quest_dict)
            except KeyError:
                print("Раунд пустой")
                pass

    def closeEvent(self, event):
        for i in range(len(self.round_dict["rounds"])):
            print(i)
            if not i in self.quest_dict.keys():
                print("нет ключа")
                continue

            else:
                self.result_dict = {"questions": self.quest_dict[i]}
                self.round_dict["rounds"][i].update(self.result_dict)

        self.save_main_settings["game"].update(self.round_dict)
        file_path_credentials = os.path.join(os.path.dirname("ScorodumCreator"), "scenario.json")
        with open(file_path_credentials, "w", encoding='utf8') as f:
            json.dump(self.save_main_settings, f, indent=4, ensure_ascii=False)

        self.list_quest = []
