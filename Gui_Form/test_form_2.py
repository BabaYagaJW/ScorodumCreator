# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_form_2.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(298, 484)
        self.All_Question = QListWidget(Dialog)
        self.All_Question.setObjectName(u"All_Question")
        self.All_Question.setGeometry(QRect(30, 80, 241, 341))
        self.All_Question.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.SelectedClicked)
        self.All_Question.setProperty(u"showDropIndicator", False)
        self.Del_Quest = QPushButton(Dialog)
        self.Del_Quest.setObjectName(u"Del_Quest")
        self.Del_Quest.setGeometry(QRect(180, 430, 75, 24))
        self.Add_Quest = QPushButton(Dialog)
        self.Add_Quest.setObjectName(u"Add_Quest")
        self.Add_Quest.setGeometry(QRect(50, 430, 75, 24))
        self.label_22 = QLabel(Dialog)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(70, 30, 71, 28))
        self.Type_Quest = QComboBox(Dialog)
        self.Type_Quest.addItem("")
        self.Type_Quest.addItem("")
        self.Type_Quest.setObjectName(u"Type_Quest")
        self.Type_Quest.setGeometry(QRect(151, 30, 70, 28))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Del_Quest.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.Add_Quest.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u0432\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.Type_Quest.setItemText(0, QCoreApplication.translate("Dialog", u"select", None))
        self.Type_Quest.setItemText(1, QCoreApplication.translate("Dialog", u"text", None))

    # retranslateUi
