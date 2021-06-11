# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Settings(object):
    def __init__(self):
        self.Stealing_Status = True
        self.Mode = 5  # Medium
        self.Player2_Status = False
        self.FirstPlayer_Status = True
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 560)
        MainWindow.setStyleSheet("background:#ffddc5")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.widget_5)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_4.addWidget(self.radioButton_3)
        self.radioButton_9 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setChecked(True)
        self.radioButton_9.setObjectName("radioButton_9")
        self.horizontalLayout_4.addWidget(self.radioButton_9)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_4.addWidget(self.radioButton_4)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_5)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_3.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_3.addWidget(self.radioButton_6)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget_5)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.radioButton = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_5)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.radioButton_7 = QtWidgets.QRadioButton(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setChecked(True)
        self.radioButton_7.setObjectName("radioButton_7")
        self.horizontalLayout.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.horizontalLayout.addWidget(self.radioButton_8)
        self.verticalLayout.addWidget(self.widget_4)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setContentsMargins(300, -1, 300, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "border: 2px solid; border-radius:12px; border-color: blue;background-color: palette(base);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.widget_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton.clicked.connect(lambda: self.Save(MainWindow))
    def Save(self,MainWindow):
        # Check stealing  (In case of stealing : Stealing_Status=True )
        Stealing=self.radioButton.isChecked()
        if Stealing == True:
            Stealing_Status=True
        else:
            Stealing_Status = False

        # Check The Mode (In case of Easy: Mode=2 , Medium: Mode=5 , Hard: Mode=10)
        Depth=5
        if self.radioButton_3.isChecked():
            Depth=2
        elif self.radioButton_9.isChecked():
            Depth=5
        elif self.radioButton_4.isChecked():
            Depth=10

        # Check Player 2 type In case of AI: Player2_Status=False)
        Player2_IsAI=self.radioButton_6.isChecked()
        if Player2_IsAI == True:
            Player2_Status=False
        else:
            Player2_Status = True

        # Check First Player In case Player 1 is the first player FirstPlayer_Status=True
        Player1_First=self.radioButton_7.isChecked()
        if Player1_First == True:
            FirstPlayer_Status=True
        else:
            FirstPlayer_Status = False
        self.Stealing_Status=Stealing_Status
        self.Mode=Depth
        self.Player2_Status=Player2_Status
        self.FirstPlayer_Status=FirstPlayer_Status
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "                   MANCALA GAME SETTINGS"))
        self.label_4.setText(_translate("MainWindow", "    Mode"))
        self.radioButton_3.setText(_translate("MainWindow", "Easy"))
        self.radioButton_9.setText(_translate("MainWindow", "Medium"))
        self.radioButton_4.setText(_translate("MainWindow", "Hard"))
        self.label_5.setText(_translate("MainWindow", "    Player 2"))
        self.radioButton_5.setText(_translate("MainWindow", "Human"))
        self.radioButton_6.setText(_translate("MainWindow", "AI Algorithm"))
        self.label_6.setText(_translate("MainWindow", "    Movement"))
        self.radioButton.setText(_translate("MainWindow", "With Stealing"))
        self.radioButton_2.setText(_translate("MainWindow", "wihout Stealing"))
        self.label_7.setText(_translate("MainWindow", "    First Player"))
        self.radioButton_7.setText(_translate("MainWindow", "PLayer 1"))
        self.radioButton_8.setText(_translate("MainWindow", "Player 2"))
        self.pushButton.setText(_translate("MainWindow", "Save"))

