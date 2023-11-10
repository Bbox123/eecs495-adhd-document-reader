from PyQt6 import QtCore, QtGui, QtWidgets
import TakeABreakMilestoneTimer as m_timer
import cardMatchingMilestone as m_cardmatch
import random
import settings

class completion_Screen(QtWidgets.QWidget):
    def __init__(self, readingBoxGridLayout: QtWidgets.QGridLayout, readingScreen):
        super().__init__()
        self.readingScreen = readingScreen
        self.readingBoxGridLayout = readingBoxGridLayout
        self.setupUI()

    def setupUI(self):
        gridLayout = QtWidgets.QGridLayout(parent=self)
        self.setObjectName("completionScreen")
        self.resize(1500, 900)
        # shadow
        self.shadowSubmit = QtWidgets.QGraphicsDropShadowEffect()
        self.shadowSubmit.setBlurRadius(10)
        self.shadowSubmit.setYOffset(5)
        self.shadowSubmit.setXOffset(0)
        self.shadowSubmit.setColor(QtGui.QColor(0, 0, 0, 90))
        # completion message
        completeMessage = QtWidgets.QLabel()
        completeMessage.setStyleSheet("width: 645px;\n"
"font: 45pt \"Niramit\";\n"
"height: 76px;\n"
"flex-shrink: 0;\n"
"color: #324143;\n"
"font-size: 45px;\n"
"font-style: bold;\n"
"font-weight: 500;\n"
"line-height: normal;")
        completeMessage.setObjectName("Completion")
        completeMessage.setText("Reading complete!")
        completeMessage.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        # completion image
        completeImage = QtWidgets.QLabel()
        completeImage.setStyleSheet("width: 645px;\n height: 76px;\n ")
        completeImage.setObjectName("completeImage")
        completeImage.setPixmap(QtGui.QPixmap("UI/icons/boat_landed.png"))
        completeImage.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        horizLayout = QtWidgets.QHBoxLayout()
        restartButton = QtWidgets.QToolButton(parent=self, clicked = lambda: self.restartDocument())
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(restartButton.sizePolicy().hasHeightForWidth())
        # restartButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/icons/read-again.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        restartButton.setStyleSheet("QToolButton {\n"
            "    border: none;    \n"
            "}\n"
            "\n"
            "QToolButton::hover {\n"
            "    background-color: rgb(191, 188, 172);\n"
            "}\n"
            "\n"
            "")
        restartButton.setIconSize(QtCore.QSize(246, 80))
        restartButton.setIcon(icon1)
        horizLayout.addWidget(restartButton)

        # reconfigure document button
        newDocButton = QtWidgets.QPushButton(parent=self.readingScreen, clicked = lambda: self.readingScreen.togglePopUp(self.readingScreen.configPopUp))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newDocButton.sizePolicy().hasHeightForWidth())
        newDocButton.setSizePolicy(sizePolicy)
        newDocButton.setMinimumSize(QtCore.QSize(270, 57))
        newDocButton.setMaximumSize(QtCore.QSize(270, 57))
        newDocButton.setGraphicsEffect(self.shadowSubmit)
        newDocButton.setStyleSheet("""
                                        QPushButton {
                                                border-radius: 20px;
                                                background: #4E8696;
                                                color: white;
                                                font-family: Inter;
                                                font-size: 24px;
                                                font-style: normal;
                                                font-weight: 500;
                                                line-height: normal;
                                        }
                                        QPushButton:hover {
                                                background: rgb(127, 153, 0);
                                        }
                                """)
        newDocButton.setObjectName("newDocButton")
        newDocButton.setText("Select new document")
        horizLayout.addWidget(newDocButton)
        
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.addWidget(completeMessage)
        verticalLayout.addWidget(completeImage)
        verticalLayout.addLayout(horizLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        verticalLayout.addSpacerItem(spacerItem)
        
        gridLayout.addLayout(verticalLayout, 0, 0, 1, 1)
        self.readingBoxGridLayout.addWidget(self, 0, 1)

    def restartDocument(self):
        self.readingScreen.parser.restart_file() 
        self.readingScreen.loadNextPartition()
        

        