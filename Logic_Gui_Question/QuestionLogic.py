from traceback import print_tb

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from Gui_Form.form_question import Ui_form_question
from Sctrure_Json.JsonStruct import JsonStruct


#from Gui_Form.test_form import Ui_Test_Form



class QuestionLogic():
    def __init__(self, quest_dict, link, type_round, count_item_round, count_question, list_quest, second_round, text_click, currentRowQuest):
        super().__init__()

        self.window_quest = QtWidgets.QMainWindow()
        self.question_gui = Ui_form_question()
        self.question_gui.setupUi(self.window_quest)
        self.window_quest.show()
        self.window_quest.closeEvent = self.closeEvent

        self.question_gui.One_Correct.clicked.connect(self.on_one_correct)
        self.question_gui.Two_Correct.clicked.connect(self.on_two_correct)
        self.question_gui.Three_Correct.clicked.connect(self.on_three_correct)
        self.question_gui.Fourth_Correct.clicked.connect(self.on_fourth_correct)
        self.question_gui.Save_Question.clicked.connect(self.on_save_question)
        self.question_gui.type_question.currentTextChanged.connect(self.on_type_question)

        self.Type_Quest = ""
        self.quest_text = ""
        self.First_Choise = ""
        self.Two_Choise = ""
        self.Third_Choise = ""
        self.Fourth_Choise = ""
        self.correct_answer = ""
        self.blitz_counter = 0

        self.quest_dict = quest_dict
        self.type_round = type_round
        self.count_item_round = count_item_round
        self.count_question = count_question
        self.list_quest = list_quest
        self.second_round = second_round
        self.link_round = link
        self.currentRowQuest = currentRowQuest

        if text_click == "doubleclick":
            try:
                x = self.quest_dict[self.count_item_round][self.currentRowQuest]
            except KeyError:
                pass
            except IndexError:
                pass
            else:
                 if self.type_round == "Блитц раунд":
                     self.question_gui.quest_text.setText(x.get("question"))
                     self.question_gui.First_Choise.setText(x.get("correct_answer"))
                     self.question_gui.One_Correct.setChecked(True)
                     self.question_gui.One_Correct.setEnabled(False)
                 else:

                     y = x.get("answers")

                     if (x.get("type") == "select"):
                         self.question_gui.type_question.setItemText(0, x.get("type"))
                         self.question_gui.type_question.setItemText(1, "text")
                     else:
                         self.question_gui.type_question.setItemText(0, x.get("type"))
                         self.question_gui.type_question.setItemText(1, "select")

                     self.question_gui.quest_text.setText(x.get("question"))
                     self.question_gui.First_Choise.setText(y[0])
                     self.question_gui.Two_Choise.setText(y[1])
                     self.question_gui.Third_Choise.setText(y[2])
                     self.question_gui.Fourth_Choise.setText(y[3])

                     if x.get("correct_answer") == y[0]:
                         self.question_gui.One_Correct.setChecked(True)
                         self.question_gui.Two_Correct.setEnabled(False)
                         self.question_gui.Three_Correct.setEnabled(False)
                         self.question_gui.Fourth_Correct.setEnabled(False)
                     elif x.get("correct_answer") == y[1]:
                         self.question_gui.Two_Correct.setChecked(True)
                         self.question_gui.One_Correct.setEnabled(False)
                         self.question_gui.Three_Correct.setEnabled(False)
                         self.question_gui.Fourth_Correct.setEnabled(False)
                     elif x.get("correct_answer") == y[2]:
                         self.question_gui.Three_Correct.setChecked(True)
                         self.question_gui.Two_Correct.setEnabled(False)
                         self.question_gui.One_Correct.setEnabled(False)
                         self.question_gui.Fourth_Correct.setEnabled(False)
                     else:
                         self.question_gui.Fourth_Correct.setChecked(True)
                         self.question_gui.Two_Correct.setEnabled(False)
                         self.question_gui.Three_Correct.setEnabled(False)
                         self.question_gui.One_Correct.setEnabled(False)


    def on_save_question(self):
        try:
            x = self.quest_dict[self.count_item_round][self.count_question]
        except KeyError:
            if self.type_round == "Блитц раунд":
                z = JsonStruct.structure_blitz_question(self.blitz_counter,
                                                                   self.question_gui.quest_text.text(),
                                                                   self.question_gui.First_Choise.text())
                self.list_quest.append(z)

                if not bool(self.quest_dict.get(self.count_item_round)):
                    self.quest_dict[self.count_item_round] = self.list_quest
                else:
                    self.quest_dict.update({self.count_item_round: self.list_quest})

                self.blitz_counter += 1
            else:
                if self.question_gui.One_Correct.isChecked():
                    self.correct_answer = self.question_gui.First_Choise.text()
                elif self.question_gui.Two_Correct.isChecked():
                    self.correct_answer = self.question_gui.Two_Choise.text()
                elif self.question_gui.Three_Correct.isChecked():
                    self.correct_answer = self.question_gui.Third_Choise.text()
                else:
                    self.correct_answer = self.question_gui.Fourth_Choise.text()

                z = JsonStruct.structure_question_settings(self.question_gui.type_question.currentText(),
                                                                      self.question_gui.quest_text.text(),
                                                                      self.question_gui.First_Choise.text(),
                                                                      self.question_gui.Two_Choise.text(),
                                                                      self.question_gui.Third_Choise.text(),
                                                                      self.question_gui.Fourth_Choise.text(),
                                                                      self.correct_answer,
                                                                      self.second_round)

                self.list_quest.append(z)

                if not bool(self.quest_dict.get(self.count_item_round)):
                    self.quest_dict.update({self.count_item_round: self.list_quest})
                else:
                    self.quest_dict.update({self.count_item_round: self.list_quest})
        except IndexError:
            if self.type_round == "Блитц раунд":
                z = JsonStruct.structure_blitz_question(self.blitz_counter,
                                                                   self.question_gui.quest_text.text(),
                                                                   self.question_gui.First_Choise.text())
                self.list_quest.append(z)

                if not bool(self.quest_dict.get(self.count_item_round)):
                    self.quest_dict[self.count_item_round] = dict(z)
                else:
                    self.quest_dict.update({self.count_item_round: self.list_quest})

                self.blitz_counter += 1
            else:
                if self.question_gui.One_Correct.isChecked():
                    self.correct_answer = self.question_gui.First_Choise.text()
                elif self.question_gui.Two_Correct.isChecked():
                    self.correct_answer = self.question_gui.Two_Choise.text()
                elif self.question_gui.Three_Correct.isChecked():
                    self.correct_answer = self.question_gui.Third_Choise.text()
                else:
                    self.correct_answer = self.question_gui.Fourth_Choise.text()

                z = JsonStruct.structure_question_settings(self.question_gui.type_question.currentText(),
                                                                      self.question_gui.quest_text.text(),
                                                                      self.question_gui.First_Choise.text(),
                                                                      self.question_gui.Two_Choise.text(),
                                                                      self.question_gui.Third_Choise.text(),
                                                                      self.question_gui.Fourth_Choise.text(),
                                                                      self.correct_answer,
                                                                      self.second_round)

                self.list_quest.append(z)

                if not bool(self.quest_dict.get(self.count_item_round)):
                    self.quest_dict.update({self.count_item_round: self.list_quest})
                else:
                    self.quest_dict.update({self.count_item_round: self.list_quest})
        else:
            if self.type_round == "Блитц раунд":

                x["question"] = self.question_gui.quest_text.text()
                x["correct_answer"] = self.question_gui.First_Choise.text()
            else:
                y = x.get("answers")

                x["type"] = self.question_gui.type_question.currentText()
                print(x["type"])
                x["question"] = self.question_gui.quest_text.text()
                y[0] = self.question_gui.First_Choise.text()
                y[1] = self.question_gui.Two_Choise.text()
                y[2] = self.question_gui.Third_Choise.text()
                y[3] = self.question_gui.Fourth_Choise.text()
                if self.question_gui.One_Correct.isChecked():
                    x["correct_answer"] = self.question_gui.First_Choise.text()
                elif self.question_gui.Two_Correct.isChecked():
                    x["correct_answer"] = self.question_gui.Two_Choise.text()
                elif self.question_gui.Three_Correct.isChecked():
                    x["correct_answer"] = self.question_gui.Third_Choise.text()
                else:
                    x["correct_answer"] = self.question_gui.Fourth_Choise.text()

        self.window_quest.close()
        self.link_round.all_vision_question(self.link_round)

    def on_type_question(self):
        if self.question_gui.type_question.currentText() == "text":
            self.question_gui.label_26.setEnabled(False)
            self.question_gui.label_27.setEnabled(False)
            self.question_gui.label_28.setEnabled(False)
            self.question_gui.Two_Choise.setEnabled(False)
            self.question_gui.Fourth_Choise.setEnabled(False)
            self.question_gui.Third_Choise.setEnabled(False)
            self.question_gui.Two_Correct.setEnabled(False)
            self.question_gui.Three_Correct.setEnabled(False)
            self.question_gui.Fourth_Correct.setEnabled(False)
            self.question_gui.One_Correct.setChecked(True)
        else:
            self.question_gui.label_26.setEnabled(True)
            self.question_gui.label_27.setEnabled(True)
            self.question_gui.label_28.setEnabled(True)
            self.question_gui.Two_Choise.setEnabled(True)
            self.question_gui.Fourth_Choise.setEnabled(True)
            self.question_gui.Third_Choise.setEnabled(True)
            self.question_gui.Two_Correct.setEnabled(True)
            self.question_gui.Fourth_Correct.setEnabled(True)
            self.question_gui.Three_Correct.setEnabled(True)
            self.question_gui.One_Correct.setChecked(False)
    # Нажатие на кнопку с отметкой о правильном ответе
    def on_one_correct(self):
        if self.question_gui.One_Correct.isChecked():
            self.question_gui.Two_Correct.setEnabled(False)
            self.question_gui.Three_Correct.setEnabled(False)
            self.question_gui.Fourth_Correct.setEnabled(False)
        else:
            self.question_gui.Two_Correct.setEnabled(True)
            self.question_gui.Three_Correct.setEnabled(True)
            self.question_gui.Fourth_Correct.setEnabled(True)

    def on_two_correct(self):
        if self.question_gui.Two_Correct.isChecked():
            self.question_gui.One_Correct.setEnabled(False)
            self.question_gui.Three_Correct.setEnabled(False)
            self.question_gui.Fourth_Correct.setEnabled(False)
        else:
            self.question_gui.One_Correct.setEnabled(True)
            self.question_gui.Three_Correct.setEnabled(True)
            self.question_gui.Fourth_Correct.setEnabled(True)

    def on_three_correct(self):
        if self.question_gui.Three_Correct.isChecked():
            self.question_gui.Two_Correct.setEnabled(False)
            self.question_gui.One_Correct.setEnabled(False)
            self.question_gui.Fourth_Correct.setEnabled(False)
        else:
            self.question_gui.Two_Correct.setEnabled(True)
            self.question_gui.One_Correct.setEnabled(True)
            self.question_gui.Fourth_Correct.setEnabled(True)

    def on_fourth_correct(self):
        if self.question_gui.Fourth_Correct.isChecked():
            self.question_gui.Two_Correct.setEnabled(False)
            self.question_gui.Three_Correct.setEnabled(False)
            self.question_gui.One_Correct.setEnabled(False)
        else:
            self.question_gui.Two_Correct.setEnabled(True)
            self.question_gui.Three_Correct.setEnabled(True)
            self.question_gui.One_Correct.setEnabled(True)

    def closeEvent(self, event):
        print("Закрыто")

        self.list_quest = []