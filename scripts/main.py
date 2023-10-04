import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPainter, QMouseEvent, QCursor
from PyQt6.QtCore import Qt, QPoint
import MainWindow as mw

class ADHDReader(QtWidgets.QMainWindow):
    def __init__(self):
        super(ADHDReader, self).__init__()
        
        self.stacked_widget = QtWidgets.QStackedWidget()

        MainWindow = QtWidgets.QMainWindow()
        ui = mw.Ui_MainWindow()
        ui.setupUi(MainWindow, self)

        self.stacked_widget.addWidget(MainWindow)
        self.setCentralWidget(self.stacked_widget)
        self.resize(1500, 900)

        self.oldPos = self.pos()
    

    def close_application(self):
        self.close()

    def maximize_application(self):
        self.showMaximized()

    def minimize_application(self):
        self.showMinimized()
    
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event: QMouseEvent):
        delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPosition().toPoint()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    AdhdReader = ADHDReader()
    AdhdReader.show()
    sys.exit(app.exec())