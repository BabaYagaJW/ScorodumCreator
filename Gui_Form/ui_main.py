# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_test.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(629, 364)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setEnabled(False)
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionSave_as.setCheckable(False)
        self.actionSave_as.setChecked(False)
        self.actionSave_as.setEnabled(True)
        self.actionSave_as.setShortcutContext(Qt.ShortcutContext.WidgetWithChildrenShortcut)
        self.actionSave_as.setAutoRepeat(False)
        self.actionSave_as.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionSave_as.setPriority(QAction.Priority.LowPriority)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionClose.setEnabled(False)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew.setCheckable(False)
        self.actionNew.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 951, 581))
        self.tabWidget.setMaximumSize(QSize(951, 581))
        self.tabWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.Main_Setting = QWidget()
        self.Main_Setting.setObjectName(u"Main_Setting")
        self.Mail_OnClick = QCheckBox(self.Main_Setting)
        self.Mail_OnClick.setObjectName(u"Mail_OnClick")
        self.Mail_OnClick.setGeometry(QRect(210, 30, 16, 31))
        self.label = QLabel(self.Main_Setting)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 181, 31))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label_2 = QLabel(self.Main_Setting)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 30, 101, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.Main_Setting)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 100, 131, 16))
        self.label_4 = QLabel(self.Main_Setting)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 140, 81, 16))
        self.label_5 = QLabel(self.Main_Setting)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 190, 91, 16))
        self.label_6 = QLabel(self.Main_Setting)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 230, 49, 16))
        self.label_7 = QLabel(self.Main_Setting)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(280, 270, 111, 16))
        self.label_8 = QLabel(self.Main_Setting)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 80, 171, 20))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_8.setFont(font2)
        self.label_9 = QLabel(self.Main_Setting)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 120, 61, 16))
        self.label_19 = QLabel(self.Main_Setting)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 150, 41, 16))
        self.label_20 = QLabel(self.Main_Setting)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 180, 41, 16))
        self.label_21 = QLabel(self.Main_Setting)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 210, 41, 16))
        self.Name_Game = QLineEdit(self.Main_Setting)
        self.Name_Game.setObjectName(u"Name_Game")
        self.Name_Game.setGeometry(QRect(90, 120, 113, 22))
        self.Theme_Game = QLineEdit(self.Main_Setting)
        self.Theme_Game.setObjectName(u"Theme_Game")
        self.Theme_Game.setGeometry(QRect(90, 150, 113, 22))
        self.Client_Game = QLineEdit(self.Main_Setting)
        self.Client_Game.setObjectName(u"Client_Game")
        self.Client_Game.setGeometry(QRect(90, 180, 113, 22))
        self.Date_Game = QLineEdit(self.Main_Setting)
        self.Date_Game.setObjectName(u"Date_Game")
        self.Date_Game.setGeometry(QRect(90, 210, 113, 22))
        self.remove_answer = QSpinBox(self.Main_Setting)
        self.remove_answer.setObjectName(u"remove_answer")
        self.remove_answer.setGeometry(QRect(430, 100, 121, 22))
        self.remove_answer.setWrapping(False)
        self.remove_answer.setFrame(True)
        self.remove_answer.setReadOnly(False)
        self.remove_answer.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.remove_answer.setKeyboardTracking(True)
        self.remove_answer.setMinimum(0)
        self.remove_answer.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.remove_answer.setValue(10)
        self.one_for_all = QSpinBox(self.Main_Setting)
        self.one_for_all.setObjectName(u"one_for_all")
        self.one_for_all.setGeometry(QRect(430, 140, 121, 22))
        self.one_for_all.setMinimum(0)
        self.one_for_all.setValue(2)
        self.question_bet = QSpinBox(self.Main_Setting)
        self.question_bet.setObjectName(u"question_bet")
        self.question_bet.setGeometry(QRect(430, 190, 121, 22))
        self.question_bet.setMinimum(0)
        self.question_bet.setValue(1)
        self.all_in = QSpinBox(self.Main_Setting)
        self.all_in.setObjectName(u"all_in")
        self.all_in.setGeometry(QRect(430, 230, 121, 22))
        self.all_in.setMinimum(0)
        self.all_in.setValue(1)
        self.team_bet = QSpinBox(self.Main_Setting)
        self.team_bet.setObjectName(u"team_bet")
        self.team_bet.setGeometry(QRect(430, 270, 121, 22))
        self.team_bet.setMinimum(0)
        self.team_bet.setValue(1)
        self.tabWidget.addTab(self.Main_Setting, "")
        self.Round_Setting = QWidget()
        self.Round_Setting.setObjectName(u"Round_Setting")
        self.label_22 = QLabel(self.Round_Setting)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(50, 70, 70, 28))
        self.label_23 = QLabel(self.Round_Setting)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(50, 120, 91, 28))
        self.Test_Round = QCheckBox(self.Round_Setting)
        self.Test_Round.setObjectName(u"Test_Round")
        self.Test_Round.setGeometry(QRect(160, 120, 21, 28))
        self.label_24 = QLabel(self.Round_Setting)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(50, 170, 81, 28))
        self.Type_Round = QComboBox(self.Round_Setting)
        self.Type_Round.addItem("")
        self.Type_Round.addItem("")
        self.Type_Round.setObjectName(u"Type_Round")
        self.Type_Round.setGeometry(QRect(140, 70, 70, 28))
        self.Add_Round = QPushButton(self.Round_Setting)
        self.Add_Round.setObjectName(u"Add_Round")
        self.Add_Round.setGeometry(QRect(320, 280, 75, 24))
        self.Del_Round = QPushButton(self.Round_Setting)
        self.Del_Round.setObjectName(u"Del_Round")
        self.Del_Round.setGeometry(QRect(440, 280, 75, 24))
        self.All_Round = QListWidget(self.Round_Setting)
        self.All_Round.setObjectName(u"All_Round")
        self.All_Round.setGeometry(QRect(300, 10, 241, 261))
        self.All_Round.setFrameShape(QFrame.Shape.Box)
        self.All_Round.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.SelectedClicked)
        self.Second_Round = QSpinBox(self.Round_Setting)
        self.Second_Round.setObjectName(u"Second_Round")
        self.Second_Round.setGeometry(QRect(140, 170, 71, 22))
        self.Second_Round.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.Second_Round.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.Second_Round.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Second_Round.setWrapping(True)
        self.Second_Round.setFrame(True)
        self.Second_Round.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Second_Round.setAccelerated(True)
        self.Second_Round.setKeyboardTracking(True)
        self.Second_Round.setSingleStep(1)
        self.Second_Round.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.Second_Round.setValue(50)
        self.tabWidget.addTab(self.Round_Setting, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 629, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionClose)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ScorodumCreator", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
#if QT_CONFIG(shortcut)
        self.actionSave_as.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.Mail_OnClick.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0442\u044c \u043f\u043e\u0447\u0442\u0443 \u0443 \u0438\u0433\u0440\u043e\u043a\u043e\u0432", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u043a\u0442\u0438\u043a\u0438:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c \u043d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0434\u0438\u043d \u0437\u0430 \u0432\u0441\u0435\u0445", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0432\u043a\u0430 \u043d\u0430 \u0431\u043e\u0447\u043a\u0443", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430-\u0431\u0430\u043d\u043a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0432\u043a\u0430 \u043d\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0443", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u0438\u0433\u0440\u0435:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.Name_Game.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.Theme_Game.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.Client_Game.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.Date_Game.setText(QCoreApplication.translate("MainWindow", u"02.10.2024", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main_Setting), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0440\u0430\u0443\u043d\u0434\u0430", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442\u043e\u0432\u044b\u0439 \u0440\u0430\u0443\u043d\u0434", None))
        self.Test_Round.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0443\u043d\u0434\u0430", None))
        self.Type_Round.setItemText(0, QCoreApplication.translate("MainWindow", u"classical", None))
        self.Type_Round.setItemText(1, QCoreApplication.translate("MainWindow", u"blitz", None))

        self.Add_Round.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.Del_Round.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Round_Setting), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0443\u043d\u0434\u044b", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi


