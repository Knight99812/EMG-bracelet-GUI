# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrainModel3_wifiCD_ui.ui'
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
        MainWindow.resize(1099, 862)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(201, 31))
        font = QFont()
        font.setFamily(u"Adobe Heiti Std")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.WindowLen = QComboBox(self.centralwidget)
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

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font1)
        self.comboBox_2.setEditable(True)

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.horizontalSpacer_3 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.source = QLineEdit(self.centralwidget)
        self.source.setObjectName(u"source")
        font2 = QFont()
        font2.setFamily(u"Adobe Heiti Std")
        font2.setPointSize(10)
        self.source.setFont(font2)
        self.source.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.source)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.SubjectID = QLineEdit(self.centralwidget)
        self.SubjectID.setObjectName(u"SubjectID")
        self.SubjectID.setMinimumSize(QSize(0, 31))
        self.SubjectID.setMaximumSize(QSize(16777215, 31))
        self.SubjectID.setFont(font2)
        self.SubjectID.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.SubjectID)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 2)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(161, 71))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(111, 31))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.plus = QPushButton(self.centralwidget)
        self.plus.setObjectName(u"plus")
        self.plus.setMinimumSize(QSize(41, 31))
        font3 = QFont()
        font3.setPointSize(23)
        self.plus.setFont(font3)

        self.horizontalLayout_7.addWidget(self.plus)

        self.minus = QPushButton(self.centralwidget)
        self.minus.setObjectName(u"minus")
        self.minus.setMinimumSize(QSize(41, 31))
        self.minus.setFont(font3)

        self.horizontalLayout_7.addWidget(self.minus)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.EMG1 = PlotWidget(self.centralwidget)
        self.EMG1.setObjectName(u"EMG1")
        self.EMG1.setMinimumSize(QSize(211, 111))

        self.verticalLayout.addWidget(self.EMG1)

        self.SNR1 = QLineEdit(self.centralwidget)
        self.SNR1.setObjectName(u"SNR1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SNR1.sizePolicy().hasHeightForWidth())
        self.SNR1.setSizePolicy(sizePolicy)
        self.SNR1.setFont(font2)
        self.SNR1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.SNR1)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.EMG2 = PlotWidget(self.centralwidget)
        self.EMG2.setObjectName(u"EMG2")
        self.EMG2.setMinimumSize(QSize(211, 111))

        self.verticalLayout_2.addWidget(self.EMG2)

        self.SNR2 = QLineEdit(self.centralwidget)
        self.SNR2.setObjectName(u"SNR2")
        self.SNR2.setFont(font2)
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
        self.EMG3 = PlotWidget(self.centralwidget)
        self.EMG3.setObjectName(u"EMG3")
        self.EMG3.setMinimumSize(QSize(211, 111))

        self.verticalLayout_3.addWidget(self.EMG3)

        self.SNR3 = QLineEdit(self.centralwidget)
        self.SNR3.setObjectName(u"SNR3")
        self.SNR3.setMinimumSize(QSize(111, 31))
        self.SNR3.setFont(font2)
        self.SNR3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.SNR3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.EMG4 = PlotWidget(self.centralwidget)
        self.EMG4.setObjectName(u"EMG4")
        self.EMG4.setMinimumSize(QSize(211, 111))

        self.verticalLayout_4.addWidget(self.EMG4)

        self.SNR4 = QLineEdit(self.centralwidget)
        self.SNR4.setObjectName(u"SNR4")
        self.SNR4.setMinimumSize(QSize(111, 31))
        self.SNR4.setFont(font2)
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
        self.EMG5 = PlotWidget(self.centralwidget)
        self.EMG5.setObjectName(u"EMG5")
        self.EMG5.setMinimumSize(QSize(211, 111))

        self.verticalLayout_5.addWidget(self.EMG5)

        self.SNR5 = QLineEdit(self.centralwidget)
        self.SNR5.setObjectName(u"SNR5")
        self.SNR5.setMinimumSize(QSize(111, 31))
        self.SNR5.setFont(font2)
        self.SNR5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.SNR5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.EMG6 = PlotWidget(self.centralwidget)
        self.EMG6.setObjectName(u"EMG6")
        self.EMG6.setMinimumSize(QSize(211, 111))

        self.verticalLayout_6.addWidget(self.EMG6)

        self.SNR6 = QLineEdit(self.centralwidget)
        self.SNR6.setObjectName(u"SNR6")
        self.SNR6.setMinimumSize(QSize(111, 31))
        self.SNR6.setFont(font2)
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
        self.EMG7 = PlotWidget(self.centralwidget)
        self.EMG7.setObjectName(u"EMG7")
        self.EMG7.setMinimumSize(QSize(211, 111))

        self.verticalLayout_7.addWidget(self.EMG7)

        self.SNR7 = QLineEdit(self.centralwidget)
        self.SNR7.setObjectName(u"SNR7")
        self.SNR7.setMinimumSize(QSize(111, 31))
        self.SNR7.setFont(font2)
        self.SNR7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.SNR7)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.EMG8 = PlotWidget(self.centralwidget)
        self.EMG8.setObjectName(u"EMG8")
        self.EMG8.setMinimumSize(QSize(211, 111))

        self.verticalLayout_8.addWidget(self.EMG8)

        self.SNR8 = QLineEdit(self.centralwidget)
        self.SNR8.setObjectName(u"SNR8")
        self.SNR8.setMinimumSize(QSize(111, 31))
        self.SNR8.setFont(font2)
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
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(241, 71))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.ACC = PlotWidget(self.centralwidget)
        self.ACC.setObjectName(u"ACC")
        self.ACC.setMinimumSize(QSize(431, 261))

        self.verticalLayout_10.addWidget(self.ACC)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(241, 71))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.horizontalSpacer_13 = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.GRO = PlotWidget(self.centralwidget)
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
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(91, 41))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.SNR = QLineEdit(self.centralwidget)
        self.SNR.setObjectName(u"SNR")
        self.SNR.setMinimumSize(QSize(148, 31))
        self.SNR.setFont(font2)
        self.SNR.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.SNR)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_15 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setMinimumSize(QSize(151, 41))
        self.Start.setStyleSheet(u"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";\n"
"background-color: rgb(21, 85, 154);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.Start)

        self.Stop = QPushButton(self.centralwidget)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setMinimumSize(QSize(151, 41))
        self.Stop.setStyleSheet(u"background-color: rgb(242, 90, 71);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Adobe \u9ed1\u4f53 Std R\";")

        self.horizontalLayout_11.addWidget(self.Stop)

        self.TrainModel = QPushButton(self.centralwidget)
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

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1099, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.WindowLen.setCurrentIndex(1)


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
    # retranslateUi

