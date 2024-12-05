import json
import os

from PySide6 import QtWidgets
from Gui_Form.form_round import Ui_form_round
from Logic_Gui_Question.QuestionLogic import QuestionLogic
from NewLogicTest import MainLogic
from Sctrure_Json.JsonStruct import JsonStruct


class RoundLogic:
        def __init__(self, list_round, link, quest_dict, count_item_round, count_double_round, round_dict, save_main_settings, method_on_click, text_round):
            """

            :type self: object
            """

            self.link_main = link
            self.round_link = self
            self.window = QtWidgets.QMainWindow()
            self.round_gui = Ui_form_round()
            self.round_gui.setupUi(self.window)
            self.round_gui.Blitz_label.setEnabled(False)
            self.round_gui.Blitz_Score.setEnabled(False)
            self.window.closeEvent = self.closeEvent

            self.window.show()

            #слушатели
            self.round_gui.Add_Quest.clicked.connect(self.on_add_quest)
            self.round_gui.Del_Quest.clicked.connect(self.on_del_quest)
            self.round_gui.Type_Round.currentTextChanged.connect(self.on_type_round)
            self.round_gui.All_Question.doubleClicked.connect(self.on_double_click_quest)

            self.result_dict = {}
            self.list_round = list_round
            self.quest_dict = quest_dict
            self.list_quest = []
            self.count_item_round = count_item_round
            self.round_dict = round_dict
            self.save_main_settings = save_main_settings
            self.count_double_round = count_double_round
            self.method_on_click = method_on_click

            if method_on_click == 'doubleclick':
                self.all_vision_question()
                if text_round == "Блитц раунд":
                    self.round_gui.Type_Round.setItemText(0, "blitz")
                    self.round_gui.Type_Round.setItemText(1, "classical")
                    self.round_gui.Test_Round.setChecked(False)
                elif text_round == "Тестовый раунд":
                    self.round_gui.Type_Round.setItemText(0, "classical")
                    self.round_gui.Type_Round.setItemText(1, "blitz")
                    self.round_gui.Test_Round.setChecked(True)
                else:
                    self.round_gui.Type_Round.setItemText(0, "classical")
                    self.round_gui.Type_Round.setItemText(1, "blitz")
                    self.round_gui.Test_Round.setChecked(False)

        def on_add_quest(self):
            window_quest = QuestionLogic(self.quest_dict,
                                       self.round_link,
                                        self.round_gui.Type_Round.currentText(),
                                        self.count_item_round,
                                        self.count_double_round,
                                        self.round_gui.All_Question.count(),
                                        self.list_quest,
                                        self.round_gui.Second_Round.value(),
                                        self.round_gui.All_Question.currentRow(),
                                        "addquestion")


        def show_question(self):
            self.round_gui.All_Question.clear()
            if self.quest_dict.get(self.count_double_round):
                for i in self.quest_dict.get(self.count_double_round):
                    if i.get("type") == "select":
                        self.round_gui.All_Question.insertItem(self.round_gui.All_Question.count(),
                                                                 "С выбором ответа")
                    else:
                        self.round_gui.All_Question.insertItem(self.round_gui.All_Question.count(),
                                                                 "Свободный ответ")


        def on_double_click_quest(self):
            window_quest = QuestionLogic(self.quest_dict,
                                       self.round_link,
                                       self.round_gui.Type_Round.currentText(),
                                       self.count_item_round,
                                       self.count_double_round,
                                       self.round_gui.All_Question.count(),
                                       self.list_quest,
                                       self.round_gui.Second_Round.value(),
                                       self.round_gui.All_Question.currentRow(),
                                       "doubleclick")

        def on_type_round(self):
            if self.round_gui.Type_Round.currentText() == "classical":
                self.round_gui.Blitz_label.setEnabled(False)
                self.round_gui.Blitz_Score.setEnabled(False)
                self.round_gui.Test_Round.setEnabled(True)
                self.round_gui.Second_Round.setValue(50)
            else:
                self.round_gui.Blitz_label.setEnabled(True)
                self.round_gui.Second_Round.setValue(180)
                self.round_gui.Test_Round.setEnabled(False)
                self.round_gui.Blitz_Score.setEnabled(True)

        def on_del_quest(self):
            pass

        def save_round_settings(self):
            if self.round_gui.Type_Round.currentText() == "blitz":
                z = JsonStruct.structure_blitz_round(self.round_gui.Type_Round.currentText(),
                                                     self.round_gui.Test_Round.isChecked(),
                                                     self.round_gui.Second_Round.value(),
                                                     self.round_gui.Blitz_Score.value())
            else:
                z = JsonStruct.structure_round_settings(self.round_gui.Type_Round.currentText(),
                                                        self.round_gui.Test_Round.isChecked(),
                                                        self.round_gui.Second_Round.value())
            if self.round_gui.Test_Round.isChecked():
                self.list_round.insert(0, z)
            else:
                self.list_round.append(z)

        def save_double_settings(self):
            x = self.list_round[self.count_double_round]
            y = x["settings"]
            if x.get("type") != self.round_gui.Type_Round.currentText():
                x["type"] = self.round_gui.Type_Round.currentText()
            elif y.get("is_test") != self.round_gui.Test_Round.isChecked():
                y["is_test"] = self.round_gui.Test_Round.isChecked()

        def on_del_question(self):
            list_items = self.round_gui.All_Question.selectedItems()
            count_question = self.round_gui.All_Question.currentRow()
            if not list_items: return
            for item in list_items:
                self.round_gui.All_Question.takeItem(self.round_gui.All_Question.row(item))
                del (self.round_gui[self.count_item_round][count_question])
            print("Вопрос удален")

        def all_vision_question(self):
            print(self.count_item_round)
            self.round_gui.All_Question.clear()
            if self.method_on_click == 'addclick':
                if self.quest_dict.get(self.count_item_round):
                    for i in self.quest_dict.get(self.count_item_round):
                        if i.get("type") == "select":
                            self.round_gui.All_Question.insertItem(self.round_gui.All_Question.count(),
                                                                     "С выбором ответа")
                        else:
                            self.round_gui.All_Question.insertItem(self.round_gui.All_Question.count(),
                                                                     "Свободный ответ")
            else:
                if self.quest_dict.get(self.count_double_round):
                    for i in self.quest_dict.get(self.count_double_round):
                        if i.get("type") == "select":
                            self.round_gui.All_Question.insertItem(self.round_gui.All_Question.count(),
                                                                     "С выбором ответа")
                        else:
                            self.round_gui.All_Question.insertItem(self.round_gui.All_Question.count(),
                                                                     "Свободный ответ")

            self.list_quest = self.quest_dict.get(self.count_item_round)
            print("--------------")
            print(self.quest_dict)

        def closeEvent(self, event):
            self.list_quest = []
            if self.method_on_click == 'addclick':
                self.save_round_settings()
            else:
                self.save_double_settings()
            from __main__ import mainFormLogic
            mainFormLogic().reload_all_round(self.link_main)
            mainFormLogic.show(self.link_main)

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

            

