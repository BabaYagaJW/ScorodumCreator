from Gui_Form.ui_main import Ui_MainWindow
from Gui_Form.ui_question_round import Ui_Ques_Round

class work_to_json(object):
        def __init__(self):
                super().__init__()
                self.ui = Ui_MainWindow()
                self.ui_quest = Ui_Ques_Round()
                #self.ui.setupUi(self)

        #Сохранение основных настроек
        def save_main_settings(self):
                print(self.ui.Name_Game.text())
