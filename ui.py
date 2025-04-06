from PyQt5 import QtCore, QtWidgets


class Ui_WebBrowserMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("WebBrowserMainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.urlInput = QtWidgets.QLineEdit(self.centralwidget)
        self.urlInput.setGeometry(QtCore.QRect(10, 10, 680, 30))
        self.urlInput.setObjectName("urlInput")

        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(700, 10, 90, 30))
        self.goButton.setObjectName("goButton")

        self.webViewPlaceholder = QtWidgets.QWidget(self.centralwidget)
        self.webViewPlaceholder.setGeometry(QtCore.QRect(10, 50, 780, 540))
        self.webViewPlaceholder.setObjectName("webViewPlaceholder")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtWidgets.QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Простой браузер"))
        self.urlInput.setPlaceholderText(_translate("MainWindow", "Введите URL"))
        self.goButton.setText(_translate("MainWindow", "Перейти"))
