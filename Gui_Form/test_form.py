# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_form.ui'
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

class Ui_Test_Form(object):
    def setupUi(self, Test_Form):
        if not Test_Form.objectName():
            Test_Form.setObjectName(u"Test_Form")
        Test_Form.resize(509, 307)
        self.label_23 = QLabel(Test_Form)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(50, 30, 70, 28))
        self.Third_Choise = QLineEdit(Test_Form)
        self.Third_Choise.setObjectName(u"Third_Choise")
        self.Third_Choise.setGeometry(QRect(110, 190, 311, 22))
        self.label_24 = QLabel(Test_Form)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(200, 70, 101, 28))
        self.label_25 = QLabel(Test_Form)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(50, 110, 51, 28))
        self.label_26 = QLabel(Test_Form)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(50, 150, 51, 28))
        self.Fourth_Correct = QCheckBox(Test_Form)
        self.Fourth_Correct.setObjectName(u"Fourth_Correct")
        self.Fourth_Correct.setGeometry(QRect(440, 230, 51, 20))
        self.label_28 = QLabel(Test_Form)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(40, 230, 61, 28))
        self.quest_text = QLineEdit(Test_Form)
        self.quest_text.setObjectName(u"quest_text")
        self.quest_text.setGeometry(QRect(110, 30, 311, 31))
        self.quest_text.setClearButtonEnabled(False)
        self.Fourth_Choise = QLineEdit(Test_Form)
        self.Fourth_Choise.setObjectName(u"Fourth_Choise")
        self.Fourth_Choise.setGeometry(QRect(110, 230, 311, 22))
        self.Two_Correct = QCheckBox(Test_Form)
        self.Two_Correct.setObjectName(u"Two_Correct")
        self.Two_Correct.setGeometry(QRect(440, 150, 51, 20))
        self.label_27 = QLabel(Test_Form)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(50, 190, 51, 28))
        self.label_29 = QLabel(Test_Form)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(400, 70, 111, 28))
        self.One_Correct = QCheckBox(Test_Form)
        self.One_Correct.setObjectName(u"One_Correct")
        self.One_Correct.setGeometry(QRect(440, 110, 51, 20))
        self.Two_Choise = QLineEdit(Test_Form)
        self.Two_Choise.setObjectName(u"Two_Choise")
        self.Two_Choise.setGeometry(QRect(110, 150, 311, 22))
        self.Three_Correct = QCheckBox(Test_Form)
        self.Three_Correct.setObjectName(u"Three_Correct")
        self.Three_Correct.setGeometry(QRect(440, 190, 51, 20))
        self.First_Choise = QLineEdit(Test_Form)
        self.First_Choise.setObjectName(u"First_Choise")
        self.First_Choise.setGeometry(QRect(110, 110, 311, 22))
        self.Save_Question = QPushButton(Test_Form)
        self.Save_Question.setObjectName(u"Save_Question")
        self.Save_Question.setGeometry(QRect(210, 270, 75, 24))
        self.edit_type_quest = QComboBox(Test_Form)
        self.edit_type_quest.addItem("")
        self.edit_type_quest.addItem("")
        self.edit_type_quest.setObjectName(u"edit_type_quest")
        self.edit_type_quest.setGeometry(QRect(251, 30, 70, 28))
        self.edit_label = QLabel(Test_Form)
        self.edit_label.setObjectName(u"edit_label")
        self.edit_label.setGeometry(QRect(170, 30, 71, 28))

        self.retranslateUi(Test_Form)

        QMetaObject.connectSlotsByName(Test_Form)
    # setupUi

    def retranslateUi(self, Test_Form):
        Test_Form.setWindowTitle(QCoreApplication.translate("Test_Form", u"Form", None))
        self.label_23.setText(QCoreApplication.translate("Test_Form", u"\u0412\u043e\u043f\u0440\u043e\u0441", None))
        self.label_24.setText(QCoreApplication.translate("Test_Form", u"\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043e\u0442\u0432\u0435\u0442\u0430", None))
        self.label_25.setText(QCoreApplication.translate("Test_Form", u"\u041f\u0435\u0440\u0432\u044b\u0439", None))
        self.label_26.setText(QCoreApplication.translate("Test_Form", u"\u0412\u0442\u043e\u0440\u043e\u0439", None))
        self.Fourth_Correct.setText("")
        self.label_28.setText(QCoreApplication.translate("Test_Form", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0442\u044b\u0439", None))
        self.Two_Correct.setText("")
        self.label_27.setText(QCoreApplication.translate("Test_Form", u"\u0422\u0440\u0435\u0442\u0438\u0439", None))
        self.label_29.setText(QCoreApplication.translate("Test_Form", u"\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442", None))
        self.One_Correct.setText("")
        self.Three_Correct.setText("")
        self.Save_Question.setText(QCoreApplication.translate("Test_Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.edit_type_quest.setItemText(0, QCoreApplication.translate("Test_Form", u"select", None))
        self.edit_type_quest.setItemText(1, QCoreApplication.translate("Test_Form", u"text", None))

        self.edit_label.setText(QCoreApplication.translate("Test_Form", u"\u0422\u0438\u043f \u0432\u043e\u043f\u0440\u043e\u0441\u0430", None))
    # retranslateUi

