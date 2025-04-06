import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from ui import Ui_WebBrowserMainWindow


class WebBrowserMainWindow(QMainWindow, Ui_WebBrowserMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.webView = QWebEngineView(self.centralwidget)
        self.webView.setGeometry(self.webViewPlaceholder.geometry())
        self.webViewPlaceholder.deleteLater()
        self.urlInput.setText("https://www.google.com")
        self.goButton.clicked.connect(self.load_url)
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #fad0c4, stop:1 #ff9a9e);
            }
            QLineEdit, QPushButton {
                font-size: 16px;
            }
        """)
        self.center()
        self.load_url()

    def load_url(self):
        url = self.urlInput.text().strip()
        if not url.startswith("http"):
            url = "http://" + url
        self.webView.load(QUrl(url))

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebBrowserMainWindow()
    window.show()
    sys.exit(app.exec_())
