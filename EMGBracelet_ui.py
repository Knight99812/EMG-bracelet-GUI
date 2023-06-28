# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EMGBracelet.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1832, 895)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1088, 792))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(201, 31))
        font = QFont()
        font.setFamily(u"Adobe Heiti Std")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.WindowLen = QComboBox(self.layoutWidget)
        self.WindowLen.addItem("")
        self.WindowLen.addItem("")
        self.WindowLen.addItem("")
        self.WindowLen.setObjectName(u"WindowLen")
        self.WindowLen.setMinimumSize(QSize(111, 31))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.WindowLen.setFont(font1)
        self.WindowLen.setEditable(True)

        self.horizontalLayout_6.addWidget(self.WindowLen)

        self.horizontalSpacer_9 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.comboBox_2.setFont(font2)
        self.comboBox_2.setEditable(True)

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.horizontalSpacer_3 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.source = QLineEdit(self.layoutWidget)
        self.source.setObjectName(u"source")
        font3 = QFont()
        font3.setFamily(u"Adobe Heiti Std")
        font3.setPointSize(10)
        self.source.setFont(font3)
        self.source.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.source)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.SubjectID = QLineEdit(self.layoutWidget)
        self.SubjectID.setObjectName(u"SubjectID")
        self.SubjectID.setMinimumSize(QSize(0, 31))
        self.SubjectID.setMaximumSize(QSize(16777215, 31))
        self.SubjectID.setFont(font3)
        self.SubjectID.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.SubjectID)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 2)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(161, 71))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(111, 31))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.plus = QPushButton(self.layoutWidget)
        self.plus.setObjectName(u"plus")
        self.plus.setMinimumSize(QSize(41, 31))
        font4 = QFont()
        font4.setPointSize(23)
        self.plus.setFont(font4)

        self.horizontalLayout_7.addWidget(self.plus)

        self.minus = QPushButton(self.layoutWidget)
        self.minus.setObjectName(u"minus")
        self.minus.setMinimumSize(QSize(41, 31))
        self.minus.setFont(font4)

        self.horizontalLayout_7.addWidget(self.minus)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.EMG1 = PlotWidget(self.layoutWidget)
        self.EMG1.setObjectName(u"EMG1")
        self.EMG1.setMinimumSize(QSize(211, 111))

        self.verticalLayout.addWidget(self.EMG1)

        self.SNR1 = QLineEdit(self.layoutWidget)
        self.SNR1.setObjectName(u"SNR1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SNR1.sizePolicy().hasHeightForWidth())
        self.SNR1.setSizePolicy(sizePolicy)
        self.SNR1.setFont(font3)
        self.SNR1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.SNR1)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.EMG2 = PlotWidget(self.layoutWidget)
        self.EMG2.setObjectName(u"EMG2")
        self.EMG2.setMinimumSize(QSize(211, 111))

        self.verticalLayout_2.addWidget(self.EMG2)

        self.SNR2 = QLineEdit(self.layoutWidget)
        self.SNR2.setObjectName(u"SNR2")
        self.SNR2.setFont(font3)
        self.SNR2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.SNR2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.EMG3 = PlotWidget(self.layoutWidget)
        self.EMG3.setObjectName(u"EMG3")
        self.EMG3.setMinimumSize(QSize(211, 111))

        self.verticalLayout_3.addWidget(self.EMG3)

        self.SNR3 = QLineEdit(self.layoutWidget)
        self.SNR3.setObjectName(u"SNR3")
        self.SNR3.setMinimumSize(QSize(111, 31))
        self.SNR3.setFont(font3)
        self.SNR3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.SNR3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.EMG4 = PlotWidget(self.layoutWidget)
        self.EMG4.setObjectName(u"EMG4")
        self.EMG4.setMinimumSize(QSize(211, 111))

        self.verticalLayout_4.addWidget(self.EMG4)

        self.SNR4 = QLineEdit(self.layoutWidget)
        self.SNR4.setObjectName(u"SNR4")
        self.SNR4.setMinimumSize(QSize(111, 31))
        self.SNR4.setFont(font3)
        self.SNR4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.SNR4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.EMG5 = PlotWidget(self.layoutWidget)
        self.EMG5.setObjectName(u"EMG5")
        self.EMG5.setMinimumSize(QSize(211, 111))

        self.verticalLayout_5.addWidget(self.EMG5)

        self.SNR5 = QLineEdit(self.layoutWidget)
        self.SNR5.setObjectName(u"SNR5")
        self.SNR5.setMinimumSize(QSize(111, 31))
        self.SNR5.setFont(font3)
        self.SNR5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.SNR5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.EMG6 = PlotWidget(self.layoutWidget)
        self.EMG6.setObjectName(u"EMG6")
        self.EMG6.setMinimumSize(QSize(211, 111))

        self.verticalLayout_6.addWidget(self.EMG6)

        self.SNR6 = QLineEdit(self.layoutWidget)
        self.SNR6.setObjectName(u"SNR6")
        self.SNR6.setMinimumSize(QSize(111, 31))
        self.SNR6.setFont(font3)
        self.SNR6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.SNR6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.EMG7 = PlotWidget(self.layoutWidget)
        self.EMG7.setObjectName(u"EMG7")
        self.EMG7.setMinimumSize(QSize(211, 111))

        self.verticalLayout_7.addWidget(self.EMG7)

        self.SNR7 = QLineEdit(self.layoutWidget)
        self.SNR7.setObjectName(u"SNR7")
        self.SNR7.setMinimumSize(QSize(111, 31))
        self.SNR7.setFont(font3)
        self.SNR7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.SNR7)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.EMG8 = PlotWidget(self.layoutWidget)
        self.EMG8.setObjectName(u"EMG8")
        self.EMG8.setMinimumSize(QSize(211, 111))

        self.verticalLayout_8.addWidget(self.EMG8)

        self.SNR8 = QLineEdit(self.layoutWidget)
        self.SNR8.setObjectName(u"SNR8")
        self.SNR8.setMinimumSize(QSize(111, 31))
        self.SNR8.setFont(font3)
        self.SNR8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.SNR8)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_4)


        self.verticalLayout_13.addLayout(self.verticalLayout_9)


        self.gridLayout.addLayout(self.verticalLayout_13, 1, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(241, 71))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.ACC = PlotWidget(self.layoutWidget)
        self.ACC.setObjectName(u"ACC")
        self.ACC.setMinimumSize(QSize(431, 261))

        self.verticalLayout_10.addWidget(self.ACC)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(241, 71))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.horizontalSpacer_13 = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.GRO = PlotWidget(self.layoutWidget)
        self.GRO.setObjectName(u"GRO")
        self.GRO.setMinimumSize(QSize(431, 261))

        self.verticalLayout_11.addWidget(self.GRO)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)


        self.gridLayout.addLayout(self.verticalLayout_12, 1, 1, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_16 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_16)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(91, 41))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.SNR = QLineEdit(self.layoutWidget)
        self.SNR.setObjectName(u"SNR")
        self.SNR.setMinimumSize(QSize(148, 31))
        self.SNR.setFont(font3)
        self.SNR.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.SNR)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_15 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Start = QPushButton(self.layoutWidget)
        self.Start.setObjectName(u"Start")
        self.Start.setMinimumSize(QSize(151, 41))
        self.Start.setStyleSheet(u"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";\n"
"background-color: rgb(21, 85, 154);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.Start)

        self.Stop = QPushButton(self.layoutWidget)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setMinimumSize(QSize(151, 41))
        self.Stop.setStyleSheet(u"background-color: rgb(242, 90, 71);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";")

        self.horizontalLayout_11.addWidget(self.Stop)

        self.TrainModel = QPushButton(self.layoutWidget)
        self.TrainModel.setObjectName(u"TrainModel")
        self.TrainModel.setMinimumSize(QSize(151, 41))
        self.TrainModel.setStyleSheet(u"background-color: rgb(108, 108, 108);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";\n"
"")

        self.horizontalLayout_11.addWidget(self.TrainModel)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)


        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 0, 1, 2)

        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(1, 3)
        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(1090, 0, 627, 451))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        font5 = QFont()
        font5.setFamily(u"Adobe Heiti Std")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_12.setFont(font5)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_12)

        self.TrialNum = QLineEdit(self.layoutWidget_2)
        self.TrialNum.setObjectName(u"TrialNum")
        self.TrialNum.setMinimumSize(QSize(80, 31))
        self.TrialNum.setMaximumSize(QSize(100, 40))
        self.TrialNum.setFont(font3)
        self.TrialNum.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.TrialNum)

        self.label_13 = QLabel(self.layoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(18, 16777215))
        font6 = QFont()
        font6.setFamily(u"Adobe \u9ed1\u4f53 Std R")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.comboBox = QComboBox(self.layoutWidget_2)
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

        self.horizontalLayout_14.addWidget(self.comboBox)


        self.verticalLayout_16.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(81, 31))
        self.label_3.setFont(font5)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_3)

        self.GestureNum = QLineEdit(self.layoutWidget_2)
        self.GestureNum.setObjectName(u"GestureNum")
        self.GestureNum.setMinimumSize(QSize(80, 31))
        self.GestureNum.setMaximumSize(QSize(100, 40))
        self.GestureNum.setFont(font3)
        self.GestureNum.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.GestureNum)

        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(18, 16777215))
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";")

        self.horizontalLayout_15.addWidget(self.label_14)

        self.label_15 = QLabel(self.layoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(41, 31))
        self.label_15.setFont(font5)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_15)


        self.verticalLayout_16.addLayout(self.horizontalLayout_15)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.horizontalLayout_13.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_16 = QLabel(self.layoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_16)

        self.MissionTimer = QLineEdit(self.layoutWidget_2)
        self.MissionTimer.setObjectName(u"MissionTimer")
        self.MissionTimer.setMinimumSize(QSize(148, 29))
        self.MissionTimer.setFont(font3)
        self.MissionTimer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.MissionTimer)


        self.verticalLayout_17.addLayout(self.horizontalLayout_16)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_17.addItem(self.horizontalSpacer_6)

        self.pushButton = QPushButton(self.layoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(151, 41))
        self.pushButton.setStyleSheet(u"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";\n"
"background-color: rgb(21, 85, 154);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.pushButton)


        self.horizontalLayout_13.addLayout(self.verticalLayout_17)

        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_17 = QLabel(self.layoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font5)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_17)

        self.CurrentGesture = QLineEdit(self.layoutWidget_2)
        self.CurrentGesture.setObjectName(u"CurrentGesture")
        self.CurrentGesture.setMinimumSize(QSize(221, 41))

        self.verticalLayout_18.addWidget(self.CurrentGesture)

        self.CurrentFig = QLabel(self.layoutWidget_2)
        self.CurrentFig.setObjectName(u"CurrentFig")
        self.CurrentFig.setMinimumSize(QSize(221, 191))

        self.verticalLayout_18.addWidget(self.CurrentFig)

        self.verticalLayout_18.setStretch(2, 1)

        self.horizontalLayout_18.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_8)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_18 = QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_18)

        self.NextGesture = QLineEdit(self.layoutWidget_2)
        self.NextGesture.setObjectName(u"NextGesture")
        self.NextGesture.setMinimumSize(QSize(221, 41))

        self.verticalLayout_19.addWidget(self.NextGesture)

        self.NextFig = QLabel(self.layoutWidget_2)
        self.NextFig.setObjectName(u"NextFig")
        self.NextFig.setMinimumSize(QSize(221, 191))

        self.verticalLayout_19.addWidget(self.NextFig)

        self.verticalLayout_19.setStretch(2, 1)

        self.horizontalLayout_18.addLayout(self.verticalLayout_19)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(2, 1)

        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.verticalLayout_14.setStretch(0, 4)
        self.verticalLayout_14.setStretch(1, 15)
        self.layoutWidget_3 = QWidget(self.centralwidget)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(1090, 450, 631, 341))
        self.verticalLayout_40 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_46 = QLabel(self.layoutWidget_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_46)

        self.comboBox_18 = QComboBox(self.layoutWidget_3)
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setMinimumSize(QSize(0, 30))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(8)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.comboBox_18.setFont(font7)
        self.comboBox_18.setStyleSheet(u"font: 8pt \"Arial\";")
        self.comboBox_18.setEditable(True)

        self.horizontalLayout_63.addWidget(self.comboBox_18)


        self.horizontalLayout_62.addLayout(self.horizontalLayout_63)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_39)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_47 = QLabel(self.layoutWidget_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.label_47)

        self.comboBox_20 = QComboBox(self.layoutWidget_3)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setEnabled(True)
        self.comboBox_20.setMinimumSize(QSize(0, 30))
        font8 = QFont()
        font8.setFamily(u"Adobe \u9ed1\u4f53 Std R")
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.comboBox_20.setFont(font8)
        self.comboBox_20.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_20.setStyleSheet(u"font: 9pt \"Adobe \u9ed1\u4f53 Std R\";")
        self.comboBox_20.setEditable(True)
        self.comboBox_20.setInsertPolicy(QComboBox.InsertAtBottom)

        self.horizontalLayout_64.addWidget(self.comboBox_20)

        self.horizontalLayout_64.setStretch(0, 1)
        self.horizontalLayout_64.setStretch(1, 1)

        self.horizontalLayout_62.addLayout(self.horizontalLayout_64)


        self.verticalLayout_41.addLayout(self.horizontalLayout_62)


        self.verticalLayout_40.addLayout(self.verticalLayout_41)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.GestureResultFig = QLabel(self.layoutWidget_3)
        self.GestureResultFig.setObjectName(u"GestureResultFig")

        self.verticalLayout_43.addWidget(self.GestureResultFig)

        self.verticalLayout_43.setStretch(0, 5)

        self.verticalLayout_42.addLayout(self.verticalLayout_43)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.StartTest = QPushButton(self.layoutWidget_3)
        self.StartTest.setObjectName(u"StartTest")
        self.StartTest.setMinimumSize(QSize(151, 41))
        self.StartTest.setStyleSheet(u"font: 9pt \"Adobe \u9ed1\u4f53 Std R\";\n"
"background-color: rgb(21, 85, 154);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_66.addWidget(self.StartTest)

        self.label_48 = QLabel(self.layoutWidget_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.label_48)

        self.speed = QLabel(self.layoutWidget_3)
        self.speed.setObjectName(u"speed")
        font9 = QFont()
        font9.setFamily(u"Adobe Heiti Std")
        font9.setPointSize(14)
        self.speed.setFont(font9)
        self.speed.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.speed)

        self.StopTest = QPushButton(self.layoutWidget_3)
        self.StopTest.setObjectName(u"StopTest")
        self.StopTest.setMinimumSize(QSize(151, 41))
        self.StopTest.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(242, 90, 71);\n"
"font: 9pt \"Adobe \u9ed1\u4f53 Std R\";")

        self.horizontalLayout_66.addWidget(self.StopTest)


        self.verticalLayout_42.addLayout(self.horizontalLayout_66)

        self.verticalLayout_42.setStretch(0, 1)

        self.verticalLayout_40.addLayout(self.verticalLayout_42)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1832, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.WindowLen.setCurrentIndex(1)
        self.comboBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Visualization Window", None))
        self.WindowLen.setItemText(0, QCoreApplication.translate("MainWindow", u"0.1s", None))
        self.WindowLen.setItemText(1, QCoreApplication.translate("MainWindow", u"1s", None))
        self.WindowLen.setItemText(2, QCoreApplication.translate("MainWindow", u"10s", None))

        self.WindowLen.setCurrentText(QCoreApplication.translate("MainWindow", u"1s", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"normal", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"cross-day", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("MainWindow", u"normal", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u57df", None))
        self.source.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u8bd5ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u8bd5ID", None))
        self.SubjectID.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u8bd5ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"EMG\u4fe1\u53f7\u5b9e\u65f6\u663e\u793a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Set Scale", None))
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.SNR1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SNR2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SNR3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SNR4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SNR5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SNR6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SNR7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SNR8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"IMU-ACC\u4fe1\u53f7\u5b9e\u65f6\u663e\u793a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"IMU-GRO\u4fe1\u53f7\u5b9e\u65f6\u663e\u793a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SNR", None))
        self.SNR.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bfb\u53d6", None))
        self.Stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u8bfb\u53d6", None))
        self.TrainModel.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u6a21\u578b", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u52a8\u4f5c\u6b21\u6570", None))
        self.TrialNum.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u6b21\u6570", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"  /", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u52a8\u4f5c\u5e8f\u53f7", None))
        self.GestureNum.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u5e8f\u53f7", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"  /", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"  5", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u8ba1\u65f6\u5668", None))
        self.MissionTimer.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u8ba1\u65f6\u5668", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u91c7\u96c6", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u624b\u52bf\u63d0\u793a", None))
        self.CurrentFig.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u624b\u52bf\u63d0\u793a", None))
        self.NextFig.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"mode", None))
        self.comboBox_18.setItemText(0, QCoreApplication.translate("MainWindow", u"high-accuracy", None))
        self.comboBox_18.setItemText(1, QCoreApplication.translate("MainWindow", u"high-sensitivity", None))

        self.comboBox_18.setCurrentText(QCoreApplication.translate("MainWindow", u"high-accuracy", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\u53f7", None))
        self.comboBox_20.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_20.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_20.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_20.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_20.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_20.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))

        self.comboBox_20.setCurrentText(QCoreApplication.translate("MainWindow", u"1", None))
        self.GestureResultFig.setText("")
        self.StartTest.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6d4b\u8bd5", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None))
        self.speed.setText(QCoreApplication.translate("MainWindow", u"\u00d71", None))
        self.StopTest.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u6d4b\u8bd5", None))
    # retranslateUi

