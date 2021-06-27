


from PyQt5 import QtCore, QtGui, QtWidgets

class safhe_vorod(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(596, 591)
        dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo_2021-06-26_13-41-56.jpg"))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 131, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"font: 14pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 170, 131, 41))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"font: 14pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 270, 171, 111))
        self.pushButton_4.setStyleSheet("border-radius:65px 45px 200px 0px;\n"
"border:2px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"mv boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 270, 171, 111))
        self.pushButton_5.setStyleSheet("border-radius:65px 45px 200px 0px;\n"
"border:2px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"mv boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 270, 171, 111))
        self.pushButton_6.setStyleSheet("border-radius:65px 45px 200px 0px;\n"
"border:2px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"mv boli\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 430, 181, 111))
        self.pushButton_7.setStyleSheet("border-radius:65px 45px 200px 0px;\n"
"border:2px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"mv boli\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 430, 171, 111))
        self.pushButton_8.setStyleSheet("border-radius:65px 45px 200px 0px;\n"
"border:2px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"mv boli\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(410, 430, 171, 111))
        self.pushButton_9.setStyleSheet("border-radius:65px 45px 200px 0px;\n"
"border:2px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"mv boli\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 70, 411, 101))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.clicked.connect(self.switchs)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 131, 41))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"font: 14pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton.setObjectName("pushButton")
        self.dialog = dialog
        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.pushButton_2.setText(_translate("dialog", "dste bandy"))
        self.pushButton_3.setText(_translate("dialog", "about us"))
        self.pushButton_4.setText(_translate("dialog", "w1"))
        self.pushButton_5.setText(_translate("dialog", "w2"))
        self.pushButton_6.setText(_translate("dialog", "w3"))
        self.pushButton_7.setText(_translate("dialog", "w4"))
        self.pushButton_8.setText(_translate("dialog", "w5"))
        self.pushButton_9.setText(_translate("dialog", "w6"))
        self.label_2.setText(_translate("dialog", "*welcome to our program*"))
        self.pushButton.setText(_translate("dialog", "sigh in"))


    def switchs(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        self.dialog.close()



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 592)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo_2021-06-26_13-41-56.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 181, 71))
        self.label_2.setStyleSheet("font: 28pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchmoshtary)
        self.pushButton.setGeometry(QtCore.QRect(160, 150, 241, 81))
        self.pushButton.setStyleSheet("border-radius: 45px 30px 100px 0px;\n"
"font: 18pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchforoshande)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 280, 241, 81))
        self.pushButton_2.setStyleSheet("border-radius: 45px 30px 100px 0px;\n"
"font: 18pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.switchoperature)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 400, 241, 81))
        self.pushButton_3.setStyleSheet("border-radius: 45px 30px 100px 0px;\n"
"font: 18pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.retranslateUi(Dialog)
        self.dialog = Dialog
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**sigh in**"))
        self.pushButton.setText(_translate("Dialog", "moshtary"))
        self.pushButton_2.setText(_translate("Dialog", "foroshande"))
        self.pushButton_3.setText(_translate("Dialog", "operature"))

    def switchoperature(self):
        self.wwim = QtWidgets.QDialog()
        self.ui = Uoperature()
        self.ui.setupUi(self.wwim)
        self.wwim.show()
        self.dialog.close()



    def switchmoshtary(self):
      self.winn = QtWidgets.QDialog()
      self.ui = Umoshtary()
      self.ui.setupUi(self.winn)
      self.winn.show()
      self.dialog.close()

    def switchforoshande(self):
        self.won = QtWidgets.QDialog()
        self.ui = Uforoshande()
        self.ui.setupUi(self.won)
        self.won.show()
        self.dialog.close()


class Umoshtary(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo_2021-06-26_13-41-56.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 191, 61))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 81, 51))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 230, 121, 41))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 320, 81, 41))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 400, 141, 41))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 480, 121, 41))
        self.label_7.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 150, 151, 31))
        self.lineEdit.setStyleSheet("border-radius:15px 10px 50px 0px;\n"
"font: 14pt \"MV Boli\";\n"
"border:1px solid yellow;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 240, 151, 31))
        self.lineEdit_2.setStyleSheet("border-radius:15px 10px 50px 0px;\n"
"font: 14pt \"MV Boli\";\n"
"border:1px solid yellow;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 410, 151, 31))
        self.lineEdit_3.setStyleSheet("border-radius:15px 10px 50px 0px;\n"
"font: 14pt \"MV Boli\";\n"
"border:1px solid yellow;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(210, 490, 151, 31))
        self.dateEdit.setStyleSheet("border-radius:15px 10px 50px 0px;\n"
"font: 12pt \"MV Boli\";\n"
"border:1px solid yellow;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);")
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(210, 330, 151, 31))
        self.comboBox.setStyleSheet("border-radius:15px 10px 50px 0px;\n"
"font: 14pt \"MV Boli\";\n"
"border:1px solid yellow;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchaccount)
        self.pushButton.setGeometry(QtCore.QRect(440, 280, 131, 61))
        self.pushButton.setStyleSheet("border-radius:25px 20px 50px 0px;\n"
"border:1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**moshtary**"))
        self.label_3.setText(_translate("Dialog", "name:"))
        self.label_4.setText(_translate("Dialog", "last name:"))
        self.label_5.setText(_translate("Dialog", "gender:"))
        self.label_6.setText(_translate("Dialog", "national code:"))
        self.label_7.setText(_translate("Dialog", "birth date:"))
        self.comboBox.setItemText(0, _translate("Dialog", "woman"))
        self.comboBox.setItemText(1, _translate("Dialog", "man"))
        self.pushButton.setText(_translate("Dialog", "next"))

    def switchaccount(self):
        self.wen = QtWidgets.QDialog()
        self.ui = Uiaccount()
        self.ui.setupUi(self.wen)
        self.wen.show()
        self.dialog.close()


class Uiaccount(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 573)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 611, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo_2021-06-26_13-41-56.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 281, 61))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 111, 41))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 111, 31))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 290, 61, 41))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 360, 151, 51))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 450, 91, 41))
        self.label_7.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 130, 171, 41))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0p;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"font: 14pt \"mv boli\";\n"
"border:1px solid yellow")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 210, 171, 41))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"font: 14pt \"mv boli\";\n"
"border:1px solid yellow")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 290, 171, 41))
        self.lineEdit_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"font: 14pt \"mv boli\";\n"
"border:1px solid yellow")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 370, 171, 41))
        self.lineEdit_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"font: 14pt \"mv boli\";\n"
"border:1px solid yellow")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 450, 281, 111))
        self.lineEdit_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"font: 14pt \"mv boli\";\n"
"border:1px solid yellow")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 260, 121, 81))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"mv boli\";\n"
"border:1px solid yellow")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**create account**"))
        self.label_3.setText(_translate("Dialog", "username:"))
        self.label_4.setText(_translate("Dialog", "password:"))
        self.label_5.setText(_translate("Dialog", "email:"))
        self.label_6.setText(_translate("Dialog", "phone number:"))
        self.label_7.setText(_translate("Dialog", "address:"))
        self.pushButton.setText(_translate("Dialog", "sigh in"))



class Uforoshande(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 590)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo_2021-06-26_13-41-56.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 221, 81))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 71, 41))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 111, 41))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 340, 81, 31))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 410, 141, 51))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 490, 111, 51))
        self.label_7.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 260, 181, 41))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color:rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(220, 340, 181, 41))
        self.comboBox.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color:rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 420, 181, 41))
        self.lineEdit_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color:rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(230, 500, 171, 41))
        self.dateEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color:rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 170, 181, 41))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color:rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchfaccount)
        self.pushButton.setGeometry(QtCore.QRect(460, 310, 121, 61))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**foroshande**"))
        self.label_3.setText(_translate("Dialog", "name:"))
        self.label_4.setText(_translate("Dialog", "last name:"))
        self.label_5.setText(_translate("Dialog", "gender:"))
        self.label_6.setText(_translate("Dialog", "national code:"))
        self.label_7.setText(_translate("Dialog", "birthdate:"))
        self.comboBox.setItemText(0, _translate("Dialog", "woman"))
        self.comboBox.setItemText(1, _translate("Dialog", "man"))
        self.pushButton.setText(_translate("Dialog", "next"))

    def switchfaccount(self):
        self.win = QtWidgets.QDialog()
        self.ui = faccount()
        self.ui.setupUi(self.win)
        self.win.show()
        self.dialog.close()
class faccount(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 589)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 621, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo_2021-06-26_13-41-56.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 281, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 111, 41))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 180, 101, 51))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 320, 161, 51))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 250, 71, 41))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 460, 111, 41))
        self.label_7.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(50, 390, 131, 41))
        self.label_8.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 110, 171, 41))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 190, 171, 41))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 260, 171, 41))
        self.lineEdit_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 330, 171, 41))
        self.lineEdit_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 470, 161, 91))
        self.lineEdit_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(220, 400, 171, 41))
        self.comboBox.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color: rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 270, 121, 71))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**create account**"))
        self.label_3.setText(_translate("Dialog", "username:"))
        self.label_4.setText(_translate("Dialog", "password:"))
        self.label_5.setText(_translate("Dialog", "phone number:"))
        self.label_6.setText(_translate("Dialog", "email:"))
        self.label_7.setText(_translate("Dialog", "address:"))
        self.label_8.setText(_translate("Dialog", "store type:"))
        self.comboBox.setItemText(0, _translate("Dialog", "n1"))
        self.comboBox.setItemText(1, _translate("Dialog", "n2"))
        self.comboBox.setItemText(2, _translate("Dialog", "n3"))
        self.comboBox.setItemText(3, _translate("Dialog", "n4"))
        self.comboBox.setItemText(4, _translate("Dialog", "n5"))
        self.comboBox.setItemText(5, _translate("Dialog", "n6"))
        self.comboBox.setItemText(6, _translate("Dialog", "n7"))
        self.comboBox.setItemText(7, _translate("Dialog", "n8"))
        self.pushButton.setText(_translate("Dialog", "sigh in"))




class Uoperature(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(598, 588)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo_2021-06-26_13-41-56.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 201, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 71, 41))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 220, 111, 41))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 300, 91, 51))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 390, 141, 61))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 490, 111, 51))
        self.label_7.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchoaccount)
        self.pushButton.setGeometry(QtCore.QRect(440, 270, 121, 61))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 130, 171, 41))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 220, 171, 41))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 400, 171, 41))
        self.lineEdit_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(220, 500, 161, 41))
        self.dateEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(210, 310, 171, 41))
        self.comboBox.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**operature**"))
        self.label_3.setText(_translate("Dialog", "name:"))
        self.label_4.setText(_translate("Dialog", "last name:"))
        self.label_5.setText(_translate("Dialog", "gender:"))
        self.label_6.setText(_translate("Dialog", "national code:"))
        self.label_7.setText(_translate("Dialog", "birthdate:"))
        self.pushButton.setText(_translate("Dialog", "next"))
        self.comboBox.setItemText(0, _translate("Dialog", "woman"))
        self.comboBox.setItemText(1, _translate("Dialog", "man"))

    def switchoaccount(self):
        self.wan = QtWidgets.QDialog()
        self.ui = oaccount()
        self.ui.setupUi(self.wan)
        self.wan.show()
        self.dialog.close()


class oaccount(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 0, 621, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo_2021-06-26_13-41-56.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 281, 81))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 111, 51))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 220, 101, 41))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 380, 161, 41))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 300, 71, 41))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(70, 470, 81, 31))
        self.label_7.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 150, 171, 41))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"font: 16pt \"MV Boli\";\n"
"border:1px solid yellow;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 230, 171, 41))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"font: 16pt \"MV Boli\";\n"
"border:1px solid yellow;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 310, 171, 41))
        self.lineEdit_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"font: 16pt \"MV Boli\";\n"
"border:1px solid yellow;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 380, 171, 41))
        self.lineEdit_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"font: 16pt \"MV Boli\";\n"
"border:1px solid yellow;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 460, 171, 101))
        self.lineEdit_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"font: 16pt \"MV Boli\";\n"
"border:1px solid yellow;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 260, 131, 81))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"font: 16pt \"MV Boli\";\n"
"border:1px solid yellow;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**create account**"))
        self.label_3.setText(_translate("Dialog", "username:"))
        self.label_4.setText(_translate("Dialog", "password:"))
        self.label_5.setText(_translate("Dialog", "phone number:"))
        self.label_6.setText(_translate("Dialog", "email:"))
        self.label_7.setText(_translate("Dialog", "address:"))
        self.pushButton.setText(_translate("Dialog", "sigh in"))








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogf = QtWidgets.QDialog()
    ui = safhe_vorod()
    ui.setupUi(dialogf)
    dialogf.show()
    sys.exit(app.exec_())
