# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designerUIFiles/MainWindowImproved.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import MainWindowBackEnd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, widget):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        MainWindow.setStyleSheet("background-color: rgb(252, 255, 237);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setObjectName("gridLayout")

        # This frame contains all of the UI layouts and is nested within the main window layout
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet(
                                "background-color: rgb(101, 149, 163);\n"
                                "box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                "border-radius: 20px;\n"
                                "margin: 25%;"
                        )
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setContentsMargins(-1, 0, -1, 0)
        self.vertical_layout.setSpacing(0)
        self.vertical_layout.setObjectName("vertical_layout")
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.setObjectName("header_layout")
        self.headerText = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.headerText.setFont(font)
        self.headerText.setStyleSheet(
                                        "color: white; \n"
                                        "font-size: 40px; \n"
                                        "font-family: Inter; \n"
                                        "font-style: normal;\n"
                                        "font-weight: 400;\n"
                                        "line-height: normal;"
                                )
        self.headerText.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.headerText.setObjectName("headerText")
        self.header_layout.addWidget(self.headerText)
        self.vertical_layout.addLayout(self.header_layout)
        self.input_options_layout = QtWidgets.QHBoxLayout()
        self.input_options_layout.setObjectName("input_options_layout")

        # SpacerItems are used to maintain distance between widgets
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.input_options_layout.addItem(spacerItem)

        # The 'Upload from computer' button
        self.importButton = QtWidgets.QPushButton(self.frame, clicked = lambda: MainWindowBackEnd.importFile(self, widget))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importButton.sizePolicy().hasHeightForWidth())
        self.importButton.setSizePolicy(sizePolicy)
        self.importButton.setMaximumSize(QtCore.QSize(500, 150))
        self.importButton.setStyleSheet(
                                        "background-color: rgb(78, 134, 150);\n"
                                        "box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                        "border-radius: 20px;\n"
                                        "color: white; \n"
                                        "font-size: 32px; \n"
                                        "font-family: Inter; \n"
                                        "font-weight: 300;\n"
                                        "word-wrap: break-word;"
                                )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/icons/downloadButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importButton.setIcon(icon)
        self.importButton.setIconSize(QtCore.QSize(65, 65))
        self.importButton.setObjectName("importButton")
        self.input_options_layout.addWidget(self.importButton)

        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.input_options_layout.addItem(spacerItem1)
        self.dividerLine = QtWidgets.QFrame(self.frame)
        self.dividerLine.setStyleSheet(
                                        "border: 4px #FCFFED solid;\n"
                                        "background-color: rgb(255, 255, 255);"
                                )
        self.dividerLine.setLineWidth(1)
        self.dividerLine.setMidLineWidth(0)
        self.dividerLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.dividerLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dividerLine.setObjectName("dividerLine")
        self.input_options_layout.addWidget(self.dividerLine)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.input_options_layout.addItem(spacerItem2)

        # The plain text edit box
        self.copyPasteInput = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyPasteInput.sizePolicy().hasHeightForWidth())
        self.copyPasteInput.setSizePolicy(sizePolicy)
        self.copyPasteInput.setMinimumSize(QtCore.QSize(0, 0))
        self.copyPasteInput.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.copyPasteInput.setStyleSheet(
                                                "background: #FFF;\n"
                                                "color: rgb(118, 153, 158);\n"
                                                "border-radius: 0px;\n"
                                                "font-family: Inter;\n"
                                                "font-size: 32px;\n"
                                                "font-style: normal;\n"
                                                "font-weight: 300;\n"
                                                "line-height: normal;"
                                        )
        self.copyPasteInput.setPlaceholderText("")
        self.copyPasteInput.setObjectName("copyPasteInput")
        self.input_options_layout.addWidget(self.copyPasteInput)
        self.input_options_layout.setStretch(1, 4)
        self.input_options_layout.setStretch(3, 3)
        self.vertical_layout.addLayout(self.input_options_layout)
        self.submit_layout = QtWidgets.QHBoxLayout()
        self.submit_layout.setObjectName("submit_layout")

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.submit_layout.addItem(spacerItem3)

        # Submit button for the copy paste text box
        self.submitButton = QtWidgets.QPushButton(self.frame, clicked = lambda: MainWindowBackEnd.collectTextFromTextBox(self, self.copyPasteInput.toPlainText(), widget))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setMinimumSize(QtCore.QSize(0, 115))
        self.submitButton.setMaximumSize(QtCore.QSize(260, 200))
        self.submitButton.setStyleSheet(
                                        "border-radius: 20px;\n"
                                        "background: #FCFFED;\n"
                                        "box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);\n"
                                        "color: #324143;\n"
                                        "font-family: Inter;\n"
                                        "font-size: 32px;\n"
                                        "font-style: normal;\n"
                                        "font-weight: 500;\n"
                                        "line-height: normal;"
                                )
        self.submitButton.setObjectName("submitButton")
        self.submit_layout.addWidget(self.submitButton)
        self.vertical_layout.addLayout(self.submit_layout)
        self.gridLayout_3.addLayout(self.vertical_layout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADHD Reader"))
        self.headerText.setText(_translate("MainWindow", "Input a reading to get started:"))
        self.importButton.setText(_translate("MainWindow", "Upload from computer"))
        self.copyPasteInput.setPlainText(_translate("MainWindow", "Paste into text box..."))
        self.submitButton.setText(_translate("MainWindow", "Submit"))

