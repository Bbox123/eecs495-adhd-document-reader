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
        completeMessage = QtWidgets.QLabel()
        completeMessage.setStyleSheet("width: 645px;\n"
"font: 45pt \"Niramit\";\n"
"height: 76px;\n"
"flex-shrink: 0;\n"
"color: #324143;\n"
"font-size: 45px;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"line-height: normal;")
        completeMessage.setObjectName("Completion")
        completeMessage.setText("Reading complete.")
        completeMessage.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.addWidget(completeMessage)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        
        gridLayout.addLayout(verticalLayout, 0, 0, 1, 1)
        self.readingBoxGridLayout.addWidget(self, 0, 1)
        