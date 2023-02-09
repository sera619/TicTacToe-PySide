# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(702, 608)
        icon = QIcon()
        icon.addFile(u":/icons/img/gameicon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"\n"
"background-color: rgba(0,0,0,0);\n"
"}\n"
"#centralwidget{\n"
"border-radius: 50%;\n"
"	\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(181, 0, 0, 235), stop:0.494318 rgba(55, 0, 0, 235), stop:0.994318 rgba(4, 0, 0, 235));\n"
"}\n"
"#stackedWidget{\n"
"border-radius: 50%;\n"
"}\n"
"#menuView{\n"
"background-color: rgba(0,0,0,0);\n"
"\n"
"}\n"
"#newGameView{\n"
"background-color: rgba(0,0,0,0);\n"
"\n"
"}\n"
"#gameView{\n"
"background-color: rgba(0,0,0,0);\n"
"}\n"
"#tetView{\n"
"background-color: rgba(0,0,0,0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(14, 14, 14, 14)
        self.topFrame = QFrame(self.centralwidget)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setMouseTracking(False)
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.topFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.topFrame)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMouseTracking(False)
        self.headerFrame.setStyleSheet(u"")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.headerFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.headerFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Queen of Camelot 2.0"])
        font.setPointSize(48)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.topFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.gameView = QWidget()
        self.gameView.setObjectName(u"gameView")
        self.gameView.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.gameView)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.gameView)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gameStateLabel = QLabel(self.frame_7)
        self.gameStateLabel.setObjectName(u"gameStateLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gameStateLabel.sizePolicy().hasHeightForWidth())
        self.gameStateLabel.setSizePolicy(sizePolicy)
        self.gameStateLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(85, 170, 255);\n"
"	font: 21pt \"PhrasticMedium\";\n"
"}")
        self.gameStateLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.gameStateLabel)

        self.turnLabel = QLabel(self.frame_7)
        self.turnLabel.setObjectName(u"turnLabel")
        sizePolicy.setHeightForWidth(self.turnLabel.sizePolicy().hasHeightForWidth())
        self.turnLabel.setSizePolicy(sizePolicy)
        self.turnLabel.setMinimumSize(QSize(0, 30))
        self.turnLabel.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"PhrasticMedium"])
        font1.setPointSize(19)
        font1.setBold(False)
        font1.setItalic(False)
        self.turnLabel.setFont(font1)
        self.turnLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(0, 193, 0);\n"
"	font: 19pt \"PhrasticMedium\";\n"
"}")
        self.turnLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.turnLabel)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_3 = QFrame(self.frame_8)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setStyleSheet(u"QFrame{\n"
"border-radius: 25px;\n"
"border:1px solid rgba(234, 156, 0, 180);\n"
"\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"font: 16pt \"PhrasticMedium\";\n"
"}\n"
"#frame_6{\n"
"	background-color: rgba(11, 11, 11, 180);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setFamilies([u"PhrasticMedium"])
        font2.setPointSize(26)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"font: 26pt \"PhrasticMedium\";	")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.p2ScoreLcd = QLCDNumber(self.frame_6)
        self.p2ScoreLcd.setObjectName(u"p2ScoreLcd")
        self.p2ScoreLcd.setMinimumSize(QSize(70, 35))
        self.p2ScoreLcd.setStyleSheet(u"QLCDNumber{\n"
"color: rgb(0, 85, 255);\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.p2ScoreLcd.setFrameShadow(QFrame.Plain)
        self.p2ScoreLcd.setDigitCount(2)
        self.p2ScoreLcd.setMode(QLCDNumber.Dec)
        self.p2ScoreLcd.setSegmentStyle(QLCDNumber.Flat)
        self.p2ScoreLcd.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.p2ScoreLcd, 2, 2, 1, 1)

        self.tttRoundLCD = QLCDNumber(self.frame_6)
        self.tttRoundLCD.setObjectName(u"tttRoundLCD")
        self.tttRoundLCD.setMinimumSize(QSize(50, 35))
        self.tttRoundLCD.setStyleSheet(u"color: rgb(225, 150, 0);	\n"
"border: none;")
        self.tttRoundLCD.setDigitCount(2)
        self.tttRoundLCD.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.tttRoundLCD, 6, 2, 1, 1)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"		color: rgb(225, 150, 0);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.player1Label = QLabel(self.frame_6)
        self.player1Label.setObjectName(u"player1Label")
        self.player1Label.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.player1Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.player1Label, 1, 0, 1, 1)

        self.p1ScoreLcd = QLCDNumber(self.frame_6)
        self.p1ScoreLcd.setObjectName(u"p1ScoreLcd")
        self.p1ScoreLcd.setMinimumSize(QSize(70, 35))
        self.p1ScoreLcd.setStyleSheet(u"QLCDNumber{\n"
"	border:none;\n"
"	color: rgb(255, 0, 0);\n"
"}")
        self.p1ScoreLcd.setFrameShape(QFrame.Box)
        self.p1ScoreLcd.setFrameShadow(QFrame.Plain)
        self.p1ScoreLcd.setDigitCount(2)
        self.p1ScoreLcd.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.p1ScoreLcd, 2, 0, 1, 1)

        self.player2Label = QLabel(self.frame_6)
        self.player2Label.setObjectName(u"player2Label")
        self.player2Label.setStyleSheet(u"color: rgb(0, 85, 127);")
        self.player2Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.player2Label, 1, 2, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"font: 26pt \"PhrasticMedium\";\n"
"color: rgb(255, 0, 0);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gameField = QFrame(self.frame_3)
        self.gameField.setObjectName(u"gameField")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gameField.sizePolicy().hasHeightForWidth())
        self.gameField.setSizePolicy(sizePolicy2)
        self.gameField.setMinimumSize(QSize(350, 350))
        self.gameField.setMaximumSize(QSize(325, 325))
        font3 = QFont()
        font3.setKerning(True)
        self.gameField.setFont(font3)
        self.gameField.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 37px;\n"
"	font-weight: bold;\n"
"	color:rgb(255, 85, 0);\n"
"	font: 32pt \"Street Writer (noah)\";\n"
"	background-color: qlineargradient(spread:pad, x1:0.5175, y1:0.517, x2:0.983, y2:0.965909, stop:0.0738636 rgba(0, 0, 0, 226), stop:0.664773 rgba(33, 33, 33, 222), stop:1 rgba(57, 57, 57, 222));\n"
"}\n"
"QPushButton::Hover{\n"
"	color:#FFF;\n"
"	font-size: 56px;\n"
"	border: 2px solid orange;\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 0, 160), stop:0.994318 rgba(148, 49, 0, 160));\n"
"}\n"
"QPushButton::Disabled{\n"
"	background-color: rgba(67, 67, 67, 75);\n"
"	color:black;\n"
"}\n"
"QPushButton:Pressed{\n"
"	border-radius:37px;\n"
"}\n"
"#gameField{\n"
"	background-color: rgba(11, 11, 11, 180);\n"
"	border-radius: 25px;\n"
"\n"
"border:1px solid rgba(234, 156, 0, 180);\n"
"}")
        self.gameFieldGrid = QGridLayout(self.gameField)
        self.gameFieldGrid.setSpacing(15)
        self.gameFieldGrid.setObjectName(u"gameFieldGrid")
        self.gameFieldGrid.setContentsMargins(15, 15, 15, 15)
        self.gridBtn_8 = QPushButton(self.gameField)
        self.gridBtn_8.setObjectName(u"gridBtn_8")
        self.gridBtn_8.setMinimumSize(QSize(75, 75))
        self.gridBtn_8.setMaximumSize(QSize(85, 85))
        font4 = QFont()
        font4.setFamilies([u"Street Writer (noah)"])
        font4.setPointSize(32)
        font4.setBold(False)
        font4.setItalic(False)
        self.gridBtn_8.setFont(font4)
        self.gridBtn_8.setFocusPolicy(Qt.ClickFocus)

        self.gameFieldGrid.addWidget(self.gridBtn_8, 2, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridBtn_2 = QPushButton(self.gameField)
        self.gridBtn_2.setObjectName(u"gridBtn_2")
        self.gridBtn_2.setEnabled(True)
        self.gridBtn_2.setMinimumSize(QSize(75, 75))
        self.gridBtn_2.setMaximumSize(QSize(85, 85))
        self.gridBtn_2.setFont(font4)
        self.gridBtn_2.setFocusPolicy(Qt.ClickFocus)

        self.gameFieldGrid.addWidget(self.gridBtn_2, 0, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridBtn_3 = QPushButton(self.gameField)
        self.gridBtn_3.setObjectName(u"gridBtn_3")
        self.gridBtn_3.setMinimumSize(QSize(75, 75))
        self.gridBtn_3.setMaximumSize(QSize(85, 85))
        self.gridBtn_3.setFont(font4)
        self.gridBtn_3.setFocusPolicy(Qt.ClickFocus)

        self.gameFieldGrid.addWidget(self.gridBtn_3, 0, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridBtn_9 = QPushButton(self.gameField)
        self.gridBtn_9.setObjectName(u"gridBtn_9")
        self.gridBtn_9.setMinimumSize(QSize(75, 75))
        self.gridBtn_9.setMaximumSize(QSize(85, 85))
        self.gridBtn_9.setFont(font4)
        self.gridBtn_9.setFocusPolicy(Qt.ClickFocus)

        self.gameFieldGrid.addWidget(self.gridBtn_9, 2, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridBtn_5 = QPushButton(self.gameField)
        self.gridBtn_5.setObjectName(u"gridBtn_5")
        self.gridBtn_5.setMinimumSize(QSize(75, 75))
        self.gridBtn_5.setMaximumSize(QSize(85, 85))
        self.gridBtn_5.setFont(font4)
        self.gridBtn_5.setFocusPolicy(Qt.ClickFocus)

        self.gameFieldGrid.addWidget(self.gridBtn_5, 1, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridBtn_6 = QPushButton(self.gameField)
        self.gridBtn_6.setObjectName(u"gridBtn_6")
        self.gridBtn_6.setMinimumSize(QSize(75, 75))
        self.gridBtn_6.setMaximumSize(QSize(85, 85))
        self.gridBtn_6.setFont(font4)
        self.gridBtn_6.setFocusPolicy(Qt.ClickFocus)
        self.gridBtn_6.setStyleSheet(u"")

        self.gameFieldGrid.addWidget(self.gridBtn_6, 1, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridBtn_1 = QPushButton(self.gameField)
        self.gridBtn_1.setObjectName(u"gridBtn_1")
        sizePolicy2.setHeightForWidth(self.gridBtn_1.sizePolicy().hasHeightForWidth())
        self.gridBtn_1.setSizePolicy(sizePolicy2)
        self.gridBtn_1.setMinimumSize(QSize(75, 75))
        self.gridBtn_1.setMaximumSize(QSize(85, 85))
        self.gridBtn_1.setFont(font4)
        self.gridBtn_1.setFocusPolicy(Qt.ClickFocus)
        self.gridBtn_1.setStyleSheet(u"")
        self.gridBtn_1.setCheckable(False)

        self.gameFieldGrid.addWidget(self.gridBtn_1, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridBtn_4 = QPushButton(self.gameField)
        self.gridBtn_4.setObjectName(u"gridBtn_4")
        self.gridBtn_4.setMinimumSize(QSize(75, 75))
        self.gridBtn_4.setMaximumSize(QSize(85, 85))
        self.gridBtn_4.setFont(font4)
        self.gridBtn_4.setFocusPolicy(Qt.ClickFocus)

        self.gameFieldGrid.addWidget(self.gridBtn_4, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridBtn_7 = QPushButton(self.gameField)
        self.gridBtn_7.setObjectName(u"gridBtn_7")
        self.gridBtn_7.setMinimumSize(QSize(75, 75))
        self.gridBtn_7.setMaximumSize(QSize(85, 85))
        self.gridBtn_7.setFont(font4)
        self.gridBtn_7.setFocusPolicy(Qt.ClickFocus)

        self.gameFieldGrid.addWidget(self.gridBtn_7, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.gameField, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame_8)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setStyleSheet(u"QPushButton {\n"
"    color:#FFF;\n"
"    border: 1px solid orange;\n"
"    padding: 3px 8px;\n"
"	border-radius: 10px;\n"
"	font-weight: 700;\n"
"	font: 14pt \"PhrasticMedium\";\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	color: orange;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border: 1.4px solid orange;\n"
"	border-radius: 15px;\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 0, 160), stop:0.994318 rgba(148, 49, 0, 160));\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, 9, 9)
        self.startBtn = QPushButton(self.frame_5)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setMinimumSize(QSize(125, 35))
        font5 = QFont()
        font5.setFamilies([u"PhrasticMedium"])
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(False)
        self.startBtn.setFont(font5)

        self.horizontalLayout_3.addWidget(self.startBtn)

        self.resetBtn = QPushButton(self.frame_5)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setMinimumSize(QSize(125, 35))
        self.resetBtn.setFont(font5)

        self.horizontalLayout_3.addWidget(self.resetBtn)

        self.menuBtn = QPushButton(self.frame_5)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(125, 35))
        self.menuBtn.setFont(font5)

        self.horizontalLayout_3.addWidget(self.menuBtn)

        self.exitBtn = QPushButton(self.frame_5)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(125, 35))
        self.exitBtn.setFont(font5)

        self.horizontalLayout_3.addWidget(self.exitBtn)


        self.verticalLayout_5.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.gameView)
        self.tetView = QWidget()
        self.tetView.setObjectName(u"tetView")
        self.verticalLayout_15 = QVBoxLayout(self.tetView)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.tetView)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.tetScoreFrame = QFrame(self.frame_14)
        self.tetScoreFrame.setObjectName(u"tetScoreFrame")
        sizePolicy1.setHeightForWidth(self.tetScoreFrame.sizePolicy().hasHeightForWidth())
        self.tetScoreFrame.setSizePolicy(sizePolicy1)
        self.tetScoreFrame.setMaximumSize(QSize(16777215, 16777215))
        self.tetScoreFrame.setFrameShape(QFrame.StyledPanel)
        self.tetScoreFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.tetScoreFrame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tetStateLabel = QLabel(self.tetScoreFrame)
        self.tetStateLabel.setObjectName(u"tetStateLabel")
        self.tetStateLabel.setStyleSheet(u"font: 28px \"PhrasticMedium\";\n"
"color:rgb(59, 177, 0);")
        self.tetStateLabel.setAlignment(Qt.AlignCenter)
        self.tetStateLabel.setMargin(5)

        self.verticalLayout_17.addWidget(self.tetStateLabel, 0, Qt.AlignTop)

        self.nextTetLabel = QLabel(self.tetScoreFrame)
        self.nextTetLabel.setObjectName(u"nextTetLabel")
        self.nextTetLabel.setScaledContents(False)
        self.nextTetLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nextTetLabel.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_17.addWidget(self.nextTetLabel)

        self.label_11 = QLabel(self.tetScoreFrame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.tetScoreLCD = QLCDNumber(self.tetScoreFrame)
        self.tetScoreLCD.setObjectName(u"tetScoreLCD")
        sizePolicy1.setHeightForWidth(self.tetScoreLCD.sizePolicy().hasHeightForWidth())
        self.tetScoreLCD.setSizePolicy(sizePolicy1)
        self.tetScoreLCD.setMinimumSize(QSize(220, 40))
        self.tetScoreLCD.setMaximumSize(QSize(220, 40))
        self.tetScoreLCD.setFrameShape(QFrame.StyledPanel)
        self.tetScoreLCD.setMode(QLCDNumber.Dec)
        self.tetScoreLCD.setSegmentStyle(QLCDNumber.Flat)
        self.tetScoreLCD.setProperty("intValue", 500000)

        self.verticalLayout_17.addWidget(self.tetScoreLCD, 0, Qt.AlignBottom)

        self.label_13 = QLabel(self.tetScoreFrame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFrameShadow(QFrame.Plain)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_13, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.tetLinesLCD = QLCDNumber(self.tetScoreFrame)
        self.tetLinesLCD.setObjectName(u"tetLinesLCD")
        sizePolicy1.setHeightForWidth(self.tetLinesLCD.sizePolicy().hasHeightForWidth())
        self.tetLinesLCD.setSizePolicy(sizePolicy1)
        self.tetLinesLCD.setMinimumSize(QSize(220, 40))
        self.tetLinesLCD.setMaximumSize(QSize(220, 40))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.tetLinesLCD.setFont(font6)
        self.tetLinesLCD.setFrameShape(QFrame.StyledPanel)
        self.tetLinesLCD.setFrameShadow(QFrame.Raised)
        self.tetLinesLCD.setSmallDecimalPoint(False)
        self.tetLinesLCD.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_17.addWidget(self.tetLinesLCD)

        self.label_12 = QLabel(self.tetScoreFrame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_12, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.tetLvlLCD = QLCDNumber(self.tetScoreFrame)
        self.tetLvlLCD.setObjectName(u"tetLvlLCD")
        sizePolicy1.setHeightForWidth(self.tetLvlLCD.sizePolicy().hasHeightForWidth())
        self.tetLvlLCD.setSizePolicy(sizePolicy1)
        self.tetLvlLCD.setMinimumSize(QSize(220, 40))
        self.tetLvlLCD.setMaximumSize(QSize(220, 40))
        self.tetLvlLCD.setFont(font6)
        self.tetLvlLCD.setFrameShape(QFrame.StyledPanel)
        self.tetLvlLCD.setFrameShadow(QFrame.Raised)
        self.tetLvlLCD.setSmallDecimalPoint(False)
        self.tetLvlLCD.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_17.addWidget(self.tetLvlLCD, 0, Qt.AlignTop)


        self.horizontalLayout_5.addWidget(self.tetScoreFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.tetrisBoardWidget = QWidget(self.frame_14)
        self.tetrisBoardWidget.setObjectName(u"tetrisBoardWidget")
        sizePolicy1.setHeightForWidth(self.tetrisBoardWidget.sizePolicy().hasHeightForWidth())
        self.tetrisBoardWidget.setSizePolicy(sizePolicy1)
        self.tetrisBoardWidget.setMinimumSize(QSize(200, 370))
        self.tetrisBoardWidget.setMaximumSize(QSize(225, 370))

        self.horizontalLayout_5.addWidget(self.tetrisBoardWidget, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.frame_14)

        self.tetBtnFrame = QFrame(self.frame_13)
        self.tetBtnFrame.setObjectName(u"tetBtnFrame")
        self.tetBtnFrame.setMinimumSize(QSize(155, 35))
        self.tetBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.tetBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.tetBtnFrame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.tetStartBtn = QPushButton(self.tetBtnFrame)
        self.tetStartBtn.setObjectName(u"tetStartBtn")
        self.tetStartBtn.setMinimumSize(QSize(155, 35))
        self.tetStartBtn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.tetStartBtn, 0, Qt.AlignBottom)

        self.tetPauseBtn = QPushButton(self.tetBtnFrame)
        self.tetPauseBtn.setObjectName(u"tetPauseBtn")
        self.tetPauseBtn.setMinimumSize(QSize(155, 35))
        self.tetPauseBtn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.tetPauseBtn, 0, Qt.AlignBottom)

        self.tetMenuBtn = QPushButton(self.tetBtnFrame)
        self.tetMenuBtn.setObjectName(u"tetMenuBtn")
        self.tetMenuBtn.setMinimumSize(QSize(155, 35))
        self.tetMenuBtn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.tetMenuBtn, 0, Qt.AlignBottom)

        self.tetExitBtn = QPushButton(self.tetBtnFrame)
        self.tetExitBtn.setObjectName(u"tetExitBtn")
        self.tetExitBtn.setMinimumSize(QSize(155, 35))
        self.tetExitBtn.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.tetExitBtn, 0, Qt.AlignBottom)


        self.verticalLayout_16.addWidget(self.tetBtnFrame, 0, Qt.AlignBottom)


        self.verticalLayout_15.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.tetView)
        self.menuView = QWidget()
        self.menuView.setObjectName(u"menuView")
        self.verticalLayout_7 = QVBoxLayout(self.menuView)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.menuView)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 32pt \"PhrasticMedium\";\n"
"color: rgb(0, 170, 255)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.menuBtnFrame = QFrame(self.frame_4)
        self.menuBtnFrame.setObjectName(u"menuBtnFrame")
        sizePolicy3.setHeightForWidth(self.menuBtnFrame.sizePolicy().hasHeightForWidth())
        self.menuBtnFrame.setSizePolicy(sizePolicy3)
        self.menuBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.menuBtnFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.menuBtnFrame)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.menuNewGameBtn = QPushButton(self.menuBtnFrame)
        self.menuNewGameBtn.setObjectName(u"menuNewGameBtn")
        self.menuNewGameBtn.setMinimumSize(QSize(155, 35))
        self.menuNewGameBtn.setFont(font6)

        self.verticalLayout_11.addWidget(self.menuNewGameBtn, 0, Qt.AlignVCenter)

        self.menuTetBtn = QPushButton(self.menuBtnFrame)
        self.menuTetBtn.setObjectName(u"menuTetBtn")
        self.menuTetBtn.setMinimumSize(QSize(155, 35))

        self.verticalLayout_11.addWidget(self.menuTetBtn)

        self.menuoptionBtn = QPushButton(self.menuBtnFrame)
        self.menuoptionBtn.setObjectName(u"menuoptionBtn")
        self.menuoptionBtn.setMinimumSize(QSize(155, 35))
        self.menuoptionBtn.setFont(font6)

        self.verticalLayout_11.addWidget(self.menuoptionBtn, 0, Qt.AlignVCenter)

        self.menuExitBtn = QPushButton(self.menuBtnFrame)
        self.menuExitBtn.setObjectName(u"menuExitBtn")
        self.menuExitBtn.setMinimumSize(QSize(155, 35))
        self.menuExitBtn.setFont(font6)

        self.verticalLayout_11.addWidget(self.menuExitBtn, 0, Qt.AlignVCenter)


        self.verticalLayout_12.addWidget(self.menuBtnFrame)


        self.verticalLayout_9.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.frame, 0, Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.menuView)
        self.newGameView = QWidget()
        self.newGameView.setObjectName(u"newGameView")
        self.verticalLayout_13 = QVBoxLayout(self.newGameView)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_11 = QFrame(self.newGameView)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 32pt \"PhrasticMedium\";\n"
"color: rgb(0, 170, 255)")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_3)


        self.verticalLayout_13.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.newGameView)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QLabel{\n"
"font: 16pt \"PhrasticMedium\";\n"
"color: rgba(225, 150, 0, 230);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	font: 16pt \"PhrasticMedium\";\n"
"	border-radius: 8px;\n"
"	border:1px solid orange;\n"
"	color: rgba(225, 150, 0, 230);\n"
"	padding:2px;\n"
"	text-align:center;\n"
"\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0.5175, y1:0.517, x2:0.983, y2:0.965909, stop:0.0738636 rgba(0, 0, 0, 226), stop:0.664773 rgba(33, 33, 33, 222), stop:1 rgba(57, 57, 57, 222));\n"
"}\n"
"\n"
"QComboBox{\n"
"font: 16pt \"PhrasticMedium\";\n"
"color: rgba(225, 150, 0, 230);\n"
"	border:1px solid orange;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5175, y1:0.517, x2:0.983, y2:0.965909, stop:0.0738636 rgba(0, 0, 0, 226), stop:0.664773 rgba(33, 33, 33, 222), stop:1 rgba(57, 57, 57, 222));\n"
"	border-radius: 8px;\n"
"padding: 2px;\n"
"padding-right:2px;\n"
"\n"
"}\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_10)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setVerticalSpacing(15)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgba(225, 150, 0, 230);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.p1NameInput = QLineEdit(self.frame_10)
        self.p1NameInput.setObjectName(u"p1NameInput")
        self.p1NameInput.setMaxLength(20)
        self.p1NameInput.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.p1NameInput)

        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgba(225, 150, 0, 230);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.p2NameInput = QLineEdit(self.frame_10)
        self.p2NameInput.setObjectName(u"p2NameInput")
        self.p2NameInput.setMaxLength(20)
        self.p2NameInput.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.p2NameInput)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.p1IconBox = QComboBox(self.frame_10)
        self.p1IconBox.addItem("")
        self.p1IconBox.addItem("")
        self.p1IconBox.addItem("")
        self.p1IconBox.addItem("")
        self.p1IconBox.addItem("")
        self.p1IconBox.setObjectName(u"p1IconBox")
        self.p1IconBox.setMinimumSize(QSize(190, 0))
        self.p1IconBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.p1IconBox)

        self.p2IconBox = QComboBox(self.frame_10)
        self.p2IconBox.addItem("")
        self.p2IconBox.addItem("")
        self.p2IconBox.addItem("")
        self.p2IconBox.addItem("")
        self.p2IconBox.addItem("")
        self.p2IconBox.setObjectName(u"p2IconBox")
        self.p2IconBox.setLayoutDirection(Qt.LeftToRight)
        self.p2IconBox.setMaxCount(999999999)
        self.p2IconBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.p2IconBox)

        self.vsComCheck = QCheckBox(self.frame_10)
        self.vsComCheck.setObjectName(u"vsComCheck")
        self.vsComCheck.setFocusPolicy(Qt.ClickFocus)
        self.vsComCheck.setLayoutDirection(Qt.LeftToRight)
        self.vsComCheck.setStyleSheet(u"font: 14pt \"PhrasticMedium\";\n"
"\n"
"color: rgba(225, 150, 0, 230);")
        self.vsComCheck.setTristate(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.vsComCheck)


        self.verticalLayout_13.addWidget(self.frame_10, 0, Qt.AlignHCenter)

        self.newGameBtnFrame = QFrame(self.newGameView)
        self.newGameBtnFrame.setObjectName(u"newGameBtnFrame")
        self.newGameBtnFrame.setMinimumSize(QSize(0, 0))
        self.newGameBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.newGameBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.newGameBtnFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.startNewGameBtn = QPushButton(self.newGameBtnFrame)
        self.startNewGameBtn.setObjectName(u"startNewGameBtn")
        self.startNewGameBtn.setMinimumSize(QSize(125, 35))
        self.startNewGameBtn.setFont(font6)

        self.horizontalLayout_4.addWidget(self.startNewGameBtn, 0, Qt.AlignHCenter)

        self.startNewGameBackBtn = QPushButton(self.newGameBtnFrame)
        self.startNewGameBackBtn.setObjectName(u"startNewGameBackBtn")
        self.startNewGameBackBtn.setMinimumSize(QSize(125, 35))
        self.startNewGameBackBtn.setFont(font6)

        self.horizontalLayout_4.addWidget(self.startNewGameBackBtn)


        self.verticalLayout_13.addWidget(self.newGameBtnFrame, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.newGameView)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.topFrame)

        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 0, 0, 0)
        self.copyrightLabel = QLabel(self.frame_9)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setStyleSheet(u"color: rgba(140, 140, 140, 190);")

        self.verticalLayout_8.addWidget(self.copyrightLabel, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame_9, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.p2IconBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#ff5500;\">Retro </span><span style=\" font-weight:700; color:#ff0000;\">game </span><span style=\" font-weight:700; color:#aa0000;\">bOx</span></p></body></html>", None))
        self.gameStateLabel.setText("")
        self.turnLabel.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Player 2", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Round", None))
        self.player1Label.setText("")
        self.player2Label.setText(QCoreApplication.translate("MainWindow", u"454", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Player 1", None))
        self.gridBtn_8.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gridBtn_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gridBtn_3.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gridBtn_9.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gridBtn_5.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gridBtn_6.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gridBtn_1.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gridBtn_4.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gridBtn_7.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.tetStateLabel.setText(QCoreApplication.translate("MainWindow", u"Gamestate", None))
        self.nextTetLabel.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Lines", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.tetStartBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tetPauseBtn.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.tetMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.tetExitBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuNewGameBtn.setText(QCoreApplication.translate("MainWindow", u"Tic Tac Toe", None))
        self.menuTetBtn.setText(QCoreApplication.translate("MainWindow", u"Tetris", None))
        self.menuoptionBtn.setText(QCoreApplication.translate("MainWindow", u"Option", None))
        self.menuExitBtn.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Player 1 Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Player 2 Name", None))
        self.label_7.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Player 1 Icon", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Player 2 Icon", None))
        self.p1IconBox.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.p1IconBox.setItemText(1, QCoreApplication.translate("MainWindow", u"O", None))
        self.p1IconBox.setItemText(2, QCoreApplication.translate("MainWindow", u"W", None))
        self.p1IconBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Z", None))
        self.p1IconBox.setItemText(4, QCoreApplication.translate("MainWindow", u"I", None))

        self.p2IconBox.setItemText(0, QCoreApplication.translate("MainWindow", u"O", None))
        self.p2IconBox.setItemText(1, QCoreApplication.translate("MainWindow", u"X", None))
        self.p2IconBox.setItemText(2, QCoreApplication.translate("MainWindow", u"W", None))
        self.p2IconBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Z", None))
        self.p2IconBox.setItemText(4, QCoreApplication.translate("MainWindow", u"I", None))

        self.vsComCheck.setText(QCoreApplication.translate("MainWindow", u"VS Computer?", None))
        self.startNewGameBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.startNewGameBackBtn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.copyrightLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#9d9d9d;\">versiontext</span></p></body></html>", None))
    # retranslateUi

