import shutil
# !/usr/bin/python
# -*- coding: ascii -*-
import sys
import os
import json

from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

from Gui_Form.ui_main import Ui_MainWindow
from Gui_Form.ui_question_round import Ui_Ques_Round
from Sctrure_Json.JsonStruct import JsonStruct


class MainLogic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui_quest = Ui_Ques_Round()
       # self.w_json = work_to_json()
        self.ui.setupUi(self)

        # слушатели для кнопок на форме
        self.ui.Add_Round.clicked.connect(self.on_add_round)
        self.ui.Del_Round.clicked.connect(self.on_del_round)
        self.ui.All_Round.doubleClicked.connect(self.on_double_click_round)
        self.ui.tabWidget.currentChanged.connect(self.tabChanged)
        self.ui.actionSave_as.triggered.connect(self.on_save_json)

        # для работы счетчиков
        self.round_count = 0
        self.quest_select_count = 0
        self.count_question = 0
        self.count_round = 0
        self.quest_text_count = 0

        # переменные для работы раунда и вопросоы
        self.list_round = []
        self.list_quest = []
        self.round_dict = {"rounds": self.list_round}
        self.quest_dict = {}
        self.result_dict = {}

    # Переключение между вкладками
    def tabChanged(self):
        x = JsonStruct.structure_main_settings(self,
                                               self.ui.Name_Game.text(),
                                               self.ui.Theme_Game.text(),
                                               self.ui.Client_Game.text(),
                                               self.ui.Date_Game.text(),
                                               self.ui.remove_answer.value(),
                                               self.ui.one_for_all.value(),
                                               self.ui.question_bet.value(),
                                               self.ui.all_in.value(),
                                               self.ui.team_bet.value(),
                                               self.ui.Mail_OnClick.isChecked())

        if self.ui.tabWidget.currentIndex() == 1:
            pass
        else:
            for i in range(len(self.round_dict["rounds"])):
                print(i)
                if not i in self.quest_dict.keys():
                    print("нет ключа")
                    continue

                else:
                    self.result_dict = {"questions": self.quest_dict[i]}
                    self.round_dict["rounds"][i].update(self.result_dict)

            x["game"].update(self.round_dict)
            file_path_credentials = os.path.join(os.path.dirname(__file__), "scenarion.json")
            with open(file_path_credentials, "w", encoding='utf8') as f:
                json.dump(x, f, indent=4, ensure_ascii=False)

    # Двойное нажатие и открытие меню с каждым раундом
    def on_double_click_round(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_quest.setupUi(self.window)
        self.window.show()
        self.ui_quest.Add_Quest.clicked.connect(self.on_add_question)
        self.ui_quest.Del_Quest.clicked.connect(self.on_del_question)
        self.ui_quest.All_Question.doubleClicked.connect(self.on_click_question)
        self.ui_quest.One_Correct.clicked.connect(self.on_one_correct)
        self.ui_quest.Two_Correct.clicked.connect(self.on_two_correct)
        self.ui_quest.Three_Correct.clicked.connect(self.on_three_correct)
        self.ui_quest.Fourth_Correct.clicked.connect(self.on_fourth_correct)
        #self.ui_quest.Type_Quest.clicked.connect(self.on_type_quests)
       # self.ui_quest.closeEvent(self.window)

        rounds = self.ui.All_Round.currentRow()
        count_question = 0

        if self.ui.All_Round.currentItem().text() == "Блитц Раунд":
            print("Выбран блитц раунд")
            self.ui_quest.Two_Choise.setVisible(False)
            self.ui_quest.Third_Choise.setVisible(False)
            self.ui_quest.Fourth_Choise.setVisible(False)
            self.ui_quest.Two_Correct.setVisible(False)
            self.ui_quest.Three_Correct.setVisible(False)
            self.ui_quest.Fourth_Correct.setVisible(False)
            self.ui_quest.One_Correct.setChecked(True)
            self.ui_quest.Type_Quest.setVisible(False)
            self.ui_quest.label_23.setVisible(False)
            self.ui_quest.label_22.setVisible(False)
            self.ui_quest.label_26.setVisible(False)
            self.ui_quest.label_27.setVisible(False)
            self.ui_quest.label_28.setVisible(False)
        else:
            print("Выбран обычный раунд")

        # Найти решение исправления, ибо мешается, если там 0
        if self.quest_dict:
            if self.list_round[rounds]:
                if self.quest_dict.get(rounds):
                    for i in self.quest_dict.get(rounds):
                        if i.get("type") == "select":
                            self.ui_quest.All_Question.insertItem(self.ui_quest.All_Question.count(), "С выбором ответа")
                        else:
                            self.ui_quest.All_Question.insertItem(self.ui_quest.All_Question.count(), "Свободный ответ")


    def on_type_quest(self):
        print('test')

    def closeEvent(self, event):
        print("test")

    #Нажатие на кнопку с отметкой о правильном ответе

    def on_one_correct(self):
        if self.ui_quest.One_Correct.isChecked():
            self.ui_quest.Two_Correct.setEnabled(False)
            self.ui_quest.Three_Correct.setEnabled(False)
            self.ui_quest.Fourth_Correct.setEnabled(False)
        else:
            self.ui_quest.Two_Correct.setEnabled(True)
            self.ui_quest.Three_Correct.setEnabled(True)
            self.ui_quest.Fourth_Correct.setEnabled(True)

    def on_two_correct(self):
        if self.ui_quest.Two_Correct.isChecked():
            self.ui_quest.One_Correct.setEnabled(False)
            self.ui_quest.Three_Correct.setEnabled(False)
            self.ui_quest.Fourth_Correct.setEnabled(False)
        else:
            self.ui_quest.One_Correct.setEnabled(True)
            self.ui_quest.Three_Correct.setEnabled(True)
            self.ui_quest.Fourth_Correct.setEnabled(True)

    def on_three_correct(self):
        if self.ui_quest.Three_Correct.isChecked():
            self.ui_quest.Two_Correct.setEnabled(False)
            self.ui_quest.One_Correct.setEnabled(False)
            self.ui_quest.Fourth_Correct.setEnabled(False)
        else:
            self.ui_quest.Two_Correct.setEnabled(True)
            self.ui_quest.One_Correct.setEnabled(True)
            self.ui_quest.Fourth_Correct.setEnabled(True)

    def on_fourth_correct(self):
        if self.ui_quest.Fourth_Correct.isChecked():
            self.ui_quest.Two_Correct.setEnabled(False)
            self.ui_quest.Three_Correct.setEnabled(False)
            self.ui_quest.One_Correct.setEnabled(False)
        else:
            self.ui_quest.Two_Correct.setEnabled(True)
            self.ui_quest.Three_Correct.setEnabled(True)
            self.ui_quest.One_Correct.setEnabled(True)


    # Кнопка добавления вопроса
    def on_add_question(self):
        if self.ui_quest.Type_Quest.currentText() == "select":
            self.ui_quest.All_Question.insertItem(self.ui_quest.All_Question.count(),
                                                  "С выбором ответа")
        else:
            self.ui_quest.All_Question.insertItem(self.ui_quest.All_Question.count(),
                                                  "Свободный ответ")

        self.save_question_settings()
        self.ui_quest.quest_text.clear()
        self.ui_quest.First_Choise.clear()
        self.ui_quest.Two_Choise.clear()
        self.ui_quest.Third_Choise.clear()
        self.ui_quest.Fourth_Choise.clear()
        self.ui_quest.One_Correct.setEnabled(True)
        self.ui_quest.One_Correct.setChecked(False)
        self.ui_quest.Two_Correct.setEnabled(True)
        self.ui_quest.Two_Correct.setChecked(False)
        self.ui_quest.Three_Correct.setEnabled(True)
        self.ui_quest.Three_Correct.setChecked(False)
        self.ui_quest.Fourth_Correct.setEnabled(True)
        self.ui_quest.Fourth_Correct.setChecked(False)

    def on_click_question(self):
        self.ui_quest.quest_text.textEdited.connect(self.on_quest_text)
        self.ui_quest.First_Choise.textEdited.connect(self.on_one_choise)
        self.ui_quest.Two_Choise.textEdited.connect(self.on_two_choise)
        self.ui_quest.Third_Choise.textEdited.connect(self.on_three_choise)
        self.ui_quest.Fourth_Choise.textEdited.connect(self.on_fourth_choise)

        round = self.ui.All_Round.currentRow()
        count_question = self.ui_quest.All_Question.currentRow()
        list_items = self.ui_quest.All_Question.selectedItems()
        question_visible = []

        x = self.quest_dict[round][count_question]
        y = x.get("answers")

        self.ui_quest.quest_text.setText(x.get("question"))
        self.ui_quest.First_Choise.setText(y[0])
        self.ui_quest.Two_Choise.setText(y[1])
        self.ui_quest.Third_Choise.setText(y[2])
        self.ui_quest.Fourth_Choise.setText(y[3])

    # Для проверки изменений

    def on_quest_text(self):
        round = self.ui.All_Round.currentRow()
        count_question = self.ui_quest.All_Question.currentRow()
        count_add_quest = self.ui_quest.All_Question.count()
        list_items = self.ui_quest.All_Question.selectedItems()
        question_visible = []
        print(count_add_quest)
        if count_add_quest != 0:
            x = self.quest_dict[round][count_question]
            if self.ui_quest.quest_text.text() != x.get("question"):
                x["question"] = self.ui_quest.quest_text.text()
            else:
                print('Изменений нет')



    def on_one_choise(self):
        count_round = self.ui.All_Round.currentRow()
        count_question = self.ui_quest.All_Question.currentRow()
        count_add_quest = self.ui_quest.All_Question.count()
        list_items = self.ui_quest.All_Question.selectedItems()
        question_visible = []
        print(count_add_quest)
        if count_add_quest != 0:
            x = self.quest_dict[count_round][count_question]
            y = x.get("answers")
            if self.ui_quest.First_Choise.text() != y[0]:
                y[0] = self.ui_quest.First_Choise.text()
            else:
                print('Изменений нет')


    def on_two_choise(self):
        round = self.ui.All_Round.currentRow()
        count_question = self.ui_quest.All_Question.currentRow()
        count_add_quest = self.ui_quest.All_Question.count()
        list_items = self.ui_quest.All_Question.selectedItems()
        question_visible = []

        print(count_add_quest)
        if count_add_quest != 0:
            x = self.quest_dict[round][count_question]
            y = x.get("answers")


            if self.ui_quest.Two_Choise.text() != y[1]:
                y[1] = self.ui_quest.Two_Choise.text()
            else:
                print('Изменений нет')


    def on_three_choise(self):
        round = self.ui.All_Round.currentRow()
        count_question = self.ui_quest.All_Question.currentRow()
        count_add_quest = self.ui_quest.All_Question.count()
        list_items = self.ui_quest.All_Question.selectedItems()
        question_visible = []

        print(count_add_quest)
        if count_add_quest != 0:
            x = self.quest_dict[round][count_question]
            y = x.get("answers")

            if self.ui_quest.Third_Choise.text() != y[2]:
                y[2] = self.ui_quest.Third_Choise.text()
            else:
                print('Изменений нет')


    def on_fourth_choise(self):
        round = self.ui.All_Round.currentRow()
        count_question = self.ui_quest.All_Question.currentRow()
        count_add_quest = self.ui_quest.All_Question.count()
        list_items = self.ui_quest.All_Question.selectedItems()
        question_visible = []

        print(count_add_quest)
        if count_add_quest != 0:
            x = self.quest_dict[round][count_question]
            y = x.get("answers")
            if self.ui_quest.Fourth_Choise.text() != y[3]:
                y[3] = self.ui_quest.Fourth_Choise.text()
            else:
                print('Изменений нет')


    # Кнопка удаления вопроса
    def on_del_question(self):
        count_items = self.ui.All_Round.currentRow()
        list_items = self.ui_quest.All_Question.selectedItems()
        self.count_question = self.ui.All_Round.currentRow()
        if not list_items: return
        for item in list_items:
            self.ui_quest.All_Question.takeItem(self.ui_quest.All_Question.row(item))
            self.quest_dict.pop([count_items][self.count_question])
            # del self.quest_dict[count_items][self.count_question]
        print("Успешное удаление")

    # Кнопка добавления раунда
    def on_add_round(self):
        # print(self.ui.All_Round.count())

        if self.ui.Type_Round.currentText() == "classical":
            if self.ui.Test_Round.isChecked():
                self.ui.All_Round.insertItem(0, "Тестовый раунд")
            else:
                self.round_count += 1
                self.ui.All_Round.insertItem(self.ui.All_Round.count(), "Раунд " + str(self.round_count))
        else:
            self.ui.All_Round.insertItem(self.ui.All_Round.count(), "Блитц Раунд")

        self.save_round_settings()
        self.list_quest = []

    # Кнопка удаления раунда и удаление его из JSON
    def on_del_round(self):
        z = JsonStruct.structure_round_settings(self,
                                                self.ui.Type_Round.currentText(),
                                                self.ui.Test_Round.isChecked(),
                                                self.ui.Second_Round.value())
        list_items = self.ui.All_Round.selectedItems()
        self.count_round = self.ui.All_Round.currentRow()
        if not list_items: return
        for item in list_items:
            self.ui.All_Round.takeItem(self.ui.All_Round.row(item))
            self.round_ -= 1
            self.list_round.pop(self.count_round)

    # сохранение через верхнюю вкладку (доработка требуется!)
    def on_save_json(self):
        title = 'Сохранить файл как'
        directory = r'C:\Users\Home\scenario.json'
        filter_file = "Json_File *json"
        embedded_file_path = "C:/Users/andre/PycharmProjects/ScorodumCreator/test.json"
        options = QFileDialog.Options()
        dest_file, _ = QFileDialog.getSaveFileName(self, title, directory, "All Files (*)", options=options)
        if dest_file:
            try:
                shutil.copy(embedded_file_path, dest_file)
                QMessageBox.information(self, "Успех", f"Файл успешно сохранен в: {dest_file}")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {e}")

    # Сохранение настроек раунда в JSON
    def save_round_settings(self):
        z = JsonStruct.structure_round_settings(self,
                                                self.ui.Type_Round.currentText(),
                                                self.ui.Test_Round.isChecked(),
                                                self.ui.Second_Round.value())

        if self.ui.Test_Round.isChecked():
            self.list_round.insert(0, z)
        else:
            self.list_round.append(z)

    # Сохранение вопросов
    def save_question_settings(self):
        count_items = self.ui.All_Round.currentRow()
        count_items_queston = self.ui_quest.All_Question.currentRow()

        if self.ui.All_Round.currentItem().text() == "Блитц Раунд":
            z = JsonStruct.structure_blitz_round(self,
                                                 self.ui_quest.quest_text.text(),
                                                 self.ui_quest.First_Choise.text())

            self.list_quest.append(z)

            if not bool(self.quest_dict.get(count_items)):
                self.quest_dict[count_items] = list(z)
            else:
                self.quest_dict.update({count_items: self.list_quest})
        else:
            if self.ui_quest.One_Correct.isChecked():
                self.correct_answer = self.ui_quest.First_Choise.text()
            elif self.ui_quest.Two_Correct.isChecked():
                self.correct_answer = self.ui_quest.Two_Choise.text()
            elif self.ui_quest.Three_Correct.isChecked():
                self.correct_answer = self.ui_quest.Third_Choise.text()
            else:
                self.correct_answer = self.ui_quest.Fourth_Choise.text()

            z = JsonStruct.structure_question_settings(self,
                                                       self.ui_quest.Type_Quest.currentText(),
                                                       self.ui_quest.quest_text.text(),
                                                       self.ui_quest.First_Choise.text(),
                                                       self.ui_quest.Two_Choise.text(),
                                                       self.ui_quest.Third_Choise.text(),
                                                       self.ui_quest.Fourth_Choise.text(),
                                                       self.correct_answer)

            self.list_quest.append(z)

            if not bool(self.quest_dict.get(count_items)):
                self.quest_dict.update({count_items: self.list_quest})
            else:
                self.quest_dict.update({count_items: self.list_quest})

            print(self.quest_dict)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainLogic()
    window.show()

    app.exec()
