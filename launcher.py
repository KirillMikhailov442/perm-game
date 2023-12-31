# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from game import start_game


class Ui_MainWindow(object):


    def run_game(self):
        start_game()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(420, 445)
        MainWindow.setMaximumSize(QtCore.QSize(420, 445))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/textures/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.preview = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy)
        self.preview.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.preview.setFont(font)
        self.preview.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.preview.setStyleSheet("color: rgb(85, 170, 0);")
        self.preview.setText("")
        self.preview.setPixmap(QtGui.QPixmap("assets/textures/preview.jpg"))
        self.preview.setScaledContents(True)
        self.preview.setAlignment(QtCore.Qt.AlignCenter)
        self.preview.setWordWrap(False)
        self.preview.setObjectName("preview")
        self.verticalLayout_5.addWidget(self.preview)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(400, 200))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_main)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_start = QtWidgets.QPushButton(self.tab_main)
        self.button_start.setObjectName("button_start")
        self.verticalLayout_3.addWidget(self.button_start)
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_info = QtWidgets.QWidget()
        self.tab_info.setObjectName("tab_info")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_info)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_info = QtWidgets.QLabel(self.tab_info)
        self.label_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_info.setWordWrap(True)
        self.label_info.setObjectName("label_info")
        self.verticalLayout_4.addWidget(self.label_info)
        self.tabWidget.addTab(self.tab_info, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_start.clicked.connect(self.run_game)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Битва с племенем"))
        self.button_start.setText(_translate("MainWindow", "Начать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("MainWindow", "Главная"))
        self.label_info.setText(_translate("MainWindow", "Вы играете за Ермака Тимофеевича. Вы и ваш отряд отправился колонизировать остальные земли Перми, но вы попали в окружение диких уральских племен. После яростной битвы с племенем вы оказались совершенно одни в окружении. Ваша цель продержаться 3 минуты и победить вождя племени после чего вы сможете вернуться к своему отряду."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), _translate("MainWindow", "Описание"))
