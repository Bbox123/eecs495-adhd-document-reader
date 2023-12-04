import sys
from PyQt6 import QtWidgets
import MainWindow as mw
import ReadingScreen_MileStoneScreen as rs_ms
import configureDocumentPopUp as config
import settings

class ADHDReader(QtWidgets.QMainWindow):
    def __init__(self):
        super(ADHDReader, self).__init__()
        
        self.stacked_widget = QtWidgets.QStackedWidget()

        MainWindow = mw.Ui_MainWindow(self)

        self.settings_backend = settings.Settings()
        self.settings = self.settings_backend.settings

        self.stacked_widget.addWidget(MainWindow)
        self.setCentralWidget(self.stacked_widget)
        self.resize(1600, 1000)
        self.setMinimumSize(775, 950)

    def goToReadingScreen(self, parser):
        """Take the document or text and head to the reading screen to display it!"""
        ui_rs = rs_ms.Ui_ReadingScreen(self, parser)

        self.stacked_widget.addWidget(ui_rs)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.indexOf(ui_rs))

    def goToMainMenu(self):
        """Clean up instantiated widgets and go back to the main menu"""
        MainWindow = mw.Ui_MainWindow(self)
        for index in range(self.stacked_widget.count()):
            widget = self.stacked_widget.widget(index)
            if widget:
                self.stacked_widget.removeWidget(widget)
        
        self.stacked_widget.addWidget(MainWindow)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.indexOf(MainWindow))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    AdhdReader = ADHDReader()
    AdhdReader.show()
    sys.exit(app.exec())