# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from board import Mancala_Board
from AlphaBeta import Alpha_Beta_Algorithm
from time import sleep

class game(object):
    def __init__(self):
        self.x=0
        self.board=Mancala_Board(None)
        self.Game_Over_Flag=0
        self.window2 = QtWidgets.QMainWindow()
        self.Stealing_Status=None
        self.Mode=5  # Medium
        self.FirstPlayer_Status=None
        self.Player2_Status =None

    def update_settings(self, Stealing_Status, Mode, Player2_Status, FirstPlayer_Status):
        self.Stealing_Status = Stealing_Status
        self.Mode = Mode
        self.Player2_Status = Player2_Status
        self.FirstPlayer_Status = FirstPlayer_Status

    def Game_Play(self,MainWindow):
        QtWidgets.qApp.processEvents()
        sleep(1)
        if self.board.IsGameOver():
            self.label_4.setText("            GAME OVER")
            self.label_5.setText("            ")
            self.Game_Over_Flag=1
            self.Update_Mancala()
            MainWindow.repaint()

        if self.Player2_Status==False and self.FirstPlayer_Status==0:
            if self.x == 0 and self.board.IsGameOver() == 0:
                while (True):
                    self.label_5.setText("             AI TURN")
                    self.label_4.setText("            ")
                    QtWidgets.qApp.processEvents()
                    _, k = Alpha_Beta_Algorithm(self.board, self.Mode, -100000, 100000, True, self.Stealing_Status)

                    Ai_Turn = self.board.Stones_Move(k, self.Stealing_Status)

                    self.Update_Mancala()
                    MainWindow.repaint()
                    sleep(1)

                    if self.board.IsGameOver():
                        self.label_4.setText("            GAME OVER")
                        self.label_5.setText("            ")
                        self.Update_Mancala()
                        MainWindow.repaint()
                        break
                    if not Ai_Turn:
                        break
                self.FirstPlayer_Status=1
        elif self.Player2_Status==True and self.FirstPlayer_Status==0:
            self.label_5.setText("             Player 2 Turn Please click on the bucket")
            self.label_4.setText("            ")




        if self.Game_Over_Flag==0 and self.FirstPlayer_Status==1:
            self.label_4.setText( "             Player 1 Turn Please click on the bucket")
            self.label_5.setText("            ")





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 591)
        MainWindow.setStyleSheet("background:#ffddc5")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:bkue;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setMinimumSize(QtCore.QSize(100, 300))
        self.lineEdit_1.setStyleSheet("border: 2px solid; border-radius:12px; border-color: blue;background-color: palette(base);\n"
"color:#1b4972;\n"
"")
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setReadOnly(True)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout_2.addWidget(self.lineEdit_1)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(-1, 100, -1, 100)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(400, 0))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border: 2px solid; border-radius:12px; border-color: blue;background-color: palette(base);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border: 2px solid; border-radius:12px; border-color: blue;background-color: palette(base);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border: 2px solid; border-radius:12px; border-color: blue;background-color: palette(base);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border: 2px solid; border-radius:12px; border-color: blue;background-color: palette(base);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border: 2px solid; border-radius:12px; border-color: blue;background-color: palette(base);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 2px solid; border-radius:12px; border-color: blue;background-color: palette(base);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMinimumSize(QtCore.QSize(400, 0))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_7.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border: 2px solid; border-radius:12px; border-color: red;background-color: palette(base);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_8.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("border: 2px solid; border-radius:12px; border-color: red;background-color: palette(base);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_9.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("border: 2px solid; border-radius:12px; border-color: red;background-color: palette(base);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_10.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("border: 2px solid; border-radius:12px; border-color: red;background-color: palette(base);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_4.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_11.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("border: 2px solid; border-radius:12px; border-color: red;background-color: palette(base);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_4.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_12.setMinimumSize(QtCore.QSize(50, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("border: 2px solid; border-radius:12px; border-color: red;background-color: palette(base);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_4.addWidget(self.pushButton_12)
        self.verticalLayout.addWidget(self.widget_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_5 = QtWidgets.QWidget(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 200))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 300))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 300))
        self.lineEdit_2.setStyleSheet("border: 2px solid; border-radius:12px; border-color:red;background-color: palette(base);\n"
"color:#1b4972;\n"
"")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.widget_5)
        self.verticalLayout_4.addWidget(self.widget_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(lambda: self.Make_Move1(MainWindow))
        self.pushButton_2.clicked.connect(lambda: self.Make_Move2(MainWindow))
        self.pushButton_3.clicked.connect(lambda: self.Make_Move3(MainWindow))
        self.pushButton_4.clicked.connect(lambda: self.Make_Move4(MainWindow))
        self.pushButton_5.clicked.connect(lambda: self.Make_Move5(MainWindow))
        self.pushButton_6.clicked.connect(lambda: self.Make_Move6(MainWindow))
        self.pushButton_7.clicked.connect(lambda: self.Make_Move7(MainWindow))
        self.pushButton_8.clicked.connect(lambda: self.Make_Move8(MainWindow))
        self.pushButton_9.clicked.connect(lambda: self.Make_Move9(MainWindow))
        self.pushButton_10.clicked.connect(lambda: self.Make_Move10(MainWindow))
        self.pushButton_11.clicked.connect(lambda: self.Make_Move11(MainWindow))
        self.pushButton_12.clicked.connect(lambda: self.Make_Move12(MainWindow))
        self.lineEdit_1.setFont(font)
        self.lineEdit_2.setFont(font)
        self.lineEdit_1.setText("0")
        self.lineEdit_2.setText("0")

    def Update_Mancala(self):

        self.pushButton.setText(str(self.board.Mancala_board[0]))
        self.pushButton_2.setText(str(self.board.Mancala_board[1]))
        self.pushButton_3.setText(str(self.board.Mancala_board[2]))
        self.pushButton_4.setText( str(self.board.Mancala_board[3]))
        self.pushButton_5.setText(str(self.board.Mancala_board[4]))
        self.pushButton_6.setText(str(self.board.Mancala_board[5]))
        self.pushButton_7.setText(str(self.board.Mancala_board[7]))
        self.pushButton_8.setText(str(self.board.Mancala_board[8]))
        self.pushButton_9.setText(str(self.board.Mancala_board[9]))
        self.pushButton_10.setText(str(self.board.Mancala_board[10]))
        self.pushButton_11.setText(str(self.board.Mancala_board[11]))
        self.pushButton_12.setText(str(self.board.Mancala_board[12]))
        self.lineEdit_1.setText(str(self.board.Mancala_board[6]))
        self.lineEdit_2.setText(str(self.board.Mancala_board[13]))
    def Make_Move1(self,MainWindow):
        self.board.Mancala_board[0] = int(self.pushButton.text())
        self.x = self.board.Stones_Move(0, self.Stealing_Status)
        self.Update_Mancala()
        self.flag=1
        MainWindow.repaint()
        if self.x==0:
            self.FirstPlayer_Status = 0
        self.Game_Play(MainWindow)


    def Make_Move2(self,MainWindow):
        self.board.Mancala_board[1]=int(self.pushButton_2.text())
        self.x=self.board.Stones_Move(1,self.Stealing_Status)
        self.Update_Mancala()
        MainWindow.repaint()
        if self.x == 0:
            self.FirstPlayer_Status = 0
        self.Game_Play(MainWindow)

    def Make_Move3(self,MainWindow):
        self.board.Mancala_board[2] = int(self.pushButton_3.text())
        self.x = self.board.Stones_Move(2, self.Stealing_Status)
        self.Update_Mancala()
        MainWindow.repaint()
        if self.x == 0:
            self.FirstPlayer_Status = 0
        self.Game_Play(MainWindow)

    def Make_Move4(self,MainWindow):
        self.board.Mancala_board[3] = int(self.pushButton_4.text())
        self.x = self.board.Stones_Move(3, self.Stealing_Status)
        self.Update_Mancala()
        MainWindow.repaint()
        if self.x == 0:
            self.FirstPlayer_Status = 0
        self.Game_Play(MainWindow)

    def Make_Move5(self,MainWindow):
        self.board.Mancala_board[4] = int(self.pushButton_5.text())
        self.x = self.board.Stones_Move(4, self.Stealing_Status)
        self.Update_Mancala()
        MainWindow.repaint()
        if self.x == 0:
            self.FirstPlayer_Status = 0
        self.Game_Play(MainWindow)

    def Make_Move6(self,MainWindow):
        self.board.Mancala_board[5] = int(self.pushButton_6.text())
        self.x = self.board.Stones_Move(5, self.Stealing_Status)
        self.Update_Mancala()
        MainWindow.repaint()
        if self.x == 0:
            self.FirstPlayer_Status = 0
        self.Game_Play(MainWindow)

    def Make_Move7(self,MainWindow):
        if self.Player2_Status==True:
            self.board.Mancala_board[7] = int(self.pushButton_7.text())
            self.x = self.board.Stones_Move(7, self.Stealing_Status)
            self.Update_Mancala()
            MainWindow.repaint()
            if self.x == 0:
                self.FirstPlayer_Status = 1
            self.Game_Play(MainWindow)


    def Make_Move8(self,MainWindow):
        if self.Player2_Status==True:
            self.board.Mancala_board[8] = int(self.pushButton_8.text())
            self.x = self.board.Stones_Move(8, self.Stealing_Status)
            self.Update_Mancala()
            MainWindow.repaint()
            if self.x == 0:
                self.FirstPlayer_Status = 1
            self.Game_Play(MainWindow)

    def Make_Move9(self,MainWindow):
        if self.Player2_Status==True:
            self.board.Mancala_board[9] = int(self.pushButton_9.text())
            self.x = self.board.Stones_Move(9, self.Stealing_Status)
            self.Update_Mancala()
            MainWindow.repaint()
            if self.x == 0:
                self.FirstPlayer_Status = 1
            self.Game_Play(MainWindow)
    def Make_Move10(self,MainWindow):
        if self.Player2_Status==True:
            self.board.Mancala_board[10] = int(self.pushButton_10.text())
            self.x = self.board.Stones_Move(10, self.Stealing_Status)
            self.Update_Mancala()
            if self.x == 0:
                self.FirstPlayer_Status = 1
            MainWindow.repaint()
            self.Game_Play(MainWindow)
    def Make_Move11(self,MainWindow):
        if self.Player2_Status==True:
            self.board.Mancala_board[11] = int(self.pushButton_11.text())
            self.x = self.board.Stones_Move(11, self.Stealing_Status)
            self.Update_Mancala()
            MainWindow.repaint()
            if self.x == 0:
                self.FirstPlayer_Status = 1
            self.Game_Play(MainWindow)
    def Make_Move12(self,MainWindow):
       if self.Player2_Status==True:
           self.board.Mancala_board[12] = int(self.pushButton_12.text())
           self.x = self.board.Stones_Move(12, self.Stealing_Status)
           self.Update_Mancala()
           MainWindow.repaint()
           if self.x == 0:
               self.FirstPlayer_Status = 1
           self.Game_Play(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "                    MANCALA GAME"))
        self.label.setText(_translate("MainWindow", "Player 1"))
        self.label_4.setText(_translate("MainWindow", "            "))
        self.pushButton_6.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_3.setText(_translate("MainWindow", "4"))
        self.pushButton_2.setText(_translate("MainWindow", "4"))
        self.pushButton.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "4"))
        self.pushButton_8.setText(_translate("MainWindow", "4"))
        self.pushButton_9.setText(_translate("MainWindow", "4"))
        self.pushButton_10.setText(_translate("MainWindow", "4"))
        self.pushButton_11.setText(_translate("MainWindow", "4"))
        self.pushButton_12.setText(_translate("MainWindow", "4"))
        #self.label_5.setText(_translate("MainWindow", "             Player 2 Turn Please click on the bucket"))
        self.label_2.setText(_translate("MainWindow", "Player 2"))




