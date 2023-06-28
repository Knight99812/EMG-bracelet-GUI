# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GestureGuidechoose_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(645, 551)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamily(u"Adobe Heiti Std")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.TrialNum = QLineEdit(self.centralwidget)
        self.TrialNum.setObjectName(u"TrialNum")
        self.TrialNum.setMinimumSize(QSize(75, 31))
        self.TrialNum.setMaximumSize(QSize(90, 40))
        self.TrialNum.setFont(font)
        self.TrialNum.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.TrialNum)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(18, 16777215))
        self.label_5.setStyleSheet(u"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(55, 31))
        self.comboBox.setMaximumSize(QSize(60, 31))
        self.comboBox.setStyleSheet(u"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";")
        self.comboBox.setMaxVisibleItems(60)
        self.comboBox.setMinimumContentsLength(10)
        self.comboBox.setIconSize(QSize(10, 16))

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(81, 31))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.GestureNum = QLineEdit(self.centralwidget)
        self.GestureNum.setObjectName(u"GestureNum")
        self.GestureNum.setMinimumSize(QSize(75, 31))
        self.GestureNum.setMaximumSize(QSize(90, 40))
        self.GestureNum.setFont(font)
        self.GestureNum.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.GestureNum)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(18, 16777215))
        self.label_9.setStyleSheet(u"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";")

        self.horizontalLayout.addWidget(self.label_9)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(41, 31))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.MissionTimer = QLineEdit(self.centralwidget)
        self.MissionTimer.setObjectName(u"MissionTimer")
        self.MissionTimer.setMinimumSize(QSize(148, 29))
        self.MissionTimer.setFont(font)
        self.MissionTimer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.MissionTimer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.SubjectID = QLineEdit(self.centralwidget)
        self.SubjectID.setObjectName(u"SubjectID")
        self.SubjectID.setMaximumSize(QSize(174, 29))
        self.SubjectID.setFont(font)
        self.SubjectID.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.SubjectID)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(151, 41))

        self.verticalLayout_5.addWidget(self.pushButton)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.CurrentGesture = QLineEdit(self.centralwidget)
        self.CurrentGesture.setObjectName(u"CurrentGesture")
        self.CurrentGesture.setMinimumSize(QSize(221, 41))

        self.verticalLayout_2.addWidget(self.CurrentGesture)

        self.CurrentFig = QLabel(self.centralwidget)
        self.CurrentFig.setObjectName(u"CurrentFig")
        self.CurrentFig.setMinimumSize(QSize(221, 191))

        self.verticalLayout_2.addWidget(self.CurrentFig)

        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_8)

        self.NextGesture = QLineEdit(self.centralwidget)
        self.NextGesture.setObjectName(u"NextGesture")
        self.NextGesture.setMinimumSize(QSize(221, 41))

        self.verticalLayout_3.addWidget(self.NextGesture)

        self.NextFig = QLabel(self.centralwidget)
        self.NextFig.setObjectName(u"NextFig")
        self.NextFig.setMinimumSize(QSize(221, 191))

        self.verticalLayout_3.addWidget(self.NextFig)

        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.verticalLayout_6.setStretch(0, 4)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 15)

        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 645, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u52a8\u4f5c\u6b21\u6570", None))
        self.TrialNum.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u6b21\u6570", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"  /", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u52a8\u4f5c\u5e8f\u53f7", None))
        self.GestureNum.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u5e8f\u53f7", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"  /", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"  5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u8ba1\u65f6\u5668", None))
        self.MissionTimer.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u8ba1\u65f6\u5668", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u8bd5ID", None))
        self.SubjectID.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u8bd5ID", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u91c7\u96c6", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u624b\u52bf\u63d0\u793a", None))
        self.CurrentFig.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u624b\u52bf\u63d0\u793a", None))
        self.NextFig.setText("")
    # retranslateUi

