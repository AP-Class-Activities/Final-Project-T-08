

from PyQt5 import QtCore, QtGui, QtWidgets

#safhe vorod barname
class safhe_vorod(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(596, 591)
        dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.clicked.connect(self.switchgrouping)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 131, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"font: 14pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(dialog)
        self.pushButton_3.clicked.connect(self.switchabout_us)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 170, 131, 41))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"font: 14pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 320, 171, 111))
        self.pushButton_4.setStyleSheet("border-radius:65px 45px 200px 0px;\n"
"border:2px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"mv boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 320, 171, 111))
        self.pushButton_5.setStyleSheet("border-radius:65px 45px 200px 0px;\n"
"border:2px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"mv boli\";")
        self.pushButton_5.setObjectName("pushButton_5")

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
        self.pushButton_2.setText(_translate("dialog", "grouping"))
        self.pushButton_3.setText(_translate("dialog", "about us"))
        self.pushButton_4.setText(_translate("dialog", "w1"))
        self.pushButton_5.setText(_translate("dialog", "w2"))
        self.label_2.setText(_translate("dialog", "*welcome to our program*"))
        self.pushButton.setText(_translate("dialog", "sigh in"))


    def switchs(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        self.dialog.close()

    def switchabout_us(self):
        self.abou = QtWidgets.QDialog()
        self.ui = Uabout_us()
        self.ui.setupUi(self.abou)
        self.abou.show()
        self.dialog.close()

    def switchgrouping(self):
        self.group = QtWidgets.QDialog()
        self.ui = grouping()
        self.ui.setupUi(self.group)
        self.group.show()
        self.dialog.close()

#safhe aval sigh in baraye vorod
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 592)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 181, 71))
        self.label_2.setStyleSheet("font: 28pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchinupm)
        self.pushButton.setGeometry(QtCore.QRect(160, 150, 241, 81))
        self.pushButton.setStyleSheet("border-radius: 45px 30px 100px 0px;\n"
"font: 18pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchinupf)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 280, 241, 81))
        self.pushButton_2.setStyleSheet("border-radius: 45px 30px 100px 0px;\n"
"font: 18pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.switchinupo)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 400, 241, 81))
        self.pushButton_3.setStyleSheet("border-radius: 45px 30px 100px 0px;\n"
"font: 18pt \"mv boli\";\n"
"bonder: 1px solid yellow;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.clicked.connect(self.switchsafhevorod)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton_4")

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
        self.pushButton_4.setText(_translate("Dialog", "back"))


    def switchsafhevorod(self):
        self.eeu = QtWidgets.QDialog()
        self.ui = safhe_vorod()
        self.ui.setupUi(self.eeu)
        self.eeu.show()
        self.dialog.close()

    def switchinupm(self):
        self.inpp = QtWidgets.QDialog()
        self.ui = inup_m()
        self.ui.setupUi(self.inpp)
        self.inpp.show()
        self.dialog.close()

    def switchinupf(self):
        self.inpp = QtWidgets.QDialog()
        self.ui = inup_f()
        self.ui.setupUi(self.inpp)
        self.inpp.show()
        self.dialog.close()

    def switchinupo(self):
        self.inpp = QtWidgets.QDialog()
        self.ui = inup_o()
        self.ui.setupUi(self.inpp)
        self.inpp.show()
        self.dialog.close()

#safhe vorod moshtary
class inup_m(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 585)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -40, 641, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchmoshtary)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 241, 101))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchsighupm)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 310, 241, 101))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.switchuilog)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 520, 121, 41))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "sigh  in"))
        self.pushButton_2.setText(_translate("Dialog", "log in"))
        self.pushButton_3.setText(_translate("Dialog", "back"))


    def switchuilog(self):
        self.inpp = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.inpp)
        self.inpp.show()
        self.dialog.close()

    def switchmoshtary(self):
       self.winn = QtWidgets.QDialog()
       self.ui = Umoshtary()
       self.ui.setupUi(self.winn)
       self.winn.show()
       self.dialog.close()

    def switchsighupm(self):
        self.upm = QtWidgets.QDialog()
        self.ui = login_m()
        self.ui.setupUi(self.upm)
        self.upm.show()
        self.dialog.close()

#safhe vorod moshtary be hesab mojod az ghabl
class login_m(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 593)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 631, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 161, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(260, 190, 171, 51))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 270, 171, 51))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 190, 121, 31))
        self.label_3.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 270, 121, 41))
        self.label_4.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchsml)
        self.pushButton.setGeometry(QtCore.QRect(120, 360, 291, 51))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchupm)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 450, 261, 91))
        self.label_5.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**log in**"))
        self.label_3.setText(_translate("Dialog", "username:"))
        self.label_4.setText(_translate("Dialog", "password:"))
        self.pushButton.setText(_translate("Dialog", "log in"))
        self.pushButton_2.setText(_translate("dialog", "back"))

    def switchsml(self):
        self.upm = QtWidgets.QDialog()
        self.ui = safhe_m()
        self.ui.setupUi(self.upm)
        self.upm.show()
        self.dialog.close()


    def switchupm(self):
        self.upm = QtWidgets.QDialog()
        self.ui = inup_m()
        self.ui.setupUi(self.upm)
        self.upm.show()
        self.dialog.close()



#safhe vorod foroshande
class inup_f(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 585)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -40, 641, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchforoshande)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 241, 101))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchlog_f)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 310, 241, 101))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.switchuulog)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 520, 121, 41))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "sigh  in"))
        self.pushButton_2.setText(_translate("Dialog", "log in"))
        self.pushButton_3.setText(_translate("Dialog", "back"))


    def switchuulog(self):
        self.inpp = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.inpp)
        self.inpp.show()
        self.dialog.close()

    def switchforoshande(self):
        self.won = QtWidgets.QDialog()
        self.ui = Uforoshande()
        self.ui.setupUi(self.won)
        self.won.show()
        self.dialog.close()

    def switchlog_f(self):
        self.won = QtWidgets.QDialog()
        self.ui = login_f()
        self.ui.setupUi(self.won)
        self.won.show()
        self.dialog.close()

#safhe vorod foroshande be hesab mojod az ghabl
class login_f(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 593)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 631, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 161, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(260, 190, 171, 51))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 270, 171, 51))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 190, 121, 31))
        self.label_3.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 270, 121, 41))
        self.label_4.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchsflo)
        self.pushButton.setGeometry(QtCore.QRect(120, 360, 291, 51))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchupf)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 450, 261, 91))
        self.label_5.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**log in**"))
        self.label_3.setText(_translate("Dialog", "username:"))
        self.label_4.setText(_translate("Dialog", "password:"))
        self.pushButton.setText(_translate("Dialog", "log in"))
        self.pushButton_2.setText(_translate("dialog", "back"))


    def switchupf(self):
        self.won = QtWidgets.QDialog()
        self.ui = inup_f()
        self.ui.setupUi(self.won)
        self.won.show()
        self.dialog.close()

    def switchsflo(self):
        self.won = QtWidgets.QDialog()
        self.ui = safhe_f()
        self.ui.setupUi(self.won)
        self.won.show()
        self.dialog.close()

#safhe vorod operature
class inup_o(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 585)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -40, 641, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchoperature)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 241, 101))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchlogo)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 310, 241, 101))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.switchullog)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 520, 121, 41))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "sigh  in"))
        self.pushButton_2.setText(_translate("Dialog", "log in"))
        self.pushButton_3.setText(_translate("Dialog", "back"))

    def switchullog(self):
        self.inpp = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.inpp)
        self.inpp.show()
        self.dialog.close()


    def switchoperature(self):
        self.wwim = QtWidgets.QDialog()
        self.ui = Uoperature()
        self.ui.setupUi(self.wwim)
        self.wwim.show()
        self.dialog.close()

    def switchlogo(self):
        self.wwim = QtWidgets.QDialog()
        self.ui = login_o()
        self.ui.setupUi(self.wwim)
        self.wwim.show()
        self.dialog.close()


#safhe vorod operature be hesab mojod az ghabl
class login_o(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 593)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 631, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 161, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(260, 190, 171, 51))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 270, 171, 51))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 190, 121, 31))
        self.label_3.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 270, 121, 41))
        self.label_4.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchs_o)
        self.pushButton.setGeometry(QtCore.QRect(120, 360, 291, 51))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchupo)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 450, 261, 91))
        self.label_5.setStyleSheet("font: 14pt \"MV Boli\";\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**log in**"))
        self.label_3.setText(_translate("Dialog", "username:"))
        self.label_4.setText(_translate("Dialog", "password:"))
        self.pushButton.setText(_translate("Dialog", "log in"))
        self.pushButton_2.setText(_translate("dialog", "back"))

    def switchs_o(self):
        self.wwim = QtWidgets.QDialog()
        self.ui = s_oper()
        self.ui.setupUi(self.wwim)
        self.wwim.show()
        self.dialog.close()

    def switchupo(self):
        self.wwim = QtWidgets.QDialog()
        self.ui = inup_o()
        self.ui.setupUi(self.wwim)
        self.wwim.show()
        self.dialog.close()


#safhe sabt nam moshtary
class Umoshtary(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
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
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchinup_m)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton_2")
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
        self.pushButton_2.setText(_translate("Dialog", "back"))


    def switchaccount(self):
        self.wen = QtWidgets.QDialog()
        self.ui = Uiaccount()
        self.ui.setupUi(self.wen)
        self.wen.show()
        self.dialog.close()


    def switchinup_m(self):
        self.eeu = QtWidgets.QDialog()
        self.ui = inup_m()
        self.ui.setupUi(self.eeu)
        self.eeu.show()
        self.dialog.close()

#sakht ekant moshtary
class Uiaccount(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 573)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 611, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
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
        self.pushButton.clicked.connect(self.switchsafhemosh)
        self.pushButton.setGeometry(QtCore.QRect(450, 260, 121, 81))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 218, 5);\n"
"font: 16pt \"mv boli\";\n"
"border:1px solid yellow")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2= QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchsaffhevorod)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 520, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.dialog = Dialog
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
        self.pushButton_2.setText(_translate("Dialog", "back"))

    def switchsafhemosh(self):
        self.eep = QtWidgets.QDialog()
        self.ui = safhe_m()
        self.ui.setupUi(self.eep)
        self.eep.show()
        self.dialog.close()


    def switchsaffhevorod(self):
        self.eee = QtWidgets.QDialog()
        self.ui =Umoshtary()
        self.ui.setupUi(self.eee)
        self.eee.show()
        self.dialog.close()

#safhe asli moshtary dar barname
class safhe_m(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 592)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 621, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchprofile)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 131, 51))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchgropp)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 10, 131, 51))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.switchwallet)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 80, 131, 51))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 150, 571, 381))
        self.tabWidget.setStyleSheet("border-radius: 65px 20px 100px 0px;\n"
"border-color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 161, 41))
        self.label_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 255, 127);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 10, 161, 41))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 255, 127);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 12pt \"MV Boli\";\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 511, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.clicked.connect(self.switchlist)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 80, 131, 51))
        self.pushButton_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.clicked.connect(self.switchsvm)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "profile"))
        self.pushButton_2.setText(_translate("Dialog", "grouping"))
        self.pushButton_3.setText(_translate("Dialog", "wallet"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_4.setText(_translate("Dialog", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "fave list"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "list kharid history"))
        self.pushButton_5.setText(_translate("Dialog", "lists"))
        self.pushButton_6.setText(_translate("Dialog", "back"))

    def switchsvm(self):
        self.lisst= QtWidgets.QDialog()
        self.ui = safhe_vorod()
        self.ui.setupUi(self.lisst)
        self.lisst.show()
        self.dialog.close()

    def switchlist(self):
        self.lisst= QtWidgets.QDialog()
        self.ui = lists()
        self.ui.setupUi(self.lisst)
        self.lisst.show()
        self.dialog.close()

    def switchprofile(self):
        self.pro = QtWidgets.QDialog()
        self.ui = profile()
        self.ui.setupUi(self.pro)
        self.pro.show()
        self.dialog.close()

    def switchwallet(self):
        self.wall = QtWidgets.QDialog()
        self.ui = wallet()
        self.ui.setupUi(self.wall)
        self.wall.show()
        self.dialog.close()

    def switchgropp(self):
       self.ddd = QtWidgets.QDialog()
       self.ui = grouping()
       self.ui.setupUi(self.ddd)
       self.ddd.show()
       self.dialog.close()

#safhe list sefareshat moshtry
class lists(object):
    def setupUi(self, Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(594, 591)
            self.label = QtWidgets.QLabel(Dialog)
            self.label.setGeometry(QtCore.QRect(-10, -10, 631, 611))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(Dialog)
            self.label_2.setGeometry(QtCore.QRect(20, 20, 111, 41))
            self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(Dialog)
            self.label_3.setGeometry(QtCore.QRect(40, 130, 471, 31))
            self.label_3.setStyleSheet("font: 14pt \"MV Boli\";")
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(Dialog)
            self.label_4.setGeometry(QtCore.QRect(40, 190, 461, 31))
            self.label_4.setStyleSheet("font: 14pt \"MV Boli\";")
            self.label_4.setObjectName("label_4")
            self.label_5 = QtWidgets.QLabel(Dialog)
            self.label_5.setGeometry(QtCore.QRect(40, 250, 471, 31))
            self.label_5.setStyleSheet("font: 14pt \"MV Boli\";")
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(Dialog)
            self.label_6.setGeometry(QtCore.QRect(40, 300, 451, 41))
            self.label_6.setStyleSheet("font: 14pt \"MV Boli\";")
            self.label_6.setObjectName("label_6")
            self.label_7 = QtWidgets.QLabel(Dialog)
            self.label_7.setGeometry(QtCore.QRect(40, 360, 481, 41))
            self.label_7.setStyleSheet("font: 14pt \"MV Boli\";")
            self.label_7.setObjectName("label_7")
            self.label_8 = QtWidgets.QLabel(Dialog)
            self.label_8.setGeometry(QtCore.QRect(40, 430, 481, 41))
            self.label_8.setStyleSheet("font: 14pt \"MV Boli\";")
            self.label_8.setObjectName("label_8")
            self.label_9 = QtWidgets.QLabel(Dialog)
            self.label_9.setGeometry(QtCore.QRect(40, 500, 491, 41))
            self.label_9.setStyleSheet("font: 14pt \"MV Boli\";")
            self.label_9.setObjectName("label_9")
            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.clicked.connect(self.switchsfm)
            self.pushButton.setGeometry(QtCore.QRect(470, 540, 121, 41))
            self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(255, 239, 6);\n"
                                          "border-color:rgb(255, 239, 6);\n"
                                          "border: 1px solid yellow;\n"
                                          "font: 14pt \"MV Boli\";")
            self.pushButton.setObjectName("pushButton")
            self.dialog = Dialog
            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.label_2.setText(_translate("Dialog", "**lists**"))
            self.label_3.setText(_translate("Dialog", "TextLabel"))
            self.label_4.setText(_translate("Dialog", "TextLabel"))
            self.label_5.setText(_translate("Dialog", "TextLabel"))
            self.label_6.setText(_translate("Dialog", "TextLabel"))
            self.label_7.setText(_translate("Dialog", "TextLabel"))
            self.label_8.setText(_translate("Dialog", "TextLabel"))
            self.label_9.setText(_translate("Dialog", "TextLabel"))
            self.pushButton.setText(_translate("Dialog", "back"))



    def switchsfm(self):
        self.slt = QtWidgets.QDialog()
        self.ui = safhe_m()
        self.ui.setupUi(self.slt)
        self.slt.show()
        self.dialog.close()


#safhe profile moshtry
class profile(object):
    def setupUi(self, Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(596, 592)
            self.label = QtWidgets.QLabel(Dialog)
            self.label.setGeometry(QtCore.QRect(0, -10, 621, 621))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(Dialog)
            self.label_2.setGeometry(QtCore.QRect(30, 20, 151, 51))
            self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(Dialog)
            self.label_3.setGeometry(QtCore.QRect(60, 160, 81, 31))
            self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(Dialog)
            self.label_4.setGeometry(QtCore.QRect(40, 230, 111, 31))
            self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_4.setObjectName("label_4")
            self.label_5 = QtWidgets.QLabel(Dialog)
            self.label_5.setGeometry(QtCore.QRect(50, 300, 101, 31))
            self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(Dialog)
            self.label_6.setGeometry(QtCore.QRect(30, 360, 151, 41))
            self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_6.setObjectName("label_6")
            self.label_7 = QtWidgets.QLabel(Dialog)
            self.label_7.setGeometry(QtCore.QRect(230, 160, 191, 31))
            self.label_7.setStyleSheet("font: 12pt \"MV Boli\";")
            self.label_7.setObjectName("label_7")
            self.label_8 = QtWidgets.QLabel(Dialog)
            self.label_8.setGeometry(QtCore.QRect(230, 230, 191, 31))
            self.label_8.setStyleSheet("font: 12pt \"MV Boli\";")
            self.label_8.setObjectName("label_8")
            self.label_9 = QtWidgets.QLabel(Dialog)
            self.label_9.setGeometry(QtCore.QRect(230, 300, 191, 31))
            self.label_9.setStyleSheet("font: 12pt \"MV Boli\";")
            self.label_9.setObjectName("label_9")
            self.label_10 = QtWidgets.QLabel(Dialog)
            self.label_10.setGeometry(QtCore.QRect(230, 360, 191, 31))
            self.label_10.setStyleSheet("font: 12pt \"MV Boli\";")
            self.label_10.setObjectName("label_10")
            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.clicked.connect(self.switchedit)
            self.pushButton.setGeometry(QtCore.QRect(80, 470, 151, 51))
            self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(255, 239, 6);\n"
                                          "border-color:rgb(255, 239, 6);\n"
                                          "border: 1px solid yellow;\n"
                                          "font: 14pt \"MV Boli\";")
            self.pushButton.setObjectName("pushButton")
            self.pushButton_2 = QtWidgets.QPushButton(Dialog)
            self.pushButton_2.clicked.connect(self.switchsm)
            self.pushButton_2.setGeometry(QtCore.QRect(360, 470, 151, 51))
            self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                            "background-color: rgb(255, 239, 6);\n"
                                            "border-color:rgb(255, 239, 6);\n"
                                            "border: 1px solid yellow;\n"
                                            "font: 14pt \"MV Boli\";")
            self.pushButton_2.setObjectName("pushButton_2")
            self.dialog = Dialog
            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.label_2.setText(_translate("Dialog", "**profile**"))
            self.label_3.setText(_translate("Dialog", "name:"))
            self.label_4.setText(_translate("Dialog", "last name:"))
            self.label_5.setText(_translate("Dialog", "username:"))
            self.label_6.setText(_translate("Dialog", "phone number:"))
            self.label_7.setText(_translate("Dialog", "TextLabel"))
            self.label_8.setText(_translate("Dialog", "TextLabel"))
            self.label_9.setText(_translate("Dialog", "TextLabel"))
            self.label_10.setText(_translate("Dialog", "TextLabel"))
            self.pushButton.setText(_translate("Dialog", "edit"))
            self.pushButton_2.setText(_translate("Dialog", "back"))

    def switchedit(self):
            self.edi = QtWidgets.QDialog()
            self.ui = edit()
            self.ui.setupUi(self.edi)
            self.edi.show()
            self.dialog.close()

    def switchsm(self):
        self.pro = QtWidgets.QDialog()
        self.ui = safhe_m()
        self.ui.setupUi(self.pro)
        self.pro.show()
        self.dialog.close()


class edit(object):
    def setupUi(self, Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(596, 590)
            self.label = QtWidgets.QLabel(Dialog)
            self.label.setGeometry(QtCore.QRect(-20, -10, 661, 621))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(Dialog)
            self.label_2.setGeometry(QtCore.QRect(20, 20, 121, 41))
            self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(Dialog)
            self.label_3.setGeometry(QtCore.QRect(40, 130, 71, 41))
            self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(Dialog)
            self.label_4.setGeometry(QtCore.QRect(20, 200, 111, 31))
            self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_4.setObjectName("label_4")
            self.label_5 = QtWidgets.QLabel(Dialog)
            self.label_5.setGeometry(QtCore.QRect(10, 260, 141, 31))
            self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(Dialog)
            self.label_6.setGeometry(QtCore.QRect(40, 320, 61, 31))
            self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_6.setObjectName("label_6")
            self.label_7 = QtWidgets.QLabel(Dialog)
            self.label_7.setGeometry(QtCore.QRect(0, 380, 151, 31))
            self.label_7.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_7.setObjectName("label_7")
            self.label_8 = QtWidgets.QLabel(Dialog)
            self.label_8.setGeometry(QtCore.QRect(330, 140, 101, 31))
            self.label_8.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_8.setObjectName("label_8")
            self.label_9 = QtWidgets.QLabel(Dialog)
            self.label_9.setGeometry(QtCore.QRect(330, 200, 101, 31))
            self.label_9.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_9.setObjectName("label_9")
            self.label_10 = QtWidgets.QLabel(Dialog)
            self.label_10.setGeometry(QtCore.QRect(20, 440, 101, 31))
            self.label_10.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_10.setObjectName("label_10")
            self.label_11 = QtWidgets.QLabel(Dialog)
            self.label_11.setGeometry(QtCore.QRect(30, 500, 91, 31))
            self.label_11.setStyleSheet("font: 16pt \"MV Boli\";")
            self.label_11.setObjectName("label_11")
            self.lineEdit = QtWidgets.QLineEdit(Dialog)
            self.lineEdit.setGeometry(QtCore.QRect(160, 140, 151, 41))
            self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                        "background-color: rgb(253, 255, 79);\n"
                                        "border-color:rgb(253, 255, 79);\n"
                                        "border:1px solid yellow;\n"
                                        "font: 12pt \"MV Boli\";")
            self.lineEdit.setObjectName("lineEdit")
            self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
            self.lineEdit_2.setGeometry(QtCore.QRect(160, 200, 151, 41))
            self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(253, 255, 79);\n"
                                          "border-color:rgb(253, 255, 79);\n"
                                          "border:1px solid yellow;\n"
                                          "font: 12pt \"MV Boli\";")
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
            self.lineEdit_3.setGeometry(QtCore.QRect(160, 260, 151, 41))
            self.lineEdit_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(253, 255, 79);\n"
                                          "border-color:rgb(253, 255, 79);\n"
                                          "border:1px solid yellow;\n"
                                          "font: 12pt \"MV Boli\";")
            self.lineEdit_3.setObjectName("lineEdit_3")
            self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
            self.lineEdit_4.setGeometry(QtCore.QRect(160, 320, 151, 41))
            self.lineEdit_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(253, 255, 79);\n"
                                          "border-color:rgb(253, 255, 79);\n"
                                          "border:1px solid yellow;\n"
                                          "font: 12pt \"MV Boli\";")
            self.lineEdit_4.setObjectName("lineEdit_4")
            self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
            self.lineEdit_5.setGeometry(QtCore.QRect(160, 380, 151, 41))
            self.lineEdit_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(253, 255, 79);\n"
                                          "border-color:rgb(253, 255, 79);\n"
                                          "border:1px solid yellow;\n"
                                          "font: 12pt \"MV Boli\";")
            self.lineEdit_5.setObjectName("lineEdit_5")
            self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
            self.lineEdit_6.setGeometry(QtCore.QRect(160, 440, 151, 41))
            self.lineEdit_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(253, 255, 79);\n"
                                          "border-color:rgb(253, 255, 79);\n"
                                          "border:1px solid yellow;\n"
                                          "font: 12pt \"MV Boli\";")
            self.lineEdit_6.setObjectName("lineEdit_6")
            self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
            self.lineEdit_7.setGeometry(QtCore.QRect(160, 500, 151, 81))
            self.lineEdit_7.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(253, 255, 79);\n"
                                          "border-color:rgb(253, 255, 79);\n"
                                          "border:1px solid yellow;\n"
                                          "font: 12pt \"MV Boli\";")
            self.lineEdit_7.setObjectName("lineEdit_7")
            self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
            self.lineEdit_8.setGeometry(QtCore.QRect(440, 140, 141, 41))
            self.lineEdit_8.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(253, 255, 79);\n"
                                          "border-color:rgb(253, 255, 79);\n"
                                          "border:1px solid yellow;\n"
                                          "font: 12pt \"MV Boli\";")
            self.lineEdit_8.setObjectName("lineEdit_8")
            self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
            self.lineEdit_9.setGeometry(QtCore.QRect(440, 200, 141, 41))
            self.lineEdit_9.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(253, 255, 79);\n"
                                          "border-color:rgb(253, 255, 79);\n"
                                          "border:1px solid yellow;\n"
                                          "font: 12pt \"MV Boli\";")
            self.lineEdit_9.setObjectName("lineEdit_9")
            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.setGeometry(QtCore.QRect(390, 320, 141, 61))
            self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                          "background-color: rgb(255, 239, 6);\n"
                                          "border-color:rgb(255, 239, 6);\n"
                                          "border: 1px solid yellow;\n"
                                          "font: 14pt \"MV Boli\";")
            self.pushButton.setObjectName("pushButton")
            self.pushButton_2 = QtWidgets.QPushButton(Dialog)
            self.pushButton_2.clicked.connect(self.switchpro)
            self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
            self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                            "background-color: rgb(255, 239, 6);\n"
                                            "border-color:rgb(255, 239, 6);\n"
                                            "border: 1px solid yellow;\n"
                                            "font: 14pt \"MV Boli\";")
            self.pushButton_2.setObjectName("pushButton_2")
            self.label_12 = QtWidgets.QLabel(Dialog)
            self.label_12.setGeometry(QtCore.QRect(380, 400, 171, 51))
            self.label_12.setStyleSheet("font: 12pt \"MV Boli\";")
            self.label_12.setObjectName("label_12")
            self.dialog = Dialog
            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.label_2.setText(_translate("Dialog", "**edit**"))
            self.label_3.setText(_translate("Dialog", "name:"))
            self.label_4.setText(_translate("Dialog", "last name:"))
            self.label_5.setText(_translate("Dialog", "national code:"))
            self.label_6.setText(_translate("Dialog", "email:"))
            self.label_7.setText(_translate("Dialog", "phone number:"))
            self.label_8.setText(_translate("Dialog", "username:"))
            self.label_9.setText(_translate("Dialog", "password:"))
            self.label_10.setText(_translate("Dialog", "birthdate:"))
            self.label_11.setText(_translate("Dialog", "address:"))
            self.pushButton.setText(_translate("Dialog", "done"))
            self.pushButton_2.setText(_translate("Dialog", "back"))
            self.label_12.setText(_translate("Dialog", "TextLabel"))

    def switchpro(self):
        self.edi = QtWidgets.QDialog()
        self.ui = profile()
        self.ui.setupUi(self.edi)
        self.edi.show()
        self.dialog.close()


#safhe kif pol moshtry
class wallet(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 651, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 141, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 101, 31))
        self.label_3.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 91, 41))
        self.label_4.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 220, 161, 41))
        self.lineEdit.setStyleSheet("border-radius: 15px 10px 50px 0px;\n"
"font: 12pt \"MV Boli\";\n"
"background-color:rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(190, 290, 151, 41))
        self.label_5.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 330, 131, 51))
        self.pushButton.setStyleSheet("border-radius: 15px 10px 50px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchsmw)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**wallet**"))
        self.label_3.setText(_translate("Dialog", "deposit:"))
        self.label_4.setText(_translate("Dialog", "balance:"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "done"))
        self.pushButton_2.setText(_translate("Dialog", "back"))




    def switchsmw(self):
        self.wsm = QtWidgets.QDialog()
        self.ui = safhe_m()
        self.ui.setupUi(self.wsm)
        self.wsm.show()
        self.dialog.close()

#safhe asli foroshande
class safhe_f(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 593)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -20, 641, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchprosf)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchwleet)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 70, 111, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.switchlistf)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 10, 111, 41))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.clicked.connect(self.switchacty)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 70, 111, 41))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 130, 551, 381))
        self.tabWidget.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(420, 20, 61, 41))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 381, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 381, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_2.setGeometry(QtCore.QRect(420, 80, 61, 41))
        self.spinBox_2.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 381, 41))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_3.setGeometry(QtCore.QRect(420, 140, 61, 41))
        self.spinBox_3.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 381, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.spinBox_4 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_4.setGeometry(QtCore.QRect(420, 200, 61, 41))
        self.spinBox_4.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 381, 41))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.spinBox_5 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_5.setGeometry(QtCore.QRect(420, 260, 61, 41))
        self.spinBox_5.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.spinBox_5.setObjectName("spinBox_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 381, 41))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 80, 381, 41))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 140, 381, 41))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(20, 200, 381, 41))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(20, 260, 381, 41))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.label_11.setObjectName("label_11")
        self.spinBox_6 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_6.setGeometry(QtCore.QRect(420, 20, 61, 41))
        self.spinBox_6.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_7.setGeometry(QtCore.QRect(420, 80, 61, 41))
        self.spinBox_7.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_8.setGeometry(QtCore.QRect(420, 140, 61, 41))
        self.spinBox_8.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_9 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_9.setGeometry(QtCore.QRect(420, 200, 61, 41))
        self.spinBox_9.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_10 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_10.setGeometry(QtCore.QRect(420, 260, 61, 41))
        self.spinBox_10.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MV Boli\";")
        self.spinBox_10.setObjectName("spinBox_10")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.clicked.connect(self.switchfacc)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "profile"))
        self.pushButton_2.setText(_translate("Dialog", "wallet"))
        self.pushButton_3.setText(_translate("Dialog", "lists"))
        self.pushButton_4.setText(_translate("Dialog", "accountancy"))
        self.pushButton_5.setText(_translate("Dialog", "back"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "product1"))
        self.label_7.setText(_translate("Dialog", "TextLabel"))
        self.label_8.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "TextLabel"))
        self.label_10.setText(_translate("Dialog", "TextLabel"))
        self.label_11.setText(_translate("Dialog", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "product2"))

    def switchlistf(self):
        self.lisf = QtWidgets.QDialog()
        self.ui = listf()
        self.ui.setupUi(self.lisf)
        self.lisf.show()
        self.dialog.close()

    def switchacty(self):
        self.act = QtWidgets.QDialog()
        self.ui = acty()
        self.ui.setupUi(self.act)
        self.act.show()
        self.dialog.close()

    def switchprosf(self):
        self.psf = QtWidgets.QDialog()
        self.ui = profile()
        self.ui.setupUi(self.psf)
        self.psf.show()
        self.dialog.close()

    def switchwleet(self):
        self.wlee = QtWidgets.QDialog()
        self.ui = walleet()
        self.ui.setupUi(self.wlee)
        self.wlee.show()
        self.dialog.close()

    def switchfacc(self):
        self.wlee = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.wlee)
        self.wlee.show()
        self.dialog.close()

#safhe profile foroshande
class profile(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 592)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 621, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 151, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 81, 31))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 111, 31))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 300, 101, 31))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 360, 151, 41))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(230, 160, 191, 31))
        self.label_7.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(230, 230, 191, 31))
        self.label_8.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(230, 300, 191, 31))
        self.label_9.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(230, 360, 191, 31))
        self.label_10.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchedit)
        self.pushButton.setGeometry(QtCore.QRect(80, 470, 151, 51))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchsf)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 470, 151, 51))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**profile**"))
        self.label_3.setText(_translate("Dialog", "name:"))
        self.label_4.setText(_translate("Dialog", "last name:"))
        self.label_5.setText(_translate("Dialog", "username:"))
        self.label_6.setText(_translate("Dialog", "phone number:"))
        self.label_7.setText(_translate("Dialog", "TextLabel"))
        self.label_8.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "TextLabel"))
        self.label_10.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "edit"))
        self.pushButton_2.setText(_translate("Dialog", "back"))

    def switchedit(self):
        self.edi = QtWidgets.QDialog()
        self.ui = edit()
        self.ui.setupUi(self.edi)
        self.edi.show()
        self.dialog.close()

    def switchsf(self):
        self.edi = QtWidgets.QDialog()
        self.ui = safhe_f ()
        self.ui.setupUi(self.edi)
        self.edi.show()
        self.dialog.close()

#safhe edit etelaat profile foroshande
class edit(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 590)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-20, -10, 661, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 121, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 71, 41))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 111, 31))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 141, 31))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 320, 61, 31))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 380, 151, 31))
        self.label_7.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(330, 140, 101, 31))
        self.label_8.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(330, 200, 101, 31))
        self.label_9.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 440, 101, 31))
        self.label_10.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(30, 500, 91, 31))
        self.label_11.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 140, 151, 41))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 200, 151, 41))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 260, 151, 41))
        self.lineEdit_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 320, 151, 41))
        self.lineEdit_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 380, 151, 41))
        self.lineEdit_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 440, 151, 41))
        self.lineEdit_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 500, 151, 81))
        self.lineEdit_7.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(440, 140, 141, 41))
        self.lineEdit_8.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(440, 200, 141, 41))
        self.lineEdit_9.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 320, 141, 61))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchpro)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(380, 400, 171, 51))
        self.label_12.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_12.setObjectName("label_12")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**edit**"))
        self.label_3.setText(_translate("Dialog", "name:"))
        self.label_4.setText(_translate("Dialog", "last name:"))
        self.label_5.setText(_translate("Dialog", "national code:"))
        self.label_6.setText(_translate("Dialog", "email:"))
        self.label_7.setText(_translate("Dialog", "phone number:"))
        self.label_8.setText(_translate("Dialog", "username:"))
        self.label_9.setText(_translate("Dialog", "password:"))
        self.label_10.setText(_translate("Dialog", "birthdate:"))
        self.label_11.setText(_translate("Dialog", "address:"))
        self.pushButton.setText(_translate("Dialog", "done"))
        self.pushButton_2.setText(_translate("Dialog", "back"))
        self.label_12.setText(_translate("Dialog", "TextLabel"))



    def switchpro(self):
        self.edi = QtWidgets.QDialog()
        self.ui = profile()
        self.ui.setupUi(self.edi)
        self.edi.show()
        self.dialog.close()

#safhe kifpol foroshande
class walleet(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 587)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 621, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 141, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 101, 31))
        self.label_3.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 141, 31))
        self.label_4.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 330, 91, 41))
        self.label_5.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 180, 161, 41))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 260, 161, 41))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(200, 340, 151, 31))
        self.label_6.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 330, 131, 51))
        self.pushButton.setStyleSheet("border-radius: 15px 10px 50px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchsfw)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**wallet**"))
        self.label_3.setText(_translate("Dialog", "deposit:"))
        self.label_4.setText(_translate("Dialog", "withdrawal:"))
        self.label_5.setText(_translate("Dialog", "balance:"))
        self.label_6.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "done"))
        self.pushButton_2.setText(_translate("Dialog", "back"))


    def switchsfw(self):
        self.wlee = QtWidgets.QDialog()
        self.ui = safhe_f()
        self.ui.setupUi(self.wlee)
        self.wlee.show()
        self.dialog.close()

#safhe list sefareshat foroshnde
class listf(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 631, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 111, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 471, 31))
        self.label_3.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 461, 31))
        self.label_4.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 471, 31))
        self.label_5.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 300, 451, 41))
        self.label_6.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 360, 481, 41))
        self.label_7.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 430, 481, 41))
        self.label_8.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 500, 491, 41))
        self.label_9.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchsfl)
        self.pushButton.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**lists**"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "TextLabel"))
        self.label_7.setText(_translate("Dialog", "TextLabel"))
        self.label_8.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "back"))

    def switchsfl(self):
        self.lisf = QtWidgets.QDialog()
        self.ui = safhe_f()
        self.ui.setupUi(self.lisf)
        self.lisf.show()
        self.dialog.close()

#safhe foroshande baraye etelaa az karname mali
class acty(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(598, 589)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 611, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 241, 61))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 451, 51))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 441, 51))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 300, 451, 51))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 370, 471, 51))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchsfact)
        self.pushButton.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**accountancy**"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "back"))

    def switchsfact(self):
        self.act = QtWidgets.QDialog()
        self.ui = safhe_f()
        self.ui.setupUi(self.act)
        self.act.show()
        self.dialog.close()






#safhe foroshande
class Uforoshande(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 590)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
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
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchssafhevorod)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
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
        self.pushButton_2.setText(_translate("Dialog", "back"))

    def switchfaccount(self):
        self.win = QtWidgets.QDialog()
        self.ui = faccount()
        self.ui.setupUi(self.win)
        self.win.show()
        self.dialog.close()

    def switchssafhevorod(self):
        self.eee = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.eee)
        self.eee.show()
        self.dialog.close()

#safhe sakht account foroshande
class faccount(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 589)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 621, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
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
        self.pushButton.clicked.connect(self.switchsff)
        self.pushButton.setGeometry(QtCore.QRect(450, 270, 121, 71))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchforoshandeee)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.dialog = Dialog
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
        self.pushButton_2.setText(_translate("Dialog", "back"))

    def switchforoshandeee(self):
        self.eee = QtWidgets.QDialog()
        self.ui = Uforoshande()
        self.ui.setupUi(self.eee)
        self.eee.show()
        self.dialog.close()

    def switchsff(self):
        self.sff = QtWidgets.QDialog()
        self.ui = safhe_f()
        self.ui.setupUi(self.sff)
        self.sff.show()
        self.dialog.close()

#safhe vorod operature
class Uoperature(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(598, 588)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
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
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchinup_o)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
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
        self.pushButton_2.setText(_translate("Dialog", "back"))
        self.comboBox.setItemText(0, _translate("Dialog", "woman"))
        self.comboBox.setItemText(1, _translate("Dialog", "man"))



    def switchoaccount(self):
        self.wan = QtWidgets.QDialog()
        self.ui = oaccount()
        self.ui.setupUi(self.wan)
        self.wan.show()
        self.dialog.close()

    def switchsaafhevorod(self):
        self.eee = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.eee)
        self.eee.show()
        self.dialog.close()

    def switchinup_o(self):
        self.wwim = QtWidgets.QDialog()
        self.ui = inup_o()
        self.ui.setupUi(self.wwim)
        self.wwim.show()
        self.dialog.close()


#safhe sakht account operature
class oaccount(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 0, 621, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
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
        self.pushButton.clicked.connect(self.switchsoac)
        self.pushButton.setGeometry(QtCore.QRect(430, 260, 131, 81))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"font: 16pt \"MV Boli\";\n"
"border:1px solid yellow;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2= QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchsoperature)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.dialog= Dialog
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
        self.pushButton_2.setText(_translate("Dialog", "back"))

    def switchsoperature(self):
        self.eee = QtWidgets.QDialog()
        self.ui = Uoperature()
        self.ui.setupUi(self.eee)
        self.eee.show()
        self.dialog.close()

    def switchsoac(self):
        self.soac = QtWidgets.QDialog()
        self.ui = s_oper()
        self.ui.setupUi(self.soac)
        self.soac.show()
        self.dialog.close()

#safhe asli operature
class s_oper(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 590)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 651, 631))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchpop)
        self.pushButton.setGeometry(QtCore.QRect(130, 240, 131, 61))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.clicked.connect(self.switchlistop)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 240, 131, 61))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.clicked.connect(self.switchsac)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_7.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 201, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Profile"))
        self.pushButton_4.setText(_translate("Dialog", "lists"))
        self.pushButton_7.setText(_translate("Dialog", "back"))

        self.label_2.setText(_translate("Dialog", "**operature**"))

    def switchsac(self):
        self.pop = QtWidgets.QDialog()
        self.ui = oaccount()
        self.ui.setupUi(self.pop)
        self.pop.show()
        self.dialog.close()

    def switchlistop(self):
        self.liop = QtWidgets.QDialog()
        self.ui = Ui_listop()
        self.ui.setupUi(self.liop)
        self.liop.show()
        self.dialog.close()

    def switchpop(self):
        self.pop = QtWidgets.QDialog()
        self.ui = profile_operature()
        self.ui.setupUi(self.pop)
        self.pop.show()
        self.dialog.close()

#safhe profile operature
class profile_operature(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 592)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 621, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 151, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 81, 31))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 111, 31))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 300, 101, 31))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 360, 151, 41))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(230, 160, 191, 31))
        self.label_7.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(230, 230, 191, 31))
        self.label_8.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(230, 300, 191, 31))
        self.label_9.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(230, 360, 191, 31))
        self.label_10.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchedit)
        self.pushButton.setGeometry(QtCore.QRect(80, 470, 151, 51))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchso)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 470, 151, 51))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**profile**"))
        self.label_3.setText(_translate("Dialog", "name:"))
        self.label_4.setText(_translate("Dialog", "last name:"))
        self.label_5.setText(_translate("Dialog", "username:"))
        self.label_6.setText(_translate("Dialog", "phone number:"))
        self.label_7.setText(_translate("Dialog", "TextLabel"))
        self.label_8.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "TextLabel"))
        self.label_10.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "edit"))
        self.pushButton_2.setText(_translate("Dialog", "back"))

    def switchedit(self):
        self.edi = QtWidgets.QDialog()
        self.ui = edit()
        self.ui.setupUi(self.edi)
        self.edi.show()
        self.dialog.close()

    def switchso(self):
        self.edi = QtWidgets.QDialog()
        self.ui = s_oper()
        self.ui.setupUi(self.edi)
        self.edi.show()
        self.dialog.close()

#safhe edit etelaat profile operature
class edit(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 590)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-20, -10, 661, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 121, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 71, 41))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 111, 31))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 141, 31))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 320, 61, 31))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 380, 151, 31))
        self.label_7.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(330, 140, 101, 31))
        self.label_8.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(330, 200, 101, 31))
        self.label_9.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 440, 101, 31))
        self.label_10.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(30, 500, 91, 31))
        self.label_11.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 140, 151, 41))
        self.lineEdit.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 200, 151, 41))
        self.lineEdit_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 260, 151, 41))
        self.lineEdit_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 320, 151, 41))
        self.lineEdit_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 380, 151, 41))
        self.lineEdit_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 440, 151, 41))
        self.lineEdit_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 500, 151, 81))
        self.lineEdit_7.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(440, 140, 141, 41))
        self.lineEdit_8.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(440, 200, 141, 41))
        self.lineEdit_9.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 320, 141, 61))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchpro)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(380, 400, 171, 51))
        self.label_12.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_12.setObjectName("label_12")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**edit**"))
        self.label_3.setText(_translate("Dialog", "name:"))
        self.label_4.setText(_translate("Dialog", "last name:"))
        self.label_5.setText(_translate("Dialog", "national code:"))
        self.label_6.setText(_translate("Dialog", "email:"))
        self.label_7.setText(_translate("Dialog", "phone number:"))
        self.label_8.setText(_translate("Dialog", "username:"))
        self.label_9.setText(_translate("Dialog", "password:"))
        self.label_10.setText(_translate("Dialog", "birthdate:"))
        self.label_11.setText(_translate("Dialog", "address:"))
        self.pushButton.setText(_translate("Dialog", "done"))
        self.pushButton_2.setText(_translate("Dialog", "back"))
        self.label_12.setText(_translate("Dialog", "TextLabel"))



    def switchpro(self):
        self.edi = QtWidgets.QDialog()
        self.ui = profile_operature()
        self.ui.setupUi(self.edi)
        self.edi.show()
        self.dialog.close()

#safhe list operature
class Ui_listop(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 588)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 631, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 131, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 311, 51))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 311, 51))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 310, 311, 51))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(510, 120, 71, 51))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 120, 71, 51))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 200, 71, 51))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 200, 71, 51))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 300, 71, 51))
        self.pushButton_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 300, 71, 51))
        self.pushButton_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.clicked.connect(self.switchso)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_7.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**lists**"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "delete"))
        self.pushButton_2.setText(_translate("Dialog", "accept"))
        self.pushButton_3.setText(_translate("Dialog", "accept"))
        self.pushButton_4.setText(_translate("Dialog", "delete"))
        self.pushButton_5.setText(_translate("Dialog", "accept"))
        self.pushButton_6.setText(_translate("Dialog", "delete"))
        self.pushButton_7.setText(_translate("Dialog", "back"))


    def switchso(self):
        self.liop = QtWidgets.QDialog()
        self.ui =s_oper ()
        self.ui.setupUi(self.liop)
        self.liop.show()
        self.dialog.close()








#safhe dste bandy mahsolat foroshgah
class grouping(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -20, 631, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 151, 91))
        self.pushButton.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 240, 151, 91))
        self.pushButton_2.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 240, 151, 91))
        self.pushButton_3.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 240, 151, 91))
        self.pushButton_4.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 390, 151, 91))
        self.pushButton_6.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 390, 151, 91))
        self.pushButton_7.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 390, 151, 91))
        self.pushButton_5.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.clicked.connect(self.switchsvg)
        self.pushButton_8.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_8.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**grouping**"))
        self.pushButton.setText(_translate("Dialog", "digital"))
        self.pushButton_2.setText(_translate("Dialog", "clothing"))
        self.pushButton_3.setText(_translate("Dialog", "cosmetics"))
        self.pushButton_4.setText(_translate("Dialog", "stationery"))
        self.pushButton_6.setText(_translate("Dialog", "supermarket "))
        self.pushButton_7.setText(_translate("Dialog", "toy"))
        self.pushButton_5.setText(_translate("Dialog", "sports"))
        self.pushButton_8.setText(_translate("Dialog", "back"))


    def switchsvg(self):
        self.group = QtWidgets.QDialog()
        self.ui = safhe_vorod()
        self.ui.setupUi(self.group)
        self.group.show()
        self.dialog.close()

#sfhe darbareye ma
class Uabout_us(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(598, 593)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -20, 611, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchhistory)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 211, 151))
        self.pushButton.setStyleSheet("border-radius: 85px 70px 300px 0px;\n"
"border:2px solid yellow;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"font: 22pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchgoal)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 300, 151, 101))
        self.pushButton_2.setStyleSheet("border-radius: 65px 50px 100px 0px;\n"
"border:2px solid yellow;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.switchimportant)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 280, 151, 61))
        self.pushButton_3.setStyleSheet("border-radius: 45px 30px 100px 0px;\n"
"border:2px solid yellow;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"font: 12pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.clicked.connect(self.switchcontact)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 450, 141, 91))
        self.pushButton_4.setStyleSheet("border-radius: 65px 40px 100px 0px;\n"
"border:2px solid yellow;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.clicked.connect(self.switchcomment)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 120, 101, 61))
        self.pushButton_5.setStyleSheet("border-radius: 45px 30px 100px 0px;\n"
"border:2px solid yellow;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"font: 12pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.clicked.connect(self.switchsvorod)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 520, 121, 41))
        self.pushButton_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 0, 191, 81))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "history"))
        self.pushButton_2.setText(_translate("Dialog", "our goal"))
        self.pushButton_3.setText(_translate("Dialog", "important question"))
        self.pushButton_4.setText(_translate("Dialog", "contact us"))
        self.pushButton_5.setText(_translate("Dialog", "comments"))
        self.pushButton_6.setText(_translate("Dialog", "back"))
        self.label_2.setText(_translate("Dialog", "**about us**"))

    def switchimportant(self):
        self.rer = QtWidgets.QDialog()
        self.ui = Uimportantqu()
        self.ui.setupUi(self.rer)
        self.rer.show()
        self.dialog.close()

    def switchhistory(self):
       self.Dii = QtWidgets.QDialog()
       self.ui = Uhistory()
       self.ui.setupUi(self.Dii)
       self.Dii.show()
       self.dialog.close()

    def switchcontact(self):
        self.Dia = QtWidgets.QDialog()
        self.ui = Ucontact()
        self.ui.setupUi(self.Dia)
        self.Dia.show()
        self.dialog.close()

    def switchcomment(self):
       self.ghs = QtWidgets.QDialog()
       self.ui = comment()
       self.ui.setupUi(self.ghs)
       self.ghs.show()
       self.dialog.close()

    def switchgoal(self):
       self.gab = QtWidgets.QDialog()
       self.ui =Ugoal ()
       self.ui.setupUi(self.gab)
       self.gab.show()
       self.dialog.close()


    def switchsvorod(self):
        self.rer = QtWidgets.QDialog()
        self.ui = safhe_vorod()
        self.ui.setupUi(self.rer)
        self.rer.show()
        self.dialog.close()

#safhe soalat mohem
class Uimportantqu(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 588)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 621, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 341, 61))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 321, 31))
        self.label_3.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 380, 431, 31))
        self.label_4.setStyleSheet("font: 18pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 421, 31))
        self.label_5.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 421, 31))
        self.label_6.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 311, 31))
        self.label_7.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 470, 341, 31))
        self.label_8.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 510, 281, 31))
        self.label_9.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchabout)
        self.pushButton.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**important question**"))
        self.label_3.setText(_translate("Dialog", "1-why you should truse us?"))
        self.label_4.setText(_translate("Dialog", "2-have the comments been positive?"))
        self.label_5.setText(_translate("Dialog", "because we are here with the cooperation of the best"))
        self.label_6.setText(_translate("Dialog", "sellers in the country to try to create a safe and "))
        self.label_7.setText(_translate("Dialog", "enjoyable shopping environment for you"))
        self.label_8.setText(_translate("Dialog", "you can read other peoplescomments about"))
        self.label_9.setText(_translate("Dialog", "our collection on the about us page"))
        self.pushButton.setText(_translate("Dialog", "back"))


    def switchabout(self):
        self.eee = QtWidgets.QDialog()
        self.ui = Uabout_us()
        self.ui.setupUi(self.eee)
        self.eee.show()
        self.dialog.close()


#safhe tarikhcheye foroshgah
class Uhistory(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 592)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -20, 621, 631))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 161, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 481, 41))
        self.label_3.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 270, 471, 41))
        self.label_4.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 340, 461, 41))
        self.label_5.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 410, 221, 31))
        self.label_6.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchaboutt)
        self.pushButton.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**history**"))
        self.label_3.setText(_translate("Dialog", "our team started from a small student project, but"))
        self.label_4.setText(_translate("Dialog", "over time we tried to work with professional study"))
        self.label_5.setText(_translate("Dialog", "and effort,and we hope to be able to make more"))
        self.label_6.setText(_translate("Dialog", "progress in the future."))
        self.pushButton.setText(_translate("Dialog", "back"))





    def switchaboutt(self):
        self.ees = QtWidgets.QDialog()
        self.ui = Uabout_us()
        self.ui.setupUi(self.ees)
        self.ees.show()
        self.dialog.close()




#safhe ertebat ba ma
class Ucontact(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 604)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 0, 641, 631))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 211, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchconop)
        self.pushButton.setGeometry(QtCore.QRect(50, 180, 181, 31))
        self.pushButton.setStyleSheet("border-radius: 15px 10px 50px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color: rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchabouut)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 100, 101, 81))
        self.label_3.setStyleSheet("\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("photo_2021-06-28_02-48-38.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 301, 31))
        self.label_4.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 301, 31))
        self.label_5.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 350, 281, 31))
        self.label_6.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 410, 211, 61))
        self.label_7.setStyleSheet("font: 20pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 540, 331, 31))
        self.label_8.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 490, 351, 41))
        self.label_9.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**contact us**"))
        self.pushButton.setText(_translate("Dialog", "contact the operature"))
        self.pushButton_2.setText(_translate("Dialog", "back"))
        self.label_4.setText(_translate("Dialog", "phone number:  01344334555"))
        self.label_5.setText(_translate("Dialog", "email:   m2acampony@gmail.com"))
        self.label_6.setText(_translate("Dialog", "instagram:     m2a_company"))
        self.label_7.setText(_translate("Dialog", "**working hour**"))
        self.label_8.setText(_translate("Dialog", "thursday and friday from 10 to 12"))
        self.label_9.setText(_translate("Dialog", "saturday to wednesday from 8 to 12"))


    def switchabouut(self):
        self.Dio = QtWidgets.QDialog()
        self.ui =Uabout_us ()
        self.ui.setupUi(self.Dio)
        self.Dio.show()
        self.dialog.close()


    def switchconop(self):
       self.log = QtWidgets.QDialog()
       self.ui = conop()
       self.ui.setupUi(self.log)
       self.log.show()
       self.dialog.close()



#safhe ertebat ba operature
class conop(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(594, 590)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -30, 681, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 351, 61))
        self.label_2.setStyleSheet("font: 22pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 351, 41))
        self.label_3.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 151, 21))
        self.label_4.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 240, 71, 31))
        self.label_5.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 300, 101, 31))
        self.label_6.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 360, 141, 31))
        self.label_7.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 410, 81, 31))
        self.label_8.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 240, 151, 31))
        self.lineEdit.setStyleSheet("border-radius: 15px 10px 50px 0px;\n"
"font: 12pt \"MV Boli\";\n"
"background-color:rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 300, 151, 31))
        self.lineEdit_2.setStyleSheet("border-radius: 15px 10px 50px 0px;\n"
"font: 12pt \"MV Boli\";\n"
"background-color:rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 360, 151, 31))
        self.lineEdit_3.setStyleSheet("border-radius: 15px 10px 50px 0px;\n"
"font: 12pt \"MV Boli\";\n"
"background-color:rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 420, 151, 111))
        self.lineEdit_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"font: 12pt \"MV Boli\";\n"
"background-color:rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 320, 131, 61))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"font: 12pt \"MV Boli\";\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchconback)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**contact the operature**"))
        self.label_3.setText(_translate("Dialog", "you can send your message to the operature."))
        self.label_4.setText(_translate("Dialog", "wait for a reply..."))
        self.label_5.setText(_translate("Dialog", "name:"))
        self.label_6.setText(_translate("Dialog", "username:"))
        self.label_7.setText(_translate("Dialog", "phone number:"))
        self.label_8.setText(_translate("Dialog", "message:"))
        self.pushButton.setText(_translate("Dialog", "send message"))
        self.pushButton_2.setText(_translate("Dialog", "back"))

    def switchconback(self):
        self.alo = QtWidgets.QDialog()
        self.ui = Ucontact()
        self.ui.setupUi(self.alo)
        self.alo.show()
        self.dialog.close()



#safhe comment baraye foroshgah ma
class comment(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 592)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 611, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 201, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 301, 41))
        self.label_3.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 240, 71, 31))
        self.label_4.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 300, 61, 31))
        self.label_5.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 101, 31))
        self.label_6.setStyleSheet("font: 16pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(320, 320, 231, 31))
        self.horizontalSlider.setStyleSheet("gridline-color: rgb(255, 255, 127);\n"
"alternate-background-color: rgb(255, 255, 0);")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 240, 151, 31))
        self.lineEdit.setStyleSheet("border-radius: 15px 10px 50px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 300, 151, 31))
        self.lineEdit_2.setStyleSheet("border-radius: 15px 10px 50px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 370, 151, 171))
        self.lineEdit_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(253, 255, 79);\n"
"border-color:rgb(253, 255, 79);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(320, 280, 251, 31))
        self.label_7.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(320, 370, 31, 21))
        self.label_8.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(410, 370, 41, 21))
        self.label_9.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(500, 360, 61, 31))
        self.label_10.setStyleSheet("font: 12pt \"MV Boli\";")
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 420, 161, 51))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchuaboutus)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**comments**"))
        self.label_3.setText(_translate("Dialog", "please enter your comment..."))
        self.label_4.setText(_translate("Dialog", "name:"))
        self.label_5.setText(_translate("Dialog", "email:"))
        self.label_6.setText(_translate("Dialog", "comment:"))
        self.label_7.setText(_translate("Dialog", "your rating to our performance:"))
        self.label_8.setText(_translate("Dialog", "bad"))
        self.label_9.setText(_translate("Dialog", "good"))
        self.label_10.setText(_translate("Dialog", "perfect"))
        self.pushButton.setText(_translate("Dialog", "send comment"))
        self.pushButton_2.setText(_translate("Dialog", "back"))


    def switchuaboutus(self):
        self.us = QtWidgets.QDialog()
        self.ui = Uabout_us()
        self.ui.setupUi(self.us)
        self.us.show()
        self.dialog.close()

#safhe ahdaf ma dar in foroshgah
class Ugoal(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 631, 661))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 161, 31))
        self.label_3.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 581, 31))
        self.label_4.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 511, 31))
        self.label_5.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 320, 571, 31))
        self.label_6.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 390, 581, 31))
        self.label_7.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 420, 131, 31))
        self.label_8.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 480, 251, 31))
        self.label_9.setStyleSheet("font: 14pt \"MV Boli\";")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchaboutg)
        self.pushButton.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**our goal**"))
        self.label_3.setText(_translate("Dialog", "1-monetization."))
        self.label_4.setText(_translate("Dialog", "2-people who have a new profession can sell their products here"))
        self.label_5.setText(_translate("Dialog", "and start their business here.we support startups."))
        self.label_6.setText(_translate("Dialog", "3-we receive a small commission to support the internal sales."))
        self.label_7.setText(_translate("Dialog", "4-one of our most important goals is to buy and sell goods"))
        self.label_8.setText(_translate("Dialog", "easily online."))
        self.label_9.setText(_translate("Dialog", "5-Any abuse is prosecuted."))
        self.pushButton.setText(_translate("Dialog", "back"))



    def switchaboutg(self):
        self.boutg = QtWidgets.QDialog()
        self.ui = Uabout_us()
        self.ui.setupUi(self.boutg)
        self.boutg.show()
        self.dialog.close()


#daste bande mahsolat
class grouping(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -20, 631, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.switchdigital)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 151, 91))
        self.pushButton.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.clicked.connect(self.switchclothing)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 240, 151, 91))
        self.pushButton_2.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.switchcosmetics)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 240, 151, 91))
        self.pushButton_3.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.clicked.connect(self.switchstationery)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 240, 151, 91))
        self.pushButton_4.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.clicked.connect(self.switchsupermarket)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 390, 151, 91))
        self.pushButton_6.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.clicked.connect(self.switchtoy)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 390, 151, 91))
        self.pushButton_7.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.clicked.connect(self.switchsport)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 390, 151, 91))
        self.pushButton_5.setStyleSheet("border-radius:35px 30px 200px 0px;\n"
"background-color:rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border:1px solid yellow;\n"
"font: 16pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.clicked.connect(self.switchsfhego)
        self.pushButton_8.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_8.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**grouping**"))
        self.pushButton.setText(_translate("Dialog", "digital"))
        self.pushButton_2.setText(_translate("Dialog", "clothing"))
        self.pushButton_3.setText(_translate("Dialog", "cosmetics"))
        self.pushButton_4.setText(_translate("Dialog", "stationery"))
        self.pushButton_6.setText(_translate("Dialog", "supermarket "))
        self.pushButton_7.setText(_translate("Dialog", "toy"))
        self.pushButton_5.setText(_translate("Dialog", "sports"))
        self.pushButton_8.setText(_translate("Dialog", "back"))



    def switchdigital(self):
        self.digit = QtWidgets.QDialog()
        self.ui = digital()
        self.ui.setupUi(self.digit)
        self.digit.show()
        self.dialog.close()

    def switchclothing(self):
        self.clo = QtWidgets.QDialog()
        self.ui = clothing()
        self.ui.setupUi(self.clo)
        self.clo.show()
        self.dialog.close()

    def switchcosmetics(self):
       self.cas = QtWidgets.QDialog()
       self.ui = cosmetics()
       self.ui.setupUi(self.cas)
       self.cas.show()
       self.dialog.close()

    def switchstationery(self):
        self.sta = QtWidgets.QDialog()
        self.ui = stationery()
        self.ui.setupUi(self.sta)
        self.sta.show()
        self.dialog.close()

    def switchsport(self):
        self.spo = QtWidgets.QDialog()
        self.ui = sport()
        self.ui.setupUi(self.spo)
        self.spo.show()
        self.dialog.close()

    def switchsupermarket(self):
        self.sup = QtWidgets.QDialog()
        self.ui = supermarket()
        self.ui.setupUi(self.sup)
        self.sup.show()
        self.dialog.close()

    def switchtoy(self):
         self.toy = QtWidgets.QDialog()
         self.ui = toy()
         self.ui.setupUi(self.toy)
         self.toy.show()
         self.dialog.close()

    def switchsfhego(self):
        self.goro = QtWidgets.QDialog()
        self.ui = safhe_vorod()
        self.ui.setupUi(self.goro)
        self.goro.show()
        self.dialog.close()

#safhe mahsolat digital
class digital(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 590)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 621, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 141, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 160, 161, 71))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Bol\";i")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 160, 161, 71))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Bol\";i")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 280, 161, 71))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Bol\";i")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 160, 161, 71))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Bol\";i")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 280, 161, 71))
        self.pushButton_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Bol\";i")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 400, 161, 71))
        self.pushButton_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Bol\";i")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 280, 161, 71))
        self.pushButton_7.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Bol\";i")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 400, 161, 71))
        self.pushButton_8.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Bol\";i")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(390, 400, 161, 71))
        self.pushButton_9.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Bol\";i")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.clicked.connect(self.switchgrouping)
        self.pushButton_10.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_10.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**digital**"))
        self.pushButton.setText(_translate("Dialog", "tv"))
        self.pushButton_2.setText(_translate("Dialog", "camera"))
        self.pushButton_3.setText(_translate("Dialog", "air conditioner"))
        self.pushButton_4.setText(_translate("Dialog", "smart phone"))
        self.pushButton_5.setText(_translate("Dialog", "digital accessories"))
        self.pushButton_6.setText(_translate("Dialog", "printer"))
        self.pushButton_7.setText(_translate("Dialog", "laptop"))
        self.pushButton_8.setText(_translate("Dialog", "speaker"))
        self.pushButton_9.setText(_translate("Dialog", "smart watch"))
        self.pushButton_10.setText(_translate("Dialog", "back"))




    def switchgrouping(self):
        self.grop = QtWidgets.QDialog()
        self.ui = grouping()
        self.ui.setupUi(self.grop)
        self.grop.show()
        self.dialog.close()

#safhe mahsolat marbot be poshak
class clothing(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 592)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 631, 631))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 190, 161, 91))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 190, 161, 91))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 190, 151, 91))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 350, 161, 91))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 350, 161, 91))
        self.pushButton_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 350, 151, 91))
        self.pushButton_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.clicked.connect(self.switchgrop)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_7.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.dialog= Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**clothing**"))
        self.pushButton.setText(_translate("Dialog", "women"))
        self.pushButton_2.setText(_translate("Dialog", "men"))
        self.pushButton_3.setText(_translate("Dialog", "children"))
        self.pushButton_4.setText(_translate("Dialog", "bags and shoes"))
        self.pushButton_5.setText(_translate("Dialog", "accessory"))
        self.pushButton_6.setText(_translate("Dialog", "baby seismic"))
        self.pushButton_7.setText(_translate("Dialog", "back"))

    def switchgrop(self):
        self.fol = QtWidgets.QDialog()
        self.ui = grouping()
        self.ui.setupUi(self.fol)
        self.fol.show()
        self.dialog.close()


#safhe mahsolat marbot be lavazem arayesh
class cosmetics(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 631, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 191, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 210, 161, 81))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 210, 171, 81))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 350, 161, 81))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 350, 171, 81))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 210, 161, 81))
        self.pushButton_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 350, 161, 81))
        self.pushButton_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.clicked.connect(self.switchggrop)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_7.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**cosmetics**"))
        self.pushButton.setText(_translate("Dialog", "skin care "))
        self.pushButton_2.setText(_translate("Dialog", "hair care"))
        self.pushButton_3.setText(_translate("Dialog", "perfume"))
        self.pushButton_4.setText(_translate("Dialog", "personal electrical "))
        self.pushButton_5.setText(_translate("Dialog", "make up"))
        self.pushButton_6.setText(_translate("Dialog", "health products"))
        self.pushButton_7.setText(_translate("Dialog", "back"))


    def switchggrop(self):
        self.see = QtWidgets.QDialog()
        self.ui = grouping()
        self.ui.setupUi(self.see)
        self.see.show()
        self.dialog.close()



#safhe mahsolat marbot be lavazem tahrir
class stationery(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 591)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 631, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 221, 51))
        self.label_2.setStyleSheet("font: 26pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 161, 81))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 330, 161, 81))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 180, 161, 81))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 330, 161, 81))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 180, 161, 81))
        self.pushButton_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 330, 161, 81))
        self.pushButton_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.clicked.connect(self.switchgg)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_7.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**stationery**"))
        self.pushButton.setText(_translate("Dialog", "book"))
        self.pushButton_2.setText(_translate("Dialog", "carpet"))
        self.pushButton_3.setText(_translate("Dialog", "handicrafts"))
        self.pushButton_4.setText(_translate("Dialog", "movies and software"))
        self.pushButton_5.setText(_translate("Dialog", "stationery"))
        self.pushButton_6.setText(_translate("Dialog", "musical instruments"))
        self.pushButton_7.setText(_translate("Dialog", "back"))

    def switchgg(self):
        self.ool = QtWidgets.QDialog()
        self.ui = grouping()
        self.ui.setupUi(self.ool)
        self.ool.show()
        self.dialog.close()


#safhe marbot be lavazem varzeshi
class sport(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 588)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 631, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 161, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 220, 201, 81))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 220, 201, 81))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 350, 201, 81))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 350, 201, 81))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 12pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.clicked.connect(self.switchgop)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**sports**"))
        self.pushButton.setText(_translate("Dialog", "travel equipment"))
        self.pushButton_2.setText(_translate("Dialog", "sportswear"))
        self.pushButton_3.setText(_translate("Dialog", "sports products"))
        self.pushButton_4.setText(_translate("Dialog", "bicycles and accessories"))
        self.pushButton_5.setText(_translate("Dialog", "back"))

    def switchgop(self):
        self.gop = QtWidgets.QDialog()
        self.ui = grouping()
        self.ui.setupUi(self.gop)
        self.gop.show()
        self.dialog.close()


#safhe marbot be lavazem sopermarketi
class supermarket(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 587)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 611, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 241, 51))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 220, 141, 71))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 220, 151, 71))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 370, 141, 71))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 370, 141, 71))
        self.pushButton_4.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 220, 151, 71))
        self.pushButton_5.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 370, 141, 71))
        self.pushButton_6.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.clicked.connect(self.switchgot)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_7.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**supermarket**"))
        self.pushButton.setText(_translate("Dialog", "sweetmeat"))
        self.pushButton_2.setText(_translate("Dialog", "dairy products"))
        self.pushButton_3.setText(_translate("Dialog", "junk food"))
        self.pushButton_4.setText(_translate("Dialog", "finger food"))
        self.pushButton_5.setText(_translate("Dialog", "dried fruits"))
        self.pushButton_6.setText(_translate("Dialog", "PushButton"))
        self.pushButton_7.setText(_translate("Dialog", "back"))

    def switchgot(self):
        self.got = QtWidgets.QDialog()
        self.ui = grouping()
        self.ui.setupUi(self.got)
        self.got.show()
        self.dialog.close()


#safhe marbot be mahsolat asbab bazi
class toy(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 586)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, -10, 631, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PicsArt_06-27-10.31.47.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 111, 41))
        self.label_2.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 250, 181, 101))
        self.pushButton.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 250, 181, 101))
        self.pushButton_2.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
"background-color: rgb(255, 239, 6);\n"
"border-color:rgb(255, 239, 6);\n"
"border: 1px solid yellow;\n"
"font: 14pt \"MV Boli\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.clicked.connect(self.switchgoy)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 540, 121, 41))
        self.pushButton_3.setStyleSheet("border-radius: 25px 20px 100px 0px;\n"
                                      "background-color: rgb(255, 239, 6);\n"
                                      "border-color:rgb(255, 239, 6);\n"
                                      "border: 1px solid yellow;\n"
                                      "font: 14pt \"MV Boli\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.dialog = Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "**toy**"))
        self.pushButton.setText(_translate("Dialog", "mind games"))
        self.pushButton_2.setText(_translate("Dialog", "entertainment"))
        self.pushButton_3.setText(_translate("Dialog", "back"))


    def switchgoy(self):
        self.goy = QtWidgets.QDialog()
        self.ui = grouping()
        self.ui.setupUi(self.goy)
        self.goy.show()
        self.dialog.close()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogf = QtWidgets.QDialog()
    ui = safhe_vorod()
    ui.setupUi(dialogf)
    dialogf.show()
    sys.exit(app.exec_())
