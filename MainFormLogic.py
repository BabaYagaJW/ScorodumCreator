import json
import os
import shutil
import sys
from datetime import date

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from Gui_Form.ui_main import Ui_MainWindow
from Logic_Gui_Question.RoundLogic import RoundLogic
from Sctrure_Json.JsonStruct import JsonStruct


class mainFormLogic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Date_Game.setText(date.today().strftime("%d.%m.%Y"))
        # переменные для работы раунда и вопросоы
        self.list_round = []
        self.quest_dict = {}
        self.result_dict = {}
        self.del_quest_dict = {}
        self.round_dict = {"rounds": self.list_round}

        self.ui.Add_Round.clicked.connect(self.on_add_round)
        self.ui.Del_Round.clicked.connect(self.on_del_round)
        self.ui.actionSave_as.triggered.connect(self.on_save_json)
        self.ui.Save_Json.clicked.connect(self.on_save_json)
        self.ui.All_Round.doubleClicked.connect(self.on_double_click_round)

    def on_double_click_round(self):
        window_round = RoundLogic(self.list_round, self, self.quest_dict, self.ui.All_Round.count(), self.ui.All_Round.currentRow(), self.round_dict, self.Save_main_settings, "doubleclick", self.ui.All_Round.currentItem().text())
        self.hide()

    def on_add_round(self):
        self.Save_main_settings = JsonStruct.structure_main_settings(self.ui.Name_Game.text(),
                                                                     self.ui.Theme_Game.text(),
                                                                     self.ui.Client_Game.text(),
                                                                     self.ui.Date_Game.text(),
                                                                     self.ui.remove_answer.value(),
                                                                     self.ui.one_for_all.value(),
                                                                     self.ui.question_bet.value(),
                                                                     self.ui.all_in.value(),
                                                                     self.ui.team_bet.value(),
                                                                     self.ui.Mail_OnClick.isChecked())

        print(self.list_round)
        self.hide()
        window_round = RoundLogic(self.list_round, self, self.quest_dict, self.ui.All_Round.count(), self.ui.All_Round.currentRow(), self.round_dict, self.Save_main_settings, "addclick", None)

         # Сохранение через бар меню

    def reload_all_round(self, link_main):
        link_main.ui.All_Round.insertItem(0, 'test')
        print(link_main.list_round)
        link_main.ui.All_Round.clear()
        for i in link_main.list_round:
            x = i['settings']
            if x['is_test'] != False:
                link_main.ui.All_Round.insertItem(0, 'Тестовый раунд')
            else:
                try:
                    if i['type'] == 'classical':
                        link_main.ui.All_Round.insertItem(link_main.ui.All_Round.count(),
                                                     "Раунд " + str(link_main.ui.All_Round.count() + 1))
                        if x['is_test']:
                            link_main.ui.All_Round.insertItem(0, "Тестовый раунд")
                    else:
                        link_main.ui.All_Round.insertItem(link_main.ui.All_Round.count(),
                                                     "Блитц раунд")
                finally:
                    pass

    def on_del_round(self):
        text_round_del = self.ui.All_Round.currentItem().text()
        from Logic_Gui_Question.QuestionLogic import QuestionLogic
        if not self.ui.All_Round.selectedItems(): return
        for item in self.ui.All_Round.selectedItems():
            self.ui.All_Round.takeItem(self.ui.All_Round.row(item))
            self.list_round.pop(self.ui.All_Round.currentRow())
            #QuestionLogic.del_round(self, self.count_round)
            self.reload_all_round(self)
            print("Удалили раунд: " + text_round_del)

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

    def on_save_json(self):
        x = JsonStruct.structure_main_settings(self.ui.Name_Game.text(),
                                               self.ui.Theme_Game.text(),
                                               self.ui.Client_Game.text(),
                                               self.ui.Date_Game.text(),
                                               self.ui.remove_answer.value(),
                                               self.ui.one_for_all.value(),
                                               self.ui.question_bet.value(),
                                               self.ui.all_in.value(),
                                               self.ui.team_bet.value(),
                                               self.ui.Mail_OnClick.isChecked())

        x["game"].update(self.round_dict)
        file_path_credentials = os.path.join(os.path.dirname("ScorodumCreator"), "scenario.json")
        with open(file_path_credentials, "w", encoding='utf8') as f:
            json.dump(x, f, indent=4, ensure_ascii=False)

        title = 'Сохранить файл как'
        directory = r'scenario.json'
        embedded_file_path = os.path.join(os.path.dirname("ScorodumCreator"), "scenario.json")
        options = QFileDialog.Options()
        dest_file, _ = QFileDialog.getSaveFileName(self, title, directory, "All Files (*)", options=options)
        if dest_file:
            try:
                shutil.copy(embedded_file_path, dest_file)
                QMessageBox.information(self, "Успех", f"Файл успешно сохранен в: {dest_file}")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainFormLogic()
    window.show()
    app.exec()