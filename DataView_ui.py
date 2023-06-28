# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class DataViewWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1017, 378)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.EMG = PlotWidget(self.centralwidget)
        self.EMG.setObjectName(u"EMG")
        self.EMG.setGeometry(QRect(90, 90, 831, 171))
        self.EMG.setMinimumSize(QSize(211, 111))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 161, 71))
        self.label.setMinimumSize(QSize(161, 71))
        font = QFont()
        font.setFamily(u"Adobe Heiti Std")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.ChannelNum = QLabel(self.centralwidget)
        self.ChannelNum.setObjectName(u"ChannelNum")
        self.ChannelNum.setGeometry(QRect(100, 10, 161, 71))
        self.ChannelNum.setMinimumSize(QSize(161, 71))
        self.ChannelNum.setFont(font)
        self.ChannelNum.setAlignment(Qt.AlignCenter)
        self.NEXT = QPushButton(self.centralwidget)
        self.NEXT.setObjectName(u"NEXT")
        self.NEXT.setGeometry(QRect(930, 90, 61, 151))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setWeight(75)
        self.NEXT.setFont(font1)
        self.NEXT.setStyleSheet(u"background-color: rgb(21, 85, 154);\n"
"color: rgb(255, 255, 255);")
        self.PREV = QPushButton(self.centralwidget)
        self.PREV.setObjectName(u"PREV")
        self.PREV.setGeometry(QRect(20, 100, 61, 151))
        self.PREV.setFont(font1)
        self.PREV.setStyleSheet(u"background-color: rgb(21, 85, 154);\n"
"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1017, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u901a\u9053\u53f7\uff1a", None))
        self.ChannelNum.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.NEXT.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.PREV.setText(QCoreApplication.translate("MainWindow", u"<", None))
    # retranslateUi

