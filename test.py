#self.ui_quest.Add_Quest.clicked.connect(self.on_add_question)
        #self.ui_quest.Del_Quest.clicked.connect(self.on_del_question)
        #self.ui_quest.All_Question.doubleClicked.connect(self.on_click_question)
        #self.ui_quest.One_Correct.clicked.connect(self.on_one_correct)
        #self.ui_quest.Two_Correct.clicked.connect(self.on_two_correct)
        #self.ui_quest.Three_Correct.clicked.connect(self.on_three_correct)
        #self.ui_quest.Fourth_Correct.clicked.connect(self.on_fourth_correct)


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

                self.ui_quest.One_Correct.clicked.connect(self.on_one_correct)
                self.ui_quest.Two_Correct.clicked.connect(self.on_two_correct)
                self.ui_quest.Three_Correct.clicked.connect(self.on_three_correct)
                self.ui_quest.Fourth_Correct.clicked.connect(self.on_fourth_correct)
                self.ui_quest.Save_Question.clicked.connect(self.on_save_question)

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

                    self.ui_quest.Add_Quest.setVisible(False)
                    self.ui_quest.Del_Quest.setVisible(False)
                    self.ui_quest.Save_Question.setVisible(True)

#def del_round(self, count_del_round):
           # self.quest_dict.pop(count_del_round)
           # for i in list(self.quest_dict):
           #     print(i)
            #    if i > count_del_round:
             #       self.del_quest_dict[i - 1] = self.quest_dict[i]
             #   else:
             #       self.del_quest_dict[i] = self.quest_dict[i]

          #  self.quest_dict = dict(self.del_quest_dict)
          #  print(self.quest_dict)

    def reload_all_round(self):
        self.ui.All_Round.clear()
        for i in self.list_round:
            x = i['settings']
            if x['is_test'] != False:
                self.ui.All_Round.insertItem(0, 'Тестовый раунд')
            else:
                try:
                    if i['type'] == 'classical':
                        self.ui.All_Round.insertItem(self.ui.All_Round.count(),
                                                     "Раунд " + str(self.ui.All_Round.count() + 1))
                    else:
                        self.ui.All_Round.insertItem(self.ui.All_Round.count(),
                                                     "Блитц раунд")
                finally:
                    pass