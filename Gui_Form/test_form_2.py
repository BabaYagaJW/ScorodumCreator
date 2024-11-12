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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDialog, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(309, 564)
        self.All_Question = QListWidget(Dialog)
        self.All_Question.setObjectName(u"All_Question")
        self.All_Question.setGeometry(QRect(40, 160, 241, 341))
        self.All_Question.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.SelectedClicked)
        self.All_Question.setProperty(u"showDropIndicator", False)
        self.Del_Quest = QPushButton(Dialog)
        self.Del_Quest.setObjectName(u"Del_Quest")
        self.Del_Quest.setGeometry(QRect(190, 510, 75, 24))
        self.Add_Quest = QPushButton(Dialog)
        self.Add_Quest.setObjectName(u"Add_Quest")
        self.Add_Quest.setGeometry(QRect(60, 510, 75, 24))
        self.label_22 = QLabel(Dialog)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(70, 30, 71, 28))
        self.Type_Quest = QComboBox(Dialog)
        self.Type_Quest.addItem("")
        self.Type_Quest.addItem("")
        self.Type_Quest.setObjectName(u"Type_Quest")
        self.Type_Quest.setGeometry(QRect(151, 30, 70, 28))
        self.Second_Round = QSpinBox(Dialog)
        self.Second_Round.setObjectName(u"Second_Round")
        self.Second_Round.setGeometry(QRect(150, 80, 71, 22))
        self.Second_Round.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.Second_Round.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.Second_Round.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Second_Round.setWrapping(True)
        self.Second_Round.setFrame(True)
        self.Second_Round.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Second_Round.setAccelerated(True)
        self.Second_Round.setKeyboardTracking(True)
        self.Second_Round.setMaximum(300)
        self.Second_Round.setSingleStep(1)
        self.Second_Round.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Second_Round.setValue(50)
        self.label_24 = QLabel(Dialog)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(60, 80, 81, 28))
        self.Blitz_Score_2 = QSpinBox(Dialog)
        self.Blitz_Score_2.setObjectName(u"Blitz_Score_2")
        self.Blitz_Score_2.setGeometry(QRect(150, 120, 71, 22))
        self.Blitz_Score_2.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.Blitz_Score_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.Blitz_Score_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Blitz_Score_2.setWrapping(True)
        self.Blitz_Score_2.setFrame(True)
        self.Blitz_Score_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Blitz_Score_2.setAccelerated(True)
        self.Blitz_Score_2.setKeyboardTracking(True)
        self.Blitz_Score_2.setMaximum(300)
        self.Blitz_Score_2.setSingleStep(1)
        self.Blitz_Score_2.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Blitz_Score_2.setValue(50)
        self.Blitz_label_2 = QLabel(Dialog)
        self.Blitz_label_2.setObjectName(u"Blitz_label_2")
        self.Blitz_label_2.setGeometry(QRect(60, 120, 81, 28))

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

        self.label_24.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0443\u043d\u0434\u0430", None))
        self.Blitz_label_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0447\u043a\u0438 \u0431\u043b\u0438\u0446", None))
    # retranslateUi

