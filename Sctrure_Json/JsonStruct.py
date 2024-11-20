from Gui_Form.ui_main import Ui_MainWindow
from Gui_Form.form_round import Ui_form_round


class JsonStruct():
    @staticmethod
    def structure_round_settings(Type_Round, Test_Round, Second_Round):
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

    @staticmethod
    def structure_blitz_round(Type_Round, Test_Round, Second_Round, Blitz_Score):
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

    @staticmethod
    def structure_main_settings(Name_Game, Theme_Game, Client_Game, Date_Game, remove_answer, one_for_all,
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

    @staticmethod
    def structure_round():
        structure_answer = {
            "rounds": []
        }

        return structure_answer

    @staticmethod
    def structure_question():
        structure_question = {
            "questions": []
        }

        return structure_question

    @staticmethod
    def structure_question_settings(Type_Quest, quest_text, First_Choise, Two_Choise, Third_Choise, Fourth_Choise,
                                    correct_answer, Second_Round):
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
            "time_to_answer": Second_Round,
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

    @staticmethod
    def structure_blitz_question(number, quest_text, First_Choise):
        structure_blitz_question = {
            "id": number,
            "type": "text",
            "question": quest_text,
            "correct_answer": First_Choise
        }

        return structure_blitz_question
