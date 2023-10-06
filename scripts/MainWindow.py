# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designerUIFiles/MainWindowImproved.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import ReadingScreen_MileStoneScreen as rs_ms
import ParseFile as pf

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, adhdReader):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        MainWindow.setStyleSheet("background-color: rgb(252, 255, 237);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # This frame contains all of the UI layouts and is nested within the main window layout
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet(
                                "background-color: rgb(101, 149, 163);\n"
                                "box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                "border-radius: 20px;\n"
                                "margin: 25%;"
                        )
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
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
        self.headerText.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.headerText.setObjectName("headerText")
        self.header_layout.addWidget(self.headerText, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.vertical_layout.addLayout(self.header_layout)
        self.input_options_layout = QtWidgets.QHBoxLayout()
        self.input_options_layout.setObjectName("input_options_layout")

        # SpacerItems are used to maintain distance between widgets
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.input_options_layout.addItem(spacerItem)

        # The 'Upload from computer' button
        self.importButton = QtWidgets.QPushButton(self.frame, clicked = lambda: self.importFile(adhdReader))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importButton.sizePolicy().hasHeightForWidth())
        self.importButton.setSizePolicy(sizePolicy)
        self.importButton.setMaximumSize(QtCore.QSize(500, 150))
        self.importButton.setStyleSheet("""
                                        QPushButton {
                                                background-color: rgb(78, 134, 150);
                                                box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
                                                border-radius: 20px;
                                                color: white;
                                                font-size: 32px;
                                                font-family: Inter;
                                                font-weight: 300;
                                                word-wrap: break-word;
                                        }
                                        
                                        QPushButton:hover { 
                                                background-color: rgb(53, 90, 100);
                                         }
                                """)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/icons/downloadButton.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.importButton.setIcon(icon)
        self.importButton.setIconSize(QtCore.QSize(65, 65))
        self.importButton.setObjectName("importButton")
        self.input_options_layout.addWidget(self.importButton)

        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.input_options_layout.addItem(spacerItem1)
        self.dividerLine = QtWidgets.QFrame(self.frame)
        self.dividerLine.setStyleSheet(
                                        "border: 4px #FCFFED solid;\n"
                                        "background-color: rgb(255, 255, 255);"
                                )
        self.dividerLine.setLineWidth(1)
        self.dividerLine.setMidLineWidth(0)
        self.dividerLine.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.dividerLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dividerLine.setObjectName("dividerLine")
        self.input_options_layout.addWidget(self.dividerLine)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.input_options_layout.addItem(spacerItem2)

        # The plain text edit box
        self.copyPasteInput = QtWidgets.QPlainTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Expanding)
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

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.submit_layout.addItem(spacerItem3)

        # Submit button for the copy paste text box
        self.submitButton = QtWidgets.QPushButton(self.frame, clicked = lambda: self.collectTextFromTextBox(self.copyPasteInput.toPlainText(), adhdReader))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setMinimumSize(QtCore.QSize(0, 115))
        self.submitButton.setMaximumSize(QtCore.QSize(260, 200))
        self.submitButton.setStyleSheet("""
                                        QPushButton {
                                                border-radius: 20px;
                                                background: #FCFFED;
                                                box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
                                                color: #324143;
                                                font-family: Inter;
                                                font-size: 32px;
                                                font-style: normal;
                                                font-weight: 500;
                                                line-height: normal;
                                        }
                                        QPushButton:hover {
                                                background: rgb(127, 153, 0);
                                        }
                                        
                                """)
        self.submitButton.setObjectName("submitButton")
        self.submit_layout.addWidget(self.submitButton)
        self.vertical_layout.addLayout(self.submit_layout)
        self.gridLayout_3.addLayout(self.vertical_layout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.setupTitleBar(adhdReader)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupTitleBar(self, adhdReader):
        self.titleBar = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBar.sizePolicy().hasHeightForWidth())
        self.titleBar.setSizePolicy(sizePolicy)
        self.titleBar.setMinimumSize(QtCore.QSize(0, 64))
        self.titleBar.setStyleSheet("background-color: rgb(50, 65, 67);")
        self.titleBar.setObjectName("titleBar")
        self.header = QtWidgets.QHBoxLayout(self.titleBar)
        self.header.setContentsMargins(0, 0, 0, 0)
        self.header.setObjectName("header")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimizeButton = QtWidgets.QPushButton(parent=self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizeButton.sizePolicy().hasHeightForWidth())
        self.minimizeButton.setSizePolicy(sizePolicy)
        self.minimizeButton.setMinimumSize(QtCore.QSize(30, 20))
        self.minimizeButton.setMaximumSize(QtCore.QSize(35, 35))
        self.minimizeButton.setStyleSheet("""
                                        QPushButton {
                                                border: none;
                                        }
                                        """)
        self.minimizeButton.setText("")
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout_4.addWidget(self.minimizeButton, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop)
        self.maximizeButton = QtWidgets.QPushButton(parent=self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maximizeButton.sizePolicy().hasHeightForWidth())
        self.maximizeButton.setSizePolicy(sizePolicy)
        self.maximizeButton.setMaximumSize(QtCore.QSize(35, 35))
        self.maximizeButton.setStyleSheet("""
                                        QPushButton {
                                                border: none;
                                        }
                                        """)
        self.maximizeButton.setText("")
        self.horizontalLayout_4.addWidget(self.maximizeButton, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        # You have to pass in adhdReader here since that contains all of our screens
        self.closeButton = QtWidgets.QPushButton(parent=self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMaximumSize(QtCore.QSize(35, 35))
        self.closeButton.setStyleSheet("""
                                        QPushButton {
                                                border: none;
                                        }
                                        """)
        self.closeButton.setText("")
        self.horizontalLayout_4.addWidget(self.closeButton, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)
        self.Title = QtWidgets.QLabel(parent=self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setMouseTracking(True)
        self.Title.setStyleSheet("color: #B6C28B;\n"
"font-family: Inter;\n"
"font-size: 40px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title.setObjectName("Title")
        self.gridLayout_2.addWidget(self.Title, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton(parent=self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("""
                                        QPushButton {
                                                border: none;
                                        }
                                        QPushButton:hover {
                                                background: rgb(33, 44, 46);
                                        }
                                        """)
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("UI/icons/book.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.header.addLayout(self.gridLayout_2)
        self.gridLayout.addWidget(self.titleBar, 0, 1, 1, 1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADHD Reader"))
        self.headerText.setText(_translate("MainWindow", "Input a reading to get started:"))
        self.importButton.setText(_translate("MainWindow", "Upload from computer"))
        self.copyPasteInput.setPlainText(_translate("MainWindow", "Paste into text box..."))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.Title.setText(_translate("MainWindow", "ADHD Reader"))

    def collectTextFromTextBox(self, inputText, adhdReader):
        """inputText contains all the text that was placed in the text box before submit was clicked"""
        # If user clicks submit and they haven't added any text, return
        if (len(inputText) == 0 or inputText == "Paste into text box..."):
                return
        
        # Parse the file
        parser = pf.Partition_Text(text=inputText)              # create parser

        # Change to reading screen 
        self.goToReadingScreen(adhdReader, parser)           # pass in parser object

    def importFile(self, adhdReader):
        """Open the file dialog to import a .txt or .pdf"""
        # This method returns a tuple, but the ', _' syntax allows us to just grab the first index of it which has the file path
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
                caption="Import File", 
                directory="",  # Default import directory is the same directory the application is in
                filter="PDF and Text Files (*.txt | *.pdf);;Text Files (*.txt);;PDF (*.pdf)"
        )

        # If the user clicks cancel, return
        if (len(filepath) == 0):
                return

        # Parse the file
        parser = pf.Partition_Text()                            # create parser
        parser.parse_file(filepath.split(".")[-1], filepath)    # parse file

        # Change to reading screen
        self.goToReadingScreen(adhdReader, parser)

    def goToReadingScreen(self, adhdReader, parser):
        ui_rs = rs_ms.Ui_ReadingScreen(adhdReader, parser)
        ui_rs.setupUi()

        adhdReader.stacked_widget.addWidget(ui_rs)
        adhdReader.stacked_widget.setCurrentIndex(1)

