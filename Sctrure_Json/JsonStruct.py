from Gui_Form.ui_main import Ui_MainWindow
from Gui_Form.ui_question_round import Ui_Ques_Round


class JsonStruct():
    def structure_round_settings(self, Type_Round, Test_Round, Second_Round):
        structure_settings_round = {
            "type": Type_Round,
            "settings": {
                "is_test": Test_Round,
                "name": "round_name",
                "display_name": False,
                "time_to_answer": Second_Round,
                "use_special_tactics": True
            },
        }

        return structure_settings_round

    def structure_blitz_round(self, Type_Round, Test_Round, Second_Round, Blitz_Score):
        structure_blitz_round = {
            "type": Type_Round,
            "settings": {
                "is_test": Test_Round,
                "name": "round_name",
                "display_name": False,
                "time_to_answer": Second_Round,
                "blitz_score": Blitz_Score
            },
        }

        return structure_blitz_round

    def structure_main_settings(self, Name_Game, Theme_Game, Client_Game, Date_Game, remove_answer, one_for_all,
                                question_bet, all_in, team_bet, Mail_OnClick):
        structure_main = {
            "game": {
                "game_info": {
                    "name": Name_Game,
                    "theme": Theme_Game,
                    "client": Client_Game,
                    "date": Date_Game,
                },
                "game_settings": {
                    "tactics": {
                        "remove_answer": remove_answer,
                        "one_for_all": one_for_all,
                        "question_bet": question_bet,
                        "all_in": all_in,
                        "team_bet": team_bet
                    },
                    "skip_emails": Mail_OnClick
                },
            }
        }

        return structure_main

    def structure_round(self):
        structure_answer = {
            "rounds": []
        }

        return structure_answer

    def structure_question(self):
        structure_question = {
            "questions": []
        }

        return structure_question

    def structure_question_settings(self, Type_Quest, quest_text, First_Choise, Two_Choise, Third_Choise, Fourth_Choise,
                                    correct_answer):
        structure_quest_settings = {
            "type": Type_Quest,
            "question": quest_text,
            "answers": [
                First_Choise,
                Two_Choise,
                Third_Choise,
                Fourth_Choise
            ],
            "correct_answer": correct_answer,
            "time_to_answer": 20,
            "media_data": {
                "show_image": False,
                "video": {
                    "before": "",
                    "after": ""
                },
                "image": {
                    "before": "",
                    "after": "",
                    "player_displayed": False
                }
            }
        }

        return structure_quest_settings

    def structure_blitz_question(self, number, quest_text, First_Choise):
        structure_blitz_question = {
            "id": number,
            "type": "text",
            "question": quest_text,
            "correct_answer": First_Choise
        }

        return structure_blitz_question

    def test(self):
        print(self.structure_round_settings("test", "test", "test"))
        print(self.structure_main_settings("test", "test", "test", "test", "test", "test", "test", "test", "test2",
                                           "test"))
        print(self.structure_question_settings("test", "test", "test", "test", "test", "test"))
        print(self.structure_round())
        print(self.structure_question())


if __name__ == "__main__":
    JsonStruct().test()
