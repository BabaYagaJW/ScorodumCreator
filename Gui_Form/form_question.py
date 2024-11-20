# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_question.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_form_question(object):
    def setupUi(self, form_question):
        if not form_question.objectName():
            form_question.setObjectName(u"form_question")
        form_question.setWindowModality(Qt.WindowModality.WindowModal)
        form_question.resize(513, 315)
        self.label_23 = QLabel(form_question)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(50, 30, 70, 28))
        self.Third_Choise = QLineEdit(form_question)
        self.Third_Choise.setObjectName(u"Third_Choise")
        self.Third_Choise.setGeometry(QRect(110, 190, 311, 22))
        self.label_24 = QLabel(form_question)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(200, 70, 101, 28))
        self.label_25 = QLabel(form_question)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(50, 110, 51, 28))
        self.label_26 = QLabel(form_question)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(50, 150, 51, 28))
        self.Fourth_Correct = QCheckBox(form_question)
        self.Fourth_Correct.setObjectName(u"Fourth_Correct")
        self.Fourth_Correct.setGeometry(QRect(440, 230, 51, 20))
        self.label_28 = QLabel(form_question)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(40, 230, 61, 28))
        self.quest_text = QLineEdit(form_question)
        self.quest_text.setObjectName(u"quest_text")
        self.quest_text.setGeometry(QRect(110, 30, 311, 31))
        self.quest_text.setClearButtonEnabled(False)
        self.Fourth_Choise = QLineEdit(form_question)
        self.Fourth_Choise.setObjectName(u"Fourth_Choise")
        self.Fourth_Choise.setGeometry(QRect(110, 230, 311, 22))
        self.Two_Correct = QCheckBox(form_question)
        self.Two_Correct.setObjectName(u"Two_Correct")
        self.Two_Correct.setGeometry(QRect(440, 150, 51, 20))
        self.label_27 = QLabel(form_question)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(50, 190, 51, 28))
        self.label_29 = QLabel(form_question)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(400, 70, 111, 28))
        self.One_Correct = QCheckBox(form_question)
        self.One_Correct.setObjectName(u"One_Correct")
        self.One_Correct.setGeometry(QRect(440, 110, 51, 20))
        self.Two_Choise = QLineEdit(form_question)
        self.Two_Choise.setObjectName(u"Two_Choise")
        self.Two_Choise.setGeometry(QRect(110, 150, 311, 22))
        self.Three_Correct = QCheckBox(form_question)
        self.Three_Correct.setObjectName(u"Three_Correct")
        self.Three_Correct.setGeometry(QRect(440, 190, 51, 20))
        self.First_Choise = QLineEdit(form_question)
        self.First_Choise.setObjectName(u"First_Choise")
        self.First_Choise.setGeometry(QRect(110, 110, 311, 22))
        self.Save_Question = QPushButton(form_question)
        self.Save_Question.setObjectName(u"Save_Question")
        self.Save_Question.setGeometry(QRect(210, 270, 75, 24))
        self.type_question = QComboBox(form_question)
        self.type_question.addItem("")
        self.type_question.addItem("")
        self.type_question.setObjectName(u"type_question")
        self.type_question.setGeometry(QRect(250, 0, 81, 28))
        self.type_label = QLabel(form_question)
        self.type_label.setObjectName(u"type_label")
        self.type_label.setGeometry(QRect(169, 0, 81, 28))

        self.retranslateUi(form_question)

        QMetaObject.connectSlotsByName(form_question)
    # setupUi

    def retranslateUi(self, form_question):
        form_question.setWindowTitle(QCoreApplication.translate("form_question", u"\u0412\u043e\u043f\u0440\u043e\u0441", None))
        self.label_23.setText(QCoreApplication.translate("form_question", u"\u0412\u043e\u043f\u0440\u043e\u0441", None))
        self.label_24.setText(QCoreApplication.translate("form_question", u"\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043e\u0442\u0432\u0435\u0442\u0430", None))
        self.label_25.setText(QCoreApplication.translate("form_question", u"\u041f\u0435\u0440\u0432\u044b\u0439", None))
        self.label_26.setText(QCoreApplication.translate("form_question", u"\u0412\u0442\u043e\u0440\u043e\u0439", None))
        self.Fourth_Correct.setText("")
        self.label_28.setText(QCoreApplication.translate("form_question", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0442\u044b\u0439", None))
        self.Two_Correct.setText("")
        self.label_27.setText(QCoreApplication.translate("form_question", u"\u0422\u0440\u0435\u0442\u0438\u0439", None))
        self.label_29.setText(QCoreApplication.translate("form_question", u"\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442", None))
        self.One_Correct.setText("")
        self.Three_Correct.setText("")
        self.Save_Question.setText(QCoreApplication.translate("form_question", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.type_question.setItemText(0, QCoreApplication.translate("form_question", u"select", None))
        self.type_question.setItemText(1, QCoreApplication.translate("form_question", u"text", None))

        self.type_label.setText(QCoreApplication.translate("form_question", u"\u0422\u0438\u043f \u0432\u043e\u043f\u0440\u043e\u0441\u0430", None))
    # retranslateUi

