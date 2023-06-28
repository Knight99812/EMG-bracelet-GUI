# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'showResult_CD.ui'
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
        MainWindow.resize(433, 506)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamily(u"Adobe Heiti Std")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.SubjectID_2 = QLineEdit(self.centralwidget)
        self.SubjectID_2.setObjectName(u"SubjectID_2")
        font1 = QFont()
        font1.setFamily(u"Adobe Heiti Std")
        font1.setPointSize(10)
        self.SubjectID_2.setFont(font1)
        self.SubjectID_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.SubjectID_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.SubjectID = QLineEdit(self.centralwidget)
        self.SubjectID.setObjectName(u"SubjectID")
        self.SubjectID.setFont(font1)
        self.SubjectID.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.SubjectID)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.comboBox_2.setFont(font2)
        self.comboBox_2.setStyleSheet(u"font: 8pt \"Arial\";")
        self.comboBox_2.setEditable(True)

        self.horizontalLayout_4.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 30))
        self.comboBox_3.setFont(font2)
        self.comboBox_3.setStyleSheet(u"font: 8pt \"Arial\";")
        self.comboBox_3.setEditable(True)

        self.horizontalLayout_4.addWidget(self.comboBox_3)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamily(u"Adobe \u9ed1\u4f53 Std R")
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.comboBox.setFont(font3)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setStyleSheet(u"font: 9pt \"Adobe \u9ed1\u4f53 Std R\";")
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QComboBox.InsertAtBottom)

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.GestureResultFig = QLabel(self.centralwidget)
        self.GestureResultFig.setObjectName(u"GestureResultFig")

        self.verticalLayout_2.addWidget(self.GestureResultFig)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.speed = QLabel(self.centralwidget)
        self.speed.setObjectName(u"speed")
        self.speed.setFont(font)
        self.speed.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.speed)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setMinimumSize(QSize(151, 41))
        self.Start.setStyleSheet(u"font: 9pt \"Adobe \u9ed1\u4f53 Std R\";\n"
"background-color: rgb(21, 85, 154);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.Start)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.Stop = QPushButton(self.centralwidget)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setMinimumSize(QSize(151, 41))
        self.Stop.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(242, 90, 71);\n"
"font: 9pt \"Adobe \u9ed1\u4f53 Std R\";")

        self.horizontalLayout_8.addWidget(self.Stop)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.verticalLayout_3.setStretch(0, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 433, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u57dfID", None))
        self.SubjectID_2.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u8bd5ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u8bd5ID", None))
        self.SubjectID.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u8bd5ID", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"mode", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"high-accuracy", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"high-sensitivity", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("MainWindow", u"high-accuracy", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"normal", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"cross-day", None))

        self.comboBox_3.setCurrentText(QCoreApplication.translate("MainWindow", u"normal", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\u53f7", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"1", None))
        self.GestureResultFig.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
        self.speed.setText(QCoreApplication.translate("MainWindow", u"\u00d71", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6d4b\u8bd5", None))
        self.Stop.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u6d4b\u8bd5", None))
    # retranslateUi

