# Form implementation generated from reading ui file 'designerUIFiles/TakeABreakMilestone.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_takeBreakMilestone(object):
    def setupUi(self, takeBreakMilestone):
        takeBreakMilestone.setObjectName("takeBreakMilestone")
        takeBreakMilestone.resize(1221, 749)
        takeBreakMilestone.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(takeBreakMilestone)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 20, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fireworks1 = QtWidgets.QLabel(parent=takeBreakMilestone)
        self.fireworks1.setText("")
        self.fireworks1.setPixmap(QtGui.QPixmap("UI/icons/fireworks1.png"))
        self.fireworks1.setObjectName("fireworks1")
        self.fireworks1.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.verticalLayout.addWidget(self.fireworks1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.mainUI = QtWidgets.QVBoxLayout()
        self.mainUI.setContentsMargins(-1, 50, -1, 20)
        self.mainUI.setObjectName("mainUI")
        self.title = QtWidgets.QLabel(parent=takeBreakMilestone)
        self.title.setStyleSheet("color: #4E8696;\n"
                                "font-family: Inter;\n"
                                "font-size: 40px;\n"
                                "font-style: normal;\n"
                                "font-weight: 600;\n"
                                "line-height: normal;\n"
                                "border-color: rgb(255, 255, 255);"
                                )
        self.title.setObjectName("title")
        self.mainUI.addWidget(self.title, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.startTimer = QtWidgets.QPushButton(parent=takeBreakMilestone)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTimer.sizePolicy().hasHeightForWidth())
        self.startTimer.setSizePolicy(sizePolicy)
        self.startTimer.setMaximumSize(QtCore.QSize(16777215, 100))
        self.startTimer.setStyleSheet("QPushButton {\n"
                                "    border: none;    \n"
                                "    background-color: rgb(78, 134, 150);\n"
                                "    border-radius: 20px;\n"
                                "    color: #FCFFED;\n"
                                "    font-family: Inter;\n"
                                "    font-size: 32px;\n"
                                "    font-style: normal;\n"
                                "    font-weight: 400;\n"
                                "    line-height: normal;\n"
                                "}\n"
                                "\n"
                                "QPushButton::hover {\n"
                                "    background-color: rgb(46, 79, 88);\n"
                                "}")
        self.startTimer.setObjectName("startTimer")
        self.mainUI.addWidget(self.startTimer)
        self.skipButton = QtWidgets.QPushButton(parent=takeBreakMilestone)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.skipButton.setFont(font)
        self.skipButton.setSizePolicy(sizePolicy)
        self.skipButton.setStyleSheet("QPushButton {\n"
"    border: none;    \n"
"    color: #4E8696;\n"
"    font-family: Inter;\n"
"    font-size: 24px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"    text-decoration-line: underline;\n"
"}")
        self.skipButton.setObjectName("skipButton")
        self.mainUI.addWidget(self.skipButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.mainUI.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.mainUI)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fireworks2 = QtWidgets.QLabel(parent=takeBreakMilestone)
        self.fireworks2.setText("")
        self.fireworks2.setPixmap(QtGui.QPixmap("UI/icons//fireworks2.png"))
        self.fireworks2.setObjectName("fireworks2")
        self.fireworks2.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.verticalLayout_3.addWidget(self.fireworks2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(takeBreakMilestone)
        QtCore.QMetaObject.connectSlotsByName(takeBreakMilestone)

    def retranslateUi(self, takeBreakMilestone):
        _translate = QtCore.QCoreApplication.translate
        takeBreakMilestone.setWindowTitle(_translate("takeBreakMilestone", "Form"))
        self.title.setText(_translate("takeBreakMilestone", "Halfway through!"))
        self.startTimer.setText(_translate("takeBreakMilestone", "Take a timed break"))
        self.skipButton.setText(_translate("takeBreakMilestone", "Skip this milestone"))
