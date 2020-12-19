from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    from PyQt5.QtWidgets import QLineEdit
    from PyQt5.QtGui import QIcon
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-176, -81, 1111, 701))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 20pt \"Algerian\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 352, 41))
        self.label_2.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 0, 4);\n"
"font: 14pt \"Algerian\";")
        self.label_2.setObjectName("label_2")
        #self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser = QtWidgets.QLineEdit(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 140, 256, 61))
        self.textBrowser.setPlaceholderText("Enter the temperature here")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(440, 140, 256, 61))
        self.textBrowser_2.setPlaceholderText("The converted temperature is")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(70, 250, 120, 50))
        self.textBrowser_3.setPlaceholderText("Enter the unit")
        self.textBrowser_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(480, 250, 120, 50))
        self.textBrowser_4.setPlaceholderText("Enter the unit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 135, 151, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("arrow.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 240, 180, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: transparent;\n"
"font: 20pt \"Algerian\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.icon=QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("download.jpeg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(self.icon)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Temperature Converter"))
        self.label.setText(_translate("MainWindow", "TextLab"))
        self.label_2.setText(_translate("MainWindow", "TEMPERATURE CONVERTER"))
        self.pushButton.setText(_translate("MainWindow", "CONVERT"))
        self.pushButton.clicked.connect(self.choice)
    
    def clicked(self):
        self.temp=self.textBrowser.text()
        self.u1=self.textBrowser_3.text()
        self.u2=self.textBrowser_4.text()
    
    def one(self,temp):
        self.temp=float(self.temp)
        self.F=((9*self.temp)/5)+32
        return self.F
    def two(self,temp):
        self.temp=float(self.temp)
        self.K=self.temp+273.15
        return self.K
    def three(self,temp):
        self.temp=float(self.temp)
        self.C=5*((self.temp-32)/9)
        return self.C
    def four(self,temp):
        self.temp=float(self.temp)
        self.C=5*((self.temp-32)/9)
        self.K=self.C+273.15
        return self.K
    def five(self,temp):
        self.temp=float(self.temp)
        self.C=self.temp-273.15
        return self.C
    def six(self,temp):
        self.temp=float(self.temp)
        self.C=self.temp-273.15
        self.F=((9*self.C)/5)+32
        return self.F
    def choice(self):
        self.clicked()
        if self.u1=="C" and self.u2=="F":
            self.F=self.one(float(self.temp))
            ans=self.F
        elif self.u1=="C" and self.u2=="K":
            self.K=self.two(float(self.temp))
            ans=self.K
        elif self.u1=="F" and self.u2=="C":
            self.C=self.three(float(self.temp))
            ans=self.C
        elif self.u1=="F" and self.u2=="K":
            self.K=self.four(float(self.temp))
            ans=self.K
        elif self.u1=="K" and self.u2=="C":
            self.C=self.five(float(self.temp))
            ans=self.C
        elif self.u1=="K" and self.u2=="F":
            self.F=self.six(float(self.temp))
            ans=self.F
        ans=str(ans)
        self.textBrowser_2.setText(ans)


        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
