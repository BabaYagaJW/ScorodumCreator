import shutil
# !/usr/bin/python
# -*- coding: ascii -*-
import sys
import os
import json
from functools import partial

from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

from Gui_Form.ui_main import Ui_MainWindow
from Sctrure_Json.JsonStruct import JsonStruct


class MainLogic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # слушатели для кнопок на форме
        self.ui.Add_Round.clicked.connect(self.on_add_round)
        self.ui.Del_Round.clicked.connect(self.on_del_round)
        self.ui.All_Round.doubleClicked.connect(self.on_double_click_round)
        self.ui.tabWidget.currentChanged.connect(self.tabChanged)
        self.ui.actionSave_as.triggered.connect(self.on_save_json)
        self.ui.Type_Round.currentTextChanged.connect(self.on_type_round)
        self.ui.Blitz_label.setVisible(False)
        self.ui.Blitz_Score.setVisible(False)

        # для работы счетчиков
        self.round_count = 0
        self.quest_select_count = 0
        self.count_question = 0
        self.count_round = 0
        self.quest_text_count = 0

        # переменные для работы раунда и вопросоы
        self.list_round = []
        self.list_quest = []
        self.quest_dict = {}
        self.result_dict = {}
        self.round_dict = {"rounds": self.list_round}


    # Переключение между вкладками
    def tabChanged(self):
        pass

    # Кнопка добавления раунда
    def on_add_round(self):

        if self.ui.Type_Round.currentText() == "classical":
            if self.ui.Test_Round.isChecked():
                self.ui.All_Round.insertItem(0, "Тестовый раунд")
            else:
                self.round_count += 1
                self.ui.All_Round.insertItem(self.ui.All_Round.count(), "Раунд " + str(self.round_count))
        else:
            self.ui.All_Round.insertItem(self.ui.All_Round.count(), "Блитц раунд")

        self.save_round_settings()
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
            if self.round_count >= 0:
                self.round_count -= 1
            else:
                self.round_count = 0

            self.list_round.pop(self.count_round)


    # Двойное нажатие и открытие меню с каждым раундом
    def on_double_click_round(self):
        self.Save_main_settings = JsonStruct.structure_main_settings(self,
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

        from Logic_Gui_Question.QuestionLogic import QuestionLogic
        new_window = QuestionLogic(self.list_round,
                                    self.round_dict,
                                    self.ui.All_Round.currentItem().text(),
                                    self.ui.All_Round.currentRow(),
                                    self.Save_main_settings)
    def on_type_round(self):
        if self.ui.Type_Round.currentText() == "blitz":
            self.ui.Test_Round.setEnabled(False)
            self.ui.Test_Round.setChecked(False)
            self.ui.Blitz_label.setVisible(True)
            self.ui.Blitz_Score.setVisible(True)
            self.ui.Second_Round.setValue(180)
        else:
            self.ui.Test_Round.setEnabled(True)
            self.ui.Blitz_label.setVisible(False)
            self.ui.Blitz_Score.setVisible(False)
            self.ui.Second_Round.setValue(50)


    # Сохранение через бар меню
    def on_save_json(self):
        x["game"].update(self.round_dict)
        file_path_credentials = os.path.join(os.path.dirname(__file__), "scenarion.json")
        with open(file_path_credentials, "w", encoding='utf8') as f:
            json.dump(x, f, indent=4, ensure_ascii=False)

        title = 'Сохранить файл как'
        directory = r'scenario.json'
        embedded_file_path = os.path.join(os.path.dirname(__file__), "scenarion.json")
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
        if self.ui.Type_Round.currentText() == "blitz":
            z = JsonStruct.structure_blitz_round(self,
                                                 self.ui.Type_Round.currentText(),
                                                 self.ui.Test_Round.isChecked(),
                                                 self.ui.Second_Round.value(),
                                                 self.ui.Blitz_Score.value())
        else:
            z = JsonStruct.structure_round_settings(self,
                                                    self.ui.Type_Round.currentText(),
                                                    self.ui.Test_Round.isChecked(),
                                                    self.ui.Second_Round.value())
        if self.ui.Test_Round.isChecked():
            self.list_round.insert(0, z)
        else:
            self.list_round.append(z)

    def save_settings_question(self, quest_dict, round_dict):
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
        self.quest_dict = quest_dict
        self.round_dict = round_dict

        for i in range(len(self.round_dict["rounds"])):
            if not i in self.quest_dict.keys():
                continue
            else:
                self.result_dict = {"questions": self.quest_dict[i]}
                self.round_dict["rounds"][i].update(self.result_dict)
        x["game"].update(self.round_dict)
        file_path_credentials = os.path.join(os.path.dirname(__file__), "scenarion.json")
        with open(file_path_credentials, "w", encoding='utf8') as f:
            json.dump(x, f, indent=4, ensure_ascii=False)

        print("Раунд сохранился")


    def closeEvent(self, event):
        print("test")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainLogic()
    window.show()

    app.exec()
