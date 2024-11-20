# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_round.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDialog, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_form_round(object):
    def setupUi(self, form_round):
        if not form_round.objectName():
            form_round.setObjectName(u"form_round")
        form_round.resize(309, 564)
        self.All_Question = QListWidget(form_round)
        self.All_Question.setObjectName(u"All_Question")
        self.All_Question.setGeometry(QRect(30, 170, 241, 341))
        self.All_Question.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.SelectedClicked)
        self.All_Question.setProperty(u"showDropIndicator", False)
        self.Del_Quest = QPushButton(form_round)
        self.Del_Quest.setObjectName(u"Del_Quest")
        self.Del_Quest.setGeometry(QRect(160, 520, 111, 24))
        self.Del_Quest.setAutoRepeat(False)
        self.Del_Quest.setAutoExclusive(False)
        self.Del_Quest.setAutoRepeatDelay(388)
        self.Del_Quest.setAutoRepeatInterval(31)
        self.Add_Quest = QPushButton(form_round)
        self.Add_Quest.setObjectName(u"Add_Quest")
        self.Add_Quest.setGeometry(QRect(30, 520, 121, 24))
        self.Blitz_label = QLabel(form_round)
        self.Blitz_label.setObjectName(u"Blitz_label")
        self.Blitz_label.setGeometry(QRect(70, 130, 81, 28))
        self.Test_Round = QCheckBox(form_round)
        self.Test_Round.setObjectName(u"Test_Round")
        self.Test_Round.setGeometry(QRect(180, 50, 21, 28))
        self.Second_Round = QSpinBox(form_round)
        self.Second_Round.setObjectName(u"Second_Round")
        self.Second_Round.setGeometry(QRect(160, 90, 71, 22))
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
        self.label_23 = QLabel(form_round)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(70, 50, 91, 28))
        self.label_24 = QLabel(form_round)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(70, 90, 81, 28))
        self.Blitz_Score = QSpinBox(form_round)
        self.Blitz_Score.setObjectName(u"Blitz_Score")
        self.Blitz_Score.setGeometry(QRect(160, 130, 71, 22))
        self.Blitz_Score.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.Blitz_Score.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.Blitz_Score.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Blitz_Score.setWrapping(True)
        self.Blitz_Score.setFrame(True)
        self.Blitz_Score.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Blitz_Score.setAccelerated(True)
        self.Blitz_Score.setKeyboardTracking(True)
        self.Blitz_Score.setMaximum(300)
        self.Blitz_Score.setSingleStep(1)
        self.Blitz_Score.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Blitz_Score.setValue(50)
        self.Type_Round = QComboBox(form_round)
        self.Type_Round.addItem("")
        self.Type_Round.addItem("")
        self.Type_Round.setObjectName(u"Type_Round")
        self.Type_Round.setGeometry(QRect(160, 10, 91, 28))
        self.label_22 = QLabel(form_round)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(70, 10, 70, 28))

        self.retranslateUi(form_round)

        QMetaObject.connectSlotsByName(form_round)
    # setupUi

    def retranslateUi(self, form_round):
        form_round.setWindowTitle(QCoreApplication.translate("form_round", u"\u0420\u0430\u0443\u043d\u0434", None))
        self.Del_Quest.setText(QCoreApplication.translate("form_round", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441", None))
        self.Add_Quest.setText(QCoreApplication.translate("form_round", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441", None))
        self.Blitz_label.setText(QCoreApplication.translate("form_round", u"\u041e\u0447\u043a\u0438 \u0431\u043b\u0438\u0446", None))
        self.Test_Round.setText("")
        self.label_23.setText(QCoreApplication.translate("form_round", u"\u0422\u0435\u0441\u0442\u043e\u0432\u044b\u0439 \u0440\u0430\u0443\u043d\u0434", None))
        self.label_24.setText(QCoreApplication.translate("form_round", u"\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0443\u043d\u0434\u0430", None))
        self.Type_Round.setItemText(0, QCoreApplication.translate("form_round", u"classical", None))
        self.Type_Round.setItemText(1, QCoreApplication.translate("form_round", u"blitz", None))

        self.label_22.setText(QCoreApplication.translate("form_round", u"\u0422\u0438\u043f \u0440\u0430\u0443\u043d\u0434\u0430", None))
    # retranslateUi

