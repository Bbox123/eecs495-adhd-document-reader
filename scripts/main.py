import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import MainWindow as mw
import ReadingScreen as rs


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    MainWindow = QtWidgets.QMainWindow()
    ui = mw.Ui_MainWindow()
    ui.setupUi(MainWindow, widget)

    widget.addWidget(MainWindow)
    widget.setWindowTitle("ADHD Reader")
    widget.setFixedWidth(1500)
    widget.setFixedHeight(900)
    
    widget.show()
    sys.exit(app.exec_())