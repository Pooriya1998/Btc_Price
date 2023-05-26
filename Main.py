from PyQt6 import QtCore, QtWidgets
import Btc_Price
import pyttsx3
import datetime


class Ui_btc_mw(object):

    def __init__(self):
        self.engine = pyttsx3.init()

    def setupUi(self, btc_mw):
        btc_mw.setObjectName("btc_mw")
        btc_mw.resize(560, 200)

        self.centralwidget = QtWidgets.QWidget(parent=btc_mw)
        self.centralwidget.setObjectName("centralwidget")

        self.usd_tb = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.usd_tb.setGeometry(QtCore.QRect(120, 60, 281, 31))
        self.usd_tb.setObjectName("usd_tb")

        self.usd_pb = QtWidgets.QPushButton(parent=self.centralwidget)
        self.usd_pb.setGeometry(QtCore.QRect(420, 60, 111, 31))
        self.usd_pb.setObjectName("usd_pb")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 151, 20))
        self.label.setObjectName("label")

        self.text_browser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.text_browser.setGeometry(QtCore.QRect(30, 110, 501, 31))
        self.text_browser.setObjectName("text_browser")

        self.voice_pb_usd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.voice_pb_usd.setGeometry(QtCore.QRect(30, 60, 81, 31))
        self.voice_pb_usd.setObjectName("voice_pb_usd")

        btc_mw.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=btc_mw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 21))
        self.menubar.setObjectName("menubar")
        btc_mw.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=btc_mw)
        self.statusbar.setObjectName("statusbar")
        btc_mw.setStatusBar(self.statusbar)

        self.retranslateUi(btc_mw)
        self.usd_pb.clicked.connect(self.print_usd_btc)
        self.voice_pb_usd.clicked.connect(self.say_usd_btc)
        QtCore.QMetaObject.connectSlotsByName(btc_mw)

    def print_usd_btc(self):
        btc = Btc_Price.coindesk()
        btc_usd = btc.get_btc_price()
        self.text_browser.clear()
        self.usd_tb.clear()
        self.text_browser.append(str(datetime.datetime.today()))
        self.usd_tb.append("قیمت بیت کوین {} دلار می باشد".format(btc_usd))

    def say_usd_btc(self):
        btc = Btc_Price.coindesk()
        btc_usd = btc.get_btc_price()
        self.text_browser.clear()
        self.text_browser.append(str(datetime.datetime.today()))
        self.engine.say('bitcoin price is {}'.format(btc_usd))
        self.engine.runAndWait()

    def retranslateUi(self, btc_mw):
        _translate = QtCore.QCoreApplication.translate
        btc_mw.setWindowTitle(_translate("btc_mw", "MainWindow"))
        self.usd_pb.setText(_translate("btc_mw", "به دلار"))
        self.label.setText(_translate("btc_mw", "قیمت لحظه ای بیت کوین"))
        self.voice_pb_usd.setText(_translate("btc_mw", "گزارش صوتی"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    btc_mw = QtWidgets.QMainWindow()
    ui = Ui_btc_mw()
    ui.setupUi(btc_mw)
    btc_mw.show()
    sys.exit(app.exec())
