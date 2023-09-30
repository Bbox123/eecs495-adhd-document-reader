import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import MainWindow as mw
import ReadingScreen as rs


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    MainWindow = QtWidgets.QMainWindow()
    ui = mw.Ui_MainWindow()
    ui.setupUi(MainWindow, widget)

    # might change this later to lower memory costs (have it instantiate when user clicks import/submit instead of right now)
    ReadingScreen = QtWidgets.QMainWindow()
    ui_rs = rs.Ui_ReadingScreen()
    ui_rs.setupUi(ReadingScreen, widget)

    widget.addWidget(MainWindow)
    widget.addWidget(ReadingScreen)
    widget.setWindowTitle("ADHD Reader")
    widget.setFixedWidth(1500)
    widget.setFixedHeight(900)
    
    widget.show()
    sys.exit(app.exec_())