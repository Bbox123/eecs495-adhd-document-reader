# Form implementation generated from reading ui file 'designerUIFiles/popups/configureDocumentPopUp.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, adhdReader: QtWidgets.QMainWindow, readingScreen):
        super().__init__()
        self.readingScreen = readingScreen
        self.adhdReader = adhdReader
        self.setupUi()

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.centerPopUp()
    
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(700, 450)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("""
                                 QMainWindow {
                                        background-color: none;
                                        color: none;   
                                 }
                                 
                                 """)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("""
                                 QMainWindow {
                                        background-color: transparent;
                                        border-style: none;
                                        color: transparent;   
                                 }
                                 
                                 """)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.popUpFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.popUpFrame.setStyleSheet("background-color: rgb(249, 244, 239);\n"
"border-radius: 25px;")
        self.popUpFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.popUpFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.popUpFrame.setObjectName("popUpFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.popUpFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.layoutHolder_2 = QtWidgets.QHBoxLayout()
        self.layoutHolder_2.setContentsMargins(0, 0, 0, 0)
        self.layoutHolder_2.setObjectName("layoutHolder_2")
        self.iconLayout_2 = QtWidgets.QVBoxLayout()
        self.iconLayout_2.setContentsMargins(0, 2, 0, 0)
        self.iconLayout_2.setSpacing(6)
        self.iconLayout_2.setObjectName("iconLayout_2")
        self.configDocIcon_2 = QtWidgets.QLabel(parent=self.popUpFrame)
        self.configDocIcon_2.setText("")
        self.configDocIcon_2.setPixmap(QtGui.QPixmap("UI/icons/doc.png"))
        self.configDocIcon_2.setObjectName("configDocIcon_2")
        self.iconLayout_2.addWidget(self.configDocIcon_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.iconLayout_2.addItem(spacerItem)
        self.layoutHolder_2.addLayout(self.iconLayout_2)
        self.mainLayout_2 = QtWidgets.QVBoxLayout()
        self.mainLayout_2.setSpacing(15)
        self.mainLayout_2.setObjectName("mainLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.mainLayout_2.addItem(spacerItem1)
        self.title_2 = QtWidgets.QLabel(parent=self.popUpFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_2.sizePolicy().hasHeightForWidth())
        self.title_2.setSizePolicy(sizePolicy)
        self.title_2.setStyleSheet("color: #000;\n"
"font-family: Niramit;\n"
"font-size: 35px;\n"
"font-style: italic;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.title_2.setObjectName("title_2")
        self.mainLayout_2.addWidget(self.title_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.subtitle_2 = QtWidgets.QLabel(parent=self.popUpFrame)
        self.subtitle_2.setStyleSheet("color: #000;\n"
"font-family: Roboto;\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.subtitle_2.setWordWrap(True)
        self.subtitle_2.setObjectName("subtitle_2")
        self.mainLayout_2.addWidget(self.subtitle_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.continueButton_2 = QtWidgets.QPushButton(parent=self.popUpFrame, clicked = lambda: self.returnToMainMenu())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continueButton_2.sizePolicy().hasHeightForWidth())
        self.continueButton_2.setSizePolicy(sizePolicy)
        self.continueButton_2.setMinimumSize(QtCore.QSize(160, 75))
        self.continueButton_2.setStyleSheet("QPushButton {\n"
"    color: #FCFFED;\n"
"    font-family: Roboto;\n"
"    font-size: 28px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"    background-color: rgb(78, 134, 150);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"}")
        self.continueButton_2.setObjectName("continueButton_2")
        self.mainLayout_2.addWidget(self.continueButton_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.resumeReadingButton_2 = QtWidgets.QPushButton(parent=self.popUpFrame, clicked = lambda: self.readingScreen.togglePopUp(self))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resumeReadingButton_2.sizePolicy().hasHeightForWidth())
        self.resumeReadingButton_2.setSizePolicy(sizePolicy)
        self.resumeReadingButton_2.setMinimumSize(QtCore.QSize(240, 30))
        self.resumeReadingButton_2.setStyleSheet("QPushButton {\n"
"    color: #4E8696;\n"
"    font-family: Roboto;\n"
"    font-size: 24px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"    text-decoration: underline;\n"
"    background-color: transparent;\n"
"}")
        self.resumeReadingButton_2.setObjectName("resumeReadingButton_2")
        self.mainLayout_2.addWidget(self.resumeReadingButton_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.mainLayout_2.addItem(spacerItem2)
        self.layoutHolder_2.addLayout(self.mainLayout_2)
        self.closeButtonLayout_2 = QtWidgets.QVBoxLayout()
        self.closeButtonLayout_2.setContentsMargins(-1, 2, 2, -1)
        self.closeButtonLayout_2.setSpacing(10)
        self.closeButtonLayout_2.setObjectName("closeButtonLayout_2")
        self.closeButton_2 = QtWidgets.QToolButton(parent=self.popUpFrame, clicked = lambda: self.readingScreen.togglePopUp(self))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/icons/icons8-close-48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.closeButton_2.setIcon(icon)
        self.closeButton_2.setIconSize(QtCore.QSize(20, 20))
        self.closeButton_2.setObjectName("closeButton_2")
        self.closeButtonLayout_2.addWidget(self.closeButton_2, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.closeButtonLayout_2.addItem(spacerItem3)
        self.layoutHolder_2.addLayout(self.closeButtonLayout_2)
        self.layoutHolder_2.setStretch(0, 1)
        self.layoutHolder_2.setStretch(1, 2)
        self.layoutHolder_2.setStretch(2, 1)
        self.gridLayout_2.addLayout(self.layoutHolder_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.popUpFrame, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_2.setText(_translate("MainWindow", "Select new document?"))
        self.subtitle_2.setText(_translate("MainWindow", "The current document information and your progress will be lost."))
        self.continueButton_2.setText(_translate("MainWindow", "Continue"))
        self.resumeReadingButton_2.setText(_translate("MainWindow", "Resume reading..."))
        self.closeButton_2.setText(_translate("MainWindow", "..."))

    def centerPopUp(self):
        """Grab the current size of the screen to center the pop up in the middle"""

        # get current location of screen
        screen_center = self.adhdReader.frameGeometry().center()

        # get pop up data
        widgetWidth = self.frameGeometry().width()
        widgetHeight = self.frameGeometry().height()

        # calculate central position
        center_x = int(screen_center.x() - widgetWidth / 2)
        center_y = int(screen_center.y() - widgetHeight / 2)

        # move the popup to the center
        self.setGeometry(center_x, center_y, widgetWidth, widgetHeight)
        
    def returnToMainMenu(self):
        self.adhdReader.goToMainMenu()
        self.close()
        