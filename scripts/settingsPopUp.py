# Form implementation generated from reading ui file 'designerUIFiles/popups/settingsPopUp.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import settings as settings_backend


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
        self.resize(1000, 650)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("border-radius: 20px;\n"
"border: 3px solid #B6C28B;\n"
"background: #F6F4EF;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 9)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.titleBar = QtWidgets.QHBoxLayout()
        self.titleBar.setContentsMargins(-1, -1, -1, 0)
        self.titleBar.setObjectName("titleBar")
        self.titleLayout = QtWidgets.QFrame(parent=self.frame)
        self.titleLayout.setStyleSheet("background-color: rgb(182, 194, 139);\n"
"border-radius: 10px")
        self.titleLayout.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.titleLayout.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titleLayout.setObjectName("titleLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.titleLayout)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settingsIcon = QtWidgets.QToolButton(parent=self.titleLayout)
        self.settingsIcon.setEnabled(False)
        self.settingsIcon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/icons/gearWhite.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settingsIcon.setIcon(icon)
        self.settingsIcon.setIconSize(QtCore.QSize(64, 64))
        self.settingsIcon.setObjectName("settingsIcon")
        self.horizontalLayout_2.addWidget(self.settingsIcon)
        self.settingsLabel = QtWidgets.QLabel(parent=self.titleLayout)
        self.settingsLabel.setStyleSheet("color: #FFF;\n"
"font-family: Niramit;\n"
"font-size: 48px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.settingsLabel.setObjectName("settingsLabel")
        self.horizontalLayout_2.addWidget(self.settingsLabel)
        self.closeButton = QtWidgets.QToolButton(parent=self.titleLayout, clicked = lambda: self.closeSettings())
        self.closeButton.setStyleSheet("color: #FFF;")
        self.closeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/icons/closeWhite.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.closeButton.setIcon(icon1)
        self.closeButton.setIconSize(QtCore.QSize(50, 50))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.titleBar.addWidget(self.titleLayout)
        self.gridLayout_2.addLayout(self.titleBar, 0, 0, 1, 1)
        self.scrollContainer = QtWidgets.QVBoxLayout()
        self.scrollContainer.setSpacing(0)
        self.scrollContainer.setObjectName("scrollContainer")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.frame)
        self.scrollArea.setStyleSheet("border-color: none;\n"
"border-radius: 0px;\n"
"\n"
"QScrollBar::vertical {\n"
"    width: 15px;\n"
"    background-color: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(182, 194, 139);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;  \n"
"    background-color: none;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background-color: none;\n"
"}\n"
"\n"
"")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -183, 951, 693))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setStyleSheet(" QScrollBar:vertical {\n"
"                width: 15px;\n"
"                background: transparent;\n"
" }")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.settingsOptionText = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsOptionText.sizePolicy().hasHeightForWidth())
        self.settingsOptionText.setSizePolicy(sizePolicy)
        self.settingsOptionText.setStyleSheet("border-bottom: 3px solid #B6C28B;")
        self.settingsOptionText.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.settingsOptionText.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.settingsOptionText.setObjectName("settingsOptionText")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.settingsOptionText)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.settingsTitle = QtWidgets.QLabel(parent=self.settingsOptionText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsTitle.sizePolicy().hasHeightForWidth())
        self.settingsTitle.setSizePolicy(sizePolicy)
        self.settingsTitle.setStyleSheet("font-family: Niramit;\n"
"font-size: 35px;\n"
"font-style: italic;\n"
"font-weight: 600;\n"
"line-height: normal;\n"
"border: none")
        self.settingsTitle.setObjectName("settingsTitle")
        self.verticalLayout_4.addWidget(self.settingsTitle)
        self.sampleText = QtWidgets.QLabel(parent=self.settingsOptionText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampleText.sizePolicy().hasHeightForWidth())
        self.sampleText.setSizePolicy(sizePolicy)
        self.sampleText.setStyleSheet("font-family: Inter;\n"
"font-size: 15px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.sampleText.setObjectName("sampleText")
        self.verticalLayout_4.addWidget(self.sampleText, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.fontSizeLayout = QtWidgets.QHBoxLayout()
        self.fontSizeLayout.setContentsMargins(-1, -1, -1, 0)
        self.fontSizeLayout.setSpacing(15)
        self.fontSizeLayout.setObjectName("fontSizeLayout")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.fontSizeLayout.addItem(spacerItem)
        self.fontSizeLabel = QtWidgets.QLabel(parent=self.settingsOptionText)
        self.fontSizeLabel.setStyleSheet("font-family: Roboto;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.fontSizeLabel.setObjectName("fontSizeLabel")
        self.fontSizeLayout.addWidget(self.fontSizeLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.AaSmall = QtWidgets.QLabel(parent=self.settingsOptionText)
        self.AaSmall.setStyleSheet("font-family: Inter;\n"
"font-size: 15px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.AaSmall.setObjectName("AaSmall")
        self.fontSizeLayout.addWidget(self.AaSmall, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fontSlider = QtWidgets.QSlider(parent=self.settingsOptionText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontSlider.sizePolicy().hasHeightForWidth())
        self.fontSlider.setSizePolicy(sizePolicy)
        self.fontSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.fontSlider.setMinimum(1)
        self.fontSlider.setMaximum(100)
        self.fontSlider.setStyleSheet("QSlider {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background:  rgb(217, 217, 217);\n"
"    margin:8px 0;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: black;\n"
"    margin:8px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(217, 217, 217);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"}")
        self.fontSlider.setProperty("value", 28)
        self.fontSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.fontSlider.setTickInterval(0)
        self.fontSlider.setObjectName("fontSlider")
        self.fontSizeLayout.addWidget(self.fontSlider)
        self.AaBig = QtWidgets.QLabel(parent=self.settingsOptionText)
        self.AaBig.setStyleSheet("font-family: Inter;\n"
"font-size: 60px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.AaBig.setObjectName("AaBig")
        self.fontSizeLayout.addWidget(self.AaBig, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.fontSizeLayout.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.fontSizeLayout)
        self.fontStyleLayout = QtWidgets.QHBoxLayout()
        self.fontStyleLayout.setContentsMargins(-1, -1, -1, 0)
        self.fontStyleLayout.setSpacing(15)
        self.fontStyleLayout.setObjectName("fontStyleLayout")
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.fontStyleLayout.addItem(spacerItem2)
        self.fontStyleLabel = QtWidgets.QLabel(parent=self.settingsOptionText)
        self.fontStyleLabel.setStyleSheet("font-family: Roboto;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.fontStyleLabel.setObjectName("fontStyleLabel")
        self.fontStyleLayout.addWidget(self.fontStyleLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fontStyleDropDown = QtWidgets.QComboBox(parent=self.settingsOptionText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontStyleDropDown.sizePolicy().hasHeightForWidth())
        self.fontStyleDropDown.setSizePolicy(sizePolicy)
        self.fontStyleDropDown.setMinimumSize(QtCore.QSize(300, 0))
        self.fontStyleDropDown.setStyleSheet("QComboBox {\n"
"    border: 2px solid #B6C28B;\n"
"}")
        self.fontStyleDropDown.setObjectName("fontStyleDropDown")
        self.fontStyleLayout.addWidget(self.fontStyleDropDown)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.fontStyleLayout.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.fontStyleLayout)
        self.verticalLayout_3.addWidget(self.settingsOptionText)
        self.settingsOptionPages = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsOptionPages.sizePolicy().hasHeightForWidth())
        self.settingsOptionPages.setSizePolicy(sizePolicy)
        self.settingsOptionPages.setStyleSheet("border-bottom: 3px solid #B6C28B;")
        self.settingsOptionPages.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.settingsOptionPages.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.settingsOptionPages.setObjectName("settingsOptionPages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.settingsOptionPages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.settingsTitle_2 = QtWidgets.QLabel(parent=self.settingsOptionPages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsTitle_2.sizePolicy().hasHeightForWidth())
        self.settingsTitle_2.setSizePolicy(sizePolicy)
        self.settingsTitle_2.setStyleSheet("font-family: Niramit;\n"
"font-size: 35px;\n"
"font-style: italic;\n"
"font-weight: 600;\n"
"line-height: normal;\n"
"border: none")
        self.settingsTitle_2.setObjectName("settingsTitle_2")
        self.verticalLayout_5.addWidget(self.settingsTitle_2)
        self.pageSizeLayout = QtWidgets.QHBoxLayout()
        self.pageSizeLayout.setContentsMargins(-1, -1, -1, 0)
        self.pageSizeLayout.setSpacing(15)
        self.pageSizeLayout.setObjectName("pageSizeLayout")
        spacerItem4 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.pageSizeLayout.addItem(spacerItem4)
        self.pageSizeLabel = QtWidgets.QLabel(parent=self.settingsOptionPages)
        self.pageSizeLabel.setStyleSheet("font-family: Roboto;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.pageSizeLabel.setObjectName("pageSizeLabel")
        self.pageSizeLayout.addWidget(self.pageSizeLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.pageSizeLayout.addItem(spacerItem5)
        self.wordsInput = QtWidgets.QLineEdit(parent=self.settingsOptionPages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordsInput.sizePolicy().hasHeightForWidth())
        self.wordsInput.setSizePolicy(sizePolicy)
        self.wordsInput.setMaximumSize(QtCore.QSize(50, 16777215))
        self.wordsInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #B6C28B;\n"
"}")
        self.wordsInput.setObjectName("wordsInput")
        self.pageSizeLayout.addWidget(self.wordsInput)
        self.wordsInput.textChanged[str].connect(self.changePageSize)
        self.wordsLabel = QtWidgets.QLabel(parent=self.settingsOptionPages)
        self.wordsLabel.setStyleSheet("font-family: Roboto;\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.wordsLabel.setObjectName("wordsLabel")
        self.pageSizeLayout.addWidget(self.wordsLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.pageSizeLayout.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.pageSizeLayout)
        self.verticalLayout_3.addWidget(self.settingsOptionPages)
        self.settingsOptionMilestones = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsOptionMilestones.sizePolicy().hasHeightForWidth())
        self.settingsOptionMilestones.setSizePolicy(sizePolicy)
        self.settingsOptionMilestones.setStyleSheet("border-bottom: 3px solid #B6C28B;")
        self.settingsOptionMilestones.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.settingsOptionMilestones.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.settingsOptionMilestones.setObjectName("settingsOptionMilestones")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.settingsOptionMilestones)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.settingsTitle_3 = QtWidgets.QLabel(parent=self.settingsOptionMilestones)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsTitle_3.sizePolicy().hasHeightForWidth())
        self.settingsTitle_3.setSizePolicy(sizePolicy)
        self.settingsTitle_3.setStyleSheet("font-family: Niramit;\n"
"font-size: 35px;\n"
"font-style: italic;\n"
"font-weight: 600;\n"
"line-height: normal;\n"
"border: none")
        self.settingsTitle_3.setObjectName("settingsTitle_3")
        self.verticalLayout_6.addWidget(self.settingsTitle_3)
        self.frequencyLayout = QtWidgets.QHBoxLayout()
        self.frequencyLayout.setContentsMargins(-1, -1, -1, 0)
        self.frequencyLayout.setSpacing(15)
        self.frequencyLayout.setObjectName("frequencyLayout")
        spacerItem7 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.frequencyLayout.addItem(spacerItem7)
        self.frequencyLabel = QtWidgets.QLabel(parent=self.settingsOptionMilestones)
        
        self.frequencyLabel.setStyleSheet("font-family: Roboto;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.frequencyLabel.setObjectName("frequencyLabel")
        self.frequencyLayout.addWidget(self.frequencyLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.everyLabel = QtWidgets.QLabel(parent=self.settingsOptionMilestones)
        self.everyLabel.setStyleSheet("font-family: Roboto;\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.everyLabel.setObjectName("everyLabel")
        self.frequencyLayout.addWidget(self.everyLabel)
        self.frequencyInput = QtWidgets.QLineEdit(parent=self.settingsOptionMilestones)
        self.frequencyInput.textChanged[str].connect(self.changeMilestoneFrequency)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequencyInput.sizePolicy().hasHeightForWidth())
        self.frequencyInput.setSizePolicy(sizePolicy)
        self.frequencyInput.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #B6C28B;\n"
"}")
        self.frequencyInput.setObjectName("frequencyInput")
        self.frequencyLayout.addWidget(self.frequencyInput)
        self.pagesLabel = QtWidgets.QLabel(parent=self.settingsOptionMilestones)
        self.pagesLabel.setStyleSheet("font-family: Roboto;\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.pagesLabel.setObjectName("pagesLabel")
        self.frequencyLayout.addWidget(self.pagesLabel)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.frequencyLayout.addItem(spacerItem8)
        self.verticalLayout_6.addLayout(self.frequencyLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem9 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.enabledMileStonesLabel = QtWidgets.QLabel(parent=self.settingsOptionMilestones)
        self.enabledMileStonesLabel.setStyleSheet("font-family: Roboto;\n"
"font-size: 32px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;")
        self.enabledMileStonesLabel.setObjectName("enabledMileStonesLabel")
        self.horizontalLayout_8.addWidget(self.enabledMileStonesLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem11 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.checkBoxes = QtWidgets.QVBoxLayout()
        self.checkBoxes.setContentsMargins(-1, -1, 0, 0)
        self.checkBoxes.setObjectName("checkBoxes")
        self.timedBreak = QtWidgets.QCheckBox(parent=self.settingsOptionMilestones)
        self.timedBreak.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.timedBreak.setStyleSheet("font-family: Roboto;\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;\n"
"QCheckBox::checked {\n"
"    background-color: rgb(182, 194, 139);\n"
"}")
        self.timedBreak.setChecked(False)
        self.timedBreak.setObjectName("timedBreak")
        self.checkBoxes.addWidget(self.timedBreak)
        self.cardMatching = QtWidgets.QCheckBox(parent=self.settingsOptionMilestones)
        self.cardMatching.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.cardMatching.setStyleSheet("font-family: Roboto;\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;\n"
"QCheckBox::checked {\n"
"    background-color: rgb(182, 194, 139);\n"
"}")
        self.cardMatching.setObjectName("cardMatching")
        self.checkBoxes.addWidget(self.cardMatching)
#         self.pongMinigame = QtWidgets.QCheckBox(parent=self.settingsOptionMilestones)
#         self.pongMinigame.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
#         self.pongMinigame.setStyleSheet("font-family: Roboto;\n"
# "font-size: 25px;\n"
# "font-style: normal;\n"
# "font-weight: 400;\n"
# "line-height: normal;\n"
# "border: none;\n"
# "QCheckBox::checked {\n"
# "    background-color: rgb(182, 194, 139);\n"
# "}")
#         self.pongMinigame.setObjectName("pongMinigame")
#         self.checkBoxes.addWidget(self.pongMinigame)
        self.readingComp = QtWidgets.QCheckBox(parent=self.settingsOptionMilestones)
        self.readingComp.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.readingComp.setStyleSheet("font-family: Roboto;\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;\n"
"QCheckBox::checked {\n"
"    background-color: rgb(182, 194, 139);\n"
"}")
        self.readingComp.setObjectName("readingComp")
        self.checkBoxes.addWidget(self.readingComp)
        self.rewardAudio = QtWidgets.QCheckBox(parent=self.settingsOptionMilestones)
        self.rewardAudio.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.rewardAudio.setStyleSheet("font-family: Roboto;\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;\n"
"QCheckBox::checked {\n"
"    background-color: rgb(182, 194, 139);\n"
"}")
        self.rewardAudio.setObjectName("rewardAudio")
        self.checkBoxes.addWidget(self.rewardAudio)
        self.horizontalLayout_9.addLayout(self.checkBoxes)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addWidget(self.settingsOptionMilestones)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollContainer.addWidget(self.scrollArea)
        self.gridLayout_2.addLayout(self.scrollContainer, 1, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 9)
        self.verticalLayout_2.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.fontSlider.valueChanged[int].connect(self.changeFontSize)
        self.fontStyleDropDown.currentTextChanged[str].connect(self.changeFontStyle)
        self.setCurrentSettingsUI()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.settingsLabel.setText(_translate("MainWindow", "Settings"))
        self.settingsTitle.setText(_translate("MainWindow", "Text"))
        self.sampleText.setText(_translate("MainWindow", "This is sample text."))
        self.fontSizeLabel.setText(_translate("MainWindow", "Font size:"))
        self.AaSmall.setText(_translate("MainWindow", "Aa"))
        self.AaBig.setText(_translate("MainWindow", "Aa"))
        self.fontStyleLabel.setText(_translate("MainWindow", "Font style:"))
        self.settingsTitle_2.setText(_translate("MainWindow", "Pages"))
        self.pageSizeLabel.setText(_translate("MainWindow", "Page size:"))
        self.wordsLabel.setText(_translate("MainWindow", "words"))
        self.settingsTitle_3.setText(_translate("MainWindow", "Milestones"))
        self.frequencyLabel.setText(_translate("MainWindow", "Frequency:"))
        self.everyLabel.setText(_translate("MainWindow", "Every"))
        self.pagesLabel.setText(_translate("MainWindow", "pages"))
        self.enabledMileStonesLabel.setText(_translate("MainWindow", "Enabled Milestones:"))
        self.timedBreak.setText(_translate("MainWindow", "Timed Break"))
        self.cardMatching.setText(_translate("MainWindow", "Card Matching Minigame"))
        # self.pongMinigame.setText(_translate("MainWindow", "Pong Minigame"))
        self.readingComp.setText(_translate("MainWindow", "Reading Comprehension Questions"))
        self.rewardAudio.setText(_translate("MainWindow", "Reward Audio"))

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

    def changeFontSize(self, value):
        '''Change the font size, also change the sample text.'''
        fontSize = f"{value}px"

        fontStyle = self.fontStyleDropDown.currentText()

        newStyleSheet = ("""
                        font-family: {STYLE};
                        font-size:{SIZE};
                        font-style: normal;
                        font-weight: 400;
                        line-height: normal;
                        border: none;
                         """)
        
        newStyleSheet = newStyleSheet.replace("{SIZE}", fontSize).replace("{STYLE}", fontStyle)
        self.sampleText.setStyleSheet(newStyleSheet)
        # update settings in settings function
        self.adhdReader.settings.text["size"] = value

    def changeFontStyle(self, fontStyle):
        '''Change the font style, also change the sample text.'''
        fontSize = f"{self.fontSlider.value()}px"

        newStyleSheet = ("""
                        font-family: {STYLE};
                        font-size: {SIZE};
                        font-style: normal;
                        font-weight: 400;
                        line-height: normal;
                        border: none;
                         """)
        
        newStyleSheet = newStyleSheet.replace("{SIZE}", fontSize).replace("{STYLE}", fontStyle)
        self.sampleText.setStyleSheet(newStyleSheet)
        self.adhdReader.settings.text["style"] = fontStyle

    def changePageSize(self, size:str):
        if size.isnumeric() and size != "0" and int(size) != self.readingScreen.parser.partition_size:
            self.adhdReader.settings.pages["size"] = int(size)

        elif len(size) != 0:
            self.wordsInput.setText(str(self.adhdReader.settings.pages["size"]))

    def changeMilestoneFrequency(self, frequency:str):
        if frequency.isnumeric() and frequency != "0" and int(frequency) < len(self.readingScreen.parser.partitions):
            self.adhdReader.settings.Milestones["frequency"] = int(frequency)

        elif len(frequency) != 0:
            self.frequencyInput.setText(str(self.adhdReader.settings.Milestones["frequency"]))

    # Replace with values from settings object
    def setCurrentSettingsUI(self):
        '''Set Settings PopUp to reflect default settings upon initial load'''

        # Grab settings ref
        settings:settings_backend.Settings = self.adhdReader.settings

        # Text
        self.font_db = QtGui.QFontDatabase
        # The current font we use
        self.fontStyleDropDown.addItem(settings.text["style"])
        # We can add custom ones that are for individuals with dyslexia by manually adding them to this project and implementing here
        self.fontStyleDropDown.addItems(self.font_db.families())

        self.fontSlider.setValue(settings.text["size"])

        # Pages
        self.wordsInput.setText(str(settings.pages["size"]))

        # Milestones
        self.frequencyInput.setText(str(settings.Milestones["frequency"]))

        check_boxes = self.grabMilestoneCheckBoxes()

        for key, value in check_boxes.items():
            value.setChecked(settings.Milestones["enabled"][key])

    def grabMilestoneCheckBoxes(self):
        boxes = {
             "Timed Break" : self.timedBreak,
             "Card Matching Minigame" : self.cardMatching,
        #      "Pong Minigame" : self.pongMinigame,
             "Reading Comprehension Questions" : self.readingComp,
             "Reward Audio" : self.rewardAudio
        }

        return boxes
    
    def closeSettings(self):
        '''update new reading screen settings and close menu'''
        self.readingScreen.updateReaderToMatchSettings()
        self.readingScreen.togglePopUp(self)
        
        