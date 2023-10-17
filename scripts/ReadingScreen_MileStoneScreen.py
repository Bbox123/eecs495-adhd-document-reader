# Form implementation generated from reading ui file 'designerUIFiles/ReadingScreen_MileStoneScreen.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import TakeABreakMilestone as tab_m
import ParseFile
import configureDocumentPopUp as config

class Ui_ReadingScreen(QtWidgets.QMainWindow):
    
    def __init__(self, adhdReader: QtWidgets.QMainWindow, parser: ParseFile.Partition_Text):
        """Initialize the reading screen. Pass in a pointer to the screen controller (adhdReader) and a parser object"""
        super(Ui_ReadingScreen, self).__init__()
        self.adhdReader = adhdReader
        self.parser = parser
        self.muted = True

        # partitioning text in parser
        self.parser.partition_text()

        # Create config doc pop up
        self.instantiateConfigDocPopUp()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1124, 749)
        self.setStyleSheet("background-color: rgb(252, 255, 237);")
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(50, 50, 50, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("border: 10px solid #324143;\n"
"background: #FFF;\n"
"padding: -10 px;")
        
        """
        This segment of code is crucial since this is how the text box widget is added.
        We can use this to remove the text box and add the milestone widget.
        """
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.frame)
        self.textBrowser.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFontPointSize(24)
        self.textBrowser.setText(self.parser.get_next(self.loadMileStone, self.loadTextBrowser))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        
        """End of important things to pay attention to."""
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Settings = QtWidgets.QToolButton(parent=self.centralwidget)
        self.Settings.setStyleSheet("QToolButton {\n"
"    border: none;    \n"
"}\n"
"\n"
"QToolButton::hover {\n"
"    background-color: rgb(191, 188, 172);\n"
"}\n"
"\n"
"")
        self.Settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Settings.setIcon(icon)
        self.Settings.setIconSize(QtCore.QSize(50, 50))
        self.Settings.setObjectName("Settings")
        self.verticalLayout_4.addWidget(self.Settings)
        self.configDoc = QtWidgets.QToolButton(parent=self.centralwidget, clicked = lambda: self.toggleConfigDocPopUp())
        self.configDoc.setStyleSheet("QToolButton {\n"
"    border: none;    \n"
"}\n"
"\n"
"QToolButton::hover {\n"
"    background-color: rgb(191, 188, 172);\n"
"}\n"
"\n"
"")
        self.configDoc.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/icons/doc.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.configDoc.setIcon(icon1)
        self.configDoc.setIconSize(QtCore.QSize(50, 50))
        self.configDoc.setObjectName("configDoc")
        self.verticalLayout_4.addWidget(self.configDoc)
        self.textToSpeech = QtWidgets.QToolButton(parent=self.centralwidget)
        self.textToSpeech.setStyleSheet("QToolButton {\n"
"    border: none;    \n"
"}\n"
"\n"
"QToolButton::hover {\n"
"    background-color: rgb(191, 188, 172);\n"
"}\n"
"")
        self.textToSpeech.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI/icons/audio.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.textToSpeech.setIcon(icon2)
        self.textToSpeech.setIconSize(QtCore.QSize(50, 50))
        self.textToSpeech.setObjectName("textToSpeech")
        self.verticalLayout_4.addWidget(self.textToSpeech)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftArrow = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.loadLastPartition())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftArrow.sizePolicy().hasHeightForWidth())
        self.leftArrow.setSizePolicy(sizePolicy)
        self.leftArrow.setStyleSheet("QPushButton {\n"
"    border: none;    \n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(191, 188, 172);\n"
"}\n"
"\n"
"\n"
"")
        self.leftArrow.setText("")
        self.leftEnabled = QtGui.QIcon()
        self.leftEnabled.addPixmap(QtGui.QPixmap("UI/icons/leftArrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.leftDisabled = QtGui.QIcon()
        self.leftDisabled.addPixmap(QtGui.QPixmap("UI/icons/leftArrowGrayed.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.leftArrow.setIcon(self.leftDisabled)
        self.leftArrow.setIconSize(QtCore.QSize(150, 100))
        self.leftArrow.setObjectName("leftArrow")
        self.horizontalLayout_2.addWidget(self.leftArrow)
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setStyleSheet("  QProgressBar {\n"
"        border: 2px solid #C8E3E8;\n"
"        background-color: #C8E3E8;\n"
"        color: black;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #4E8696;\n"
"    }")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setMaximum(self.parser.partition_size)
        self.progressBar.setValue(1)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.rightArrow = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.loadNextPartition())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightArrow.sizePolicy().hasHeightForWidth())
        self.rightArrow.setSizePolicy(sizePolicy)
        self.rightArrow.setStyleSheet("QPushButton {\n"
"    border: none;    \n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(191, 188, 172);\n"
"}")
        self.rightArrow.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("UI/icons/rightArrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rightArrow.setIcon(icon4)
        self.rightArrow.setIconSize(QtCore.QSize(150, 100))
        self.rightArrow.setObjectName("rightArrow")
        self.horizontalLayout_2.addWidget(self.rightArrow)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def loadNextPartition(self):
        """Get the next partition or milestone"""
        self.textBrowser.setText(self.parser.get_next(self.loadMileStone, self.loadTextBrowser))
        self.progressBar.setValue(self.parser.current_partition)
        if self.parser.current_partition > 1:
            self.leftArrow.setIcon(self.leftEnabled)

    def loadLastPartition(self):
        """Get the next partition or milestone"""
        if self.parser.current_partition > 2:
            self.textBrowser.setText(self.parser.get_last(self.loadTextBrowser) )
            self.progressBar.setValue(self.parser.current_partition)
        elif self.parser.current_partition == 2:
            self.leftArrow.setIcon(self.leftDisabled)
            self.textBrowser.setText(self.parser.get_last(self.loadTextBrowser))
            self.progressBar.setValue(self.parser.current_partition)
        
    def loadMileStone(self):
        """hardcoded to take a break milestone for now"""
        takeBreakMilestone = QtWidgets.QWidget()
        ui = tab_m.Ui_takeBreakMilestone()
        ui.setupUi(takeBreakMilestone, self.gridLayout)
        self.textBrowser.hide()
        self.gridLayout.update()

    def loadTextBrowser(self):
        """Check to see if text browser needs to be shown. Hide all other widgets in our grid except for our text browser"""
        if self.textBrowser.isHidden() is not True:
            return

        # Iterate through everything in the grid layout
        for index in range(self.gridLayout.count()):
            self.gridLayout.itemAt(index).widget().hide()
        
        self.textBrowser.show()
        self.gridLayout.update()

    def toggleConfigDocPopUp(self):
        if self.configPopUp.isVisible():
            self.configPopUp.hide()
        else:
            self.configPopUp.show()
    
    def instantiateConfigDocPopUp(self):
        self.configPopUp = QtWidgets.QMainWindow()
        ui = config.Ui_MainWindow()
        ui.setupUi(self.configPopUp)
        self.configPopUp.hide() 

            
    def toggleTTS(self):
        """Toggle text to speech"""
        if self.muted:
            self.muted = False
            print("Unmuted")
        else:
            self.muted = True
            print("Muted")
