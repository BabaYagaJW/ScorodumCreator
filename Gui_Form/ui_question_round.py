# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_question_round.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDialog, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_Ques_Round(object):
    def setupUi(self, Ques_Round):
        if not Ques_Round.objectName():
            Ques_Round.setObjectName(u"Ques_Round")
        Ques_Round.resize(760, 408)
        self.All_Question = QListWidget(Ques_Round)
        self.All_Question.setObjectName(u"All_Question")
        self.All_Question.setGeometry(QRect(500, 20, 241, 341))
        self.All_Question.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.SelectedClicked)
        self.All_Question.setProperty(u"showDropIndicator", False)
        self.Add_Quest = QPushButton(Ques_Round)
        self.Add_Quest.setObjectName(u"Add_Quest")
        self.Add_Quest.setGeometry(QRect(520, 370, 75, 24))
        self.Del_Quest = QPushButton(Ques_Round)
        self.Del_Quest.setObjectName(u"Del_Quest")
        self.Del_Quest.setGeometry(QRect(650, 370, 75, 24))
        self.label_22 = QLabel(Ques_Round)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(140, 60, 70, 28))
        self.Type_Quest = QComboBox(Ques_Round)
        self.Type_Quest.addItem("")
        self.Type_Quest.addItem("")
        self.Type_Quest.setObjectName(u"Type_Quest")
        self.Type_Quest.setGeometry(QRect(220, 60, 70, 28))
        self.label_23 = QLabel(Ques_Round)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 110, 70, 28))
        self.label_24 = QLabel(Ques_Round)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(170, 150, 101, 28))
        self.First_Choise = QLineEdit(Ques_Round)
        self.First_Choise.setObjectName(u"First_Choise")
        self.First_Choise.setGeometry(QRect(80, 190, 311, 22))
        self.Two_Choise = QLineEdit(Ques_Round)
        self.Two_Choise.setObjectName(u"Two_Choise")
        self.Two_Choise.setGeometry(QRect(80, 230, 311, 22))
        self.Third_Choise = QLineEdit(Ques_Round)
        self.Third_Choise.setObjectName(u"Third_Choise")
        self.Third_Choise.setGeometry(QRect(80, 270, 311, 22))
        self.Fourth_Choise = QLineEdit(Ques_Round)
        self.Fourth_Choise.setObjectName(u"Fourth_Choise")
        self.Fourth_Choise.setGeometry(QRect(80, 310, 311, 22))
        self.label_25 = QLabel(Ques_Round)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 190, 51, 28))
        self.label_26 = QLabel(Ques_Round)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 230, 51, 28))
        self.label_27 = QLabel(Ques_Round)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 270, 51, 28))
        self.label_28 = QLabel(Ques_Round)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 310, 61, 28))
        self.One_Correct = QCheckBox(Ques_Round)
        self.One_Correct.setObjectName(u"One_Correct")
        self.One_Correct.setGeometry(QRect(410, 190, 51, 20))
        self.Two_Correct = QCheckBox(Ques_Round)
        self.Two_Correct.setObjectName(u"Two_Correct")
        self.Two_Correct.setGeometry(QRect(410, 230, 51, 20))
        self.Three_Correct = QCheckBox(Ques_Round)
        self.Three_Correct.setObjectName(u"Three_Correct")
        self.Three_Correct.setGeometry(QRect(410, 270, 51, 20))
        self.Fourth_Correct = QCheckBox(Ques_Round)
        self.Fourth_Correct.setObjectName(u"Fourth_Correct")
        self.Fourth_Correct.setGeometry(QRect(410, 310, 51, 20))
        self.label_29 = QLabel(Ques_Round)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(370, 150, 111, 28))
        self.quest_text = QLineEdit(Ques_Round)
        self.quest_text.setObjectName(u"quest_text")
        self.quest_text.setGeometry(QRect(80, 110, 311, 31))

        self.retranslateUi(Ques_Round)

        QMetaObject.connectSlotsByName(Ques_Round)
    # setupUi

    def retranslateUi(self, Ques_Round):
        Ques_Round.setWindowTitle(QCoreApplication.translate("Ques_Round", u"\u0412\u043e\u043f\u0440\u043e\u0441\u044b \u0434\u043b\u044f \u0440\u0430\u0443\u043d\u0434\u0430", None))
        self.Add_Quest.setText(QCoreApplication.translate("Ques_Round", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.Del_Quest.setText(QCoreApplication.translate("Ques_Round", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_22.setText(QCoreApplication.translate("Ques_Round", u"\u0422\u0438\u043f \u0440\u0430\u0443\u043d\u0434\u0430", None))
        self.Type_Quest.setItemText(0, QCoreApplication.translate("Ques_Round", u"select", None))
        self.Type_Quest.setItemText(1, QCoreApplication.translate("Ques_Round", u"text", None))

        self.label_23.setText(QCoreApplication.translate("Ques_Round", u"\u0412\u043e\u043f\u0440\u043e\u0441", None))
        self.label_24.setText(QCoreApplication.translate("Ques_Round", u"\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043e\u0442\u0432\u0435\u0442\u0430", None))
        self.label_25.setText(QCoreApplication.translate("Ques_Round", u"\u041f\u0435\u0440\u0432\u044b\u0439", None))
        self.label_26.setText(QCoreApplication.translate("Ques_Round", u"\u0412\u0442\u043e\u0440\u043e\u0439", None))
        self.label_27.setText(QCoreApplication.translate("Ques_Round", u"\u0422\u0440\u0435\u0442\u0438\u0439", None))
        self.label_28.setText(QCoreApplication.translate("Ques_Round", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0442\u044b\u0439", None))
        self.One_Correct.setText("")
        self.Two_Correct.setText("")
        self.Three_Correct.setText("")
        self.Fourth_Correct.setText("")
        self.label_29.setText(QCoreApplication.translate("Ques_Round", u"\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442", None))
    # retranslateUi

    def closeEvent(self, event):
        print("test")
