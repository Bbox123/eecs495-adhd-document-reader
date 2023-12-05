# Form implementation generated from reading ui file 'designerUIFiles/ReadingScreen_MileStoneScreen.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import genericMilestone as mileStoneScreen
import ParseFile
import configureDocumentPopUp as config
import settingsPopUp as settings
import settings as settings_backend
import TextToSpeech as tts
import completionScreen as complete


class Ui_ReadingScreen(QtWidgets.QMainWindow):
    
    def __init__(self, adhdReader: QtWidgets.QMainWindow, parser: ParseFile.Partition_Text):
        """Initialize the reading screen. Pass in a pointer to the screen controller (adhdReader) and a parser object"""
        super(Ui_ReadingScreen, self).__init__()
        self.adhdReader = adhdReader
        self.parser = parser
        self.muted = True
        self.paused = True
        self.ttsLoaded = False

        # partitioning text in parser
        self.parser.partition_text()

        # Create pop ups
        self.instantiatePopUps()

        # Set default milestone screen
        self.mileStoneScreen = None
        self.milestoneIndex = 0

        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setWindowTitle(self.parser.file_title)
        self.resize(1125, 750)
        self.setStyleSheet("background-color: #FAF8F3;")
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

         # add doc title
        docTitle = QtWidgets.QLabel()
        docTitle.setStyleSheet("background-color: #4E8696; font-style: italic; color: white; text-align: center; font-size: 20px; line-height: 1000px")
        docTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        # docTitle.setFixedSize(1124,50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        docTitle.setMinimumHeight(40)
        docTitle.setSizePolicy(sizePolicy)
        docTitle.setText('Reading: "'+ self.parser.file_title + '\"')
        self.verticalLayout.addWidget(docTitle)
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(50, 50, 50, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setWidthForHeight(False)
        sizePolicy.setHeightForWidth(False)
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(900, 16777215))
        # self.frame.setMinimumSize(QtCore.QSize(900, 1))
        self.frame.setStyleSheet("border: 00px solid #324143;\n"
"background: #FFF;\n"
"padding: -10 px;")
        
        # Manually build our grey screen overlay
        self.overlay = QtWidgets.QFrame(self)
        self.overlay.setStyleSheet("background-color: rgba(151, 151, 151, 210);")
        self.overlay.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.overlay.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.overlay.setGeometry(self.adhdReader.rect())
        self.overlay.hide()
        
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
        self.textBrowser.setStyleSheet(f"border-color: rgb(255, 255, 255);font-size:{self.adhdReader.settings['text']['size']};color: black;padding:30px 40px; line-height: 3; font-weight:lighter", )
        self.textBrowser.setObjectName("textBrowser")
        self.document = QtGui.QTextDocument()
        self.document.setHtml(self.parser.get_next(self.loadMileStone, self.loadTextBrowser))
        self.document.setDefaultFont(QtGui.QFont(self.adhdReader.settings["text"]["style"], int(self.adhdReader.settings["text"]["size"])))
        self.textBrowser.setDocument(self.document)
        self.backgroundFrame = QtWidgets.QFrame(self)
        self.backgroundFrame.setFixedSize(81,50)
        self.backgroundFrame.setStyleSheet("QFrame {border-radius: 25px; \n"
                                               "background-color: rgb(255, 255, 255); \n"
                                               "border: 3px solid rgb(182, 194, 139)}")
        self.backgroundFrame.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect(self.backgroundFrame))
        self.backgroundFrame.setLayout(QtWidgets.QHBoxLayout())
        self.backgroundFrame.layout().setContentsMargins(12,0,12,0)
        self.backgroundFrame.layout().setSpacing(15)
        self.gridLayout.addWidget(self.backgroundFrame, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        
        """End of important things to pay attention to."""
        self.horizontalLayout.addStretch(stretch=1)
        self.horizontalLayout.addWidget(self.frame, stretch=5)
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Settings = QtWidgets.QToolButton(parent=self.centralwidget, clicked = lambda: self.togglePopUp(self.settingsPopUp))
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
        self.Settings.setToolTip("Settings")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Settings.setIcon(icon)
        self.Settings.setIconSize(QtCore.QSize(50, 50))
        self.Settings.setObjectName("Settings")

        self.verticalLayout_4.addWidget(self.Settings, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.configDoc = QtWidgets.QToolButton(parent=self.centralwidget, clicked = lambda: self.togglePopUp(self.configPopUp))
        self.configDoc.setStyleSheet("QToolButton {\n"
"    border: none;    \n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QToolButton::hover {\n"
"    background-color: rgb(191, 188, 172);\n"
"}\n"
"\n"
"")
        self.configDoc.setText("")
        self.configDoc.setToolTip("Change document")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/icons/doc.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.configDoc.setIcon(icon1)
        self.configDoc.setIconSize(QtCore.QSize(70, 70))
        self.configDoc.setObjectName("configDoc")
        self.verticalLayout_4.addWidget(self.configDoc)
        self.textToSpeech = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.toggleTTS())
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI/icons/audio_off.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.textToSpeech.setIcon(icon2)
        self.textToSpeech.setIconSize(QtCore.QSize(44, 44))
        
        self.ttsOffStyle = "QPushButton {\n" \
"    border: none;    \n" \
"    background-color: rgba(255, 255, 255, 0);\n" \
"    border-radius: 11px;\n" \
"}\n" \
"\n" \
"QPushButton::hover {\n" \
"    background-color: rgb(191, 188, 172);\n" \
"}\n" \
""
        self.ttsOnStyle = "QPushButton {\n" \
"    border: none;    \n" \
"    background-color: rgba(255, 255, 255, 0);\n" \
"    border-radius: 11px;\n" \
"}\n" \
"\n" \
"QPushButton::hover {\n" \
"    background-color: rgb(127, 153, 0);\n" \
"}\n" \
""
        self.textToSpeech.setStyleSheet(self.ttsOffStyle)
        self.textToSpeech.setObjectName("textToSpeech")
        self.textToSpeech.setToolTip("Enable text-to-speech")
        self.textToSpeech.setFixedSize(44, 44)
        self.backgroundFrame.layout().addWidget(self.textToSpeech)
        self.textToSpeechLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.textToSpeechLabel.setFixedSize(200,50)
        self.textToSpeechLabel.setObjectName("textToSpeechLabel")
        # Not sure which color to use, (182, 194, 139) would match the other icons, but I think (127, 153, 0) is more readable
        self.textToSpeechLabel.setStyleSheet("font-size: 17px; color: rgb(255, 255, 255); font-weight: 750; font-family: Inter; font-style: italic;")
        # self.textToSpeechLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.textToSpeechLabel.setText("Text-to-speech Enabled")
        self.backgroundFrame.layout().addWidget(self.textToSpeechLabel)
        self.playPause = QtWidgets.QToolButton(parent=self.centralwidget, clicked = lambda: self.playPauseTTS())
        self.playPause.setFixedSize(44, 44)
        self.playPause.setStyleSheet("QToolButton {\n"
"    border: none;    \n"
"    background-color: rgb(182, 194, 139);\n"
"    border-radius: 11px;\n"
"}\n"
"\n"
"QToolButton::hover {\n"
"    background-color: rgb(127, 153, 0);\n"
"}\n"
"\n"
"")
        self.playPause.setText("")
        self.playPause.setToolTip("Play/Pause")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UI/icons/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.playPause.setIcon(icon3)
        self.playPause.setIconSize(QtCore.QSize(44, 44))
        self.playPause.setObjectName("playPause")
        self.backgroundFrame.layout().addWidget(self.playPause)
        self.playPause.hide()
        self.textToSpeechLabel.hide()
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addStretch(stretch=1)
        self.horizontalLayout.addLayout(self.verticalLayout_4, stretch=2)
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
        self.progressBar.setValue(0)
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
        
        self.progressBar.setMaximum(self.parser.get_partitions_list_size())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.updateReaderToMatchSettings()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def loadNextPartition(self):
        """Get the next partition or milestone"""
        # check for if completion screen should instead be loaded
        if self.parser.current_partition == len(self.parser.partitions):
            self.loadCompletion()
            self.progressBar.setValue(self.parser.current_partition)
            self.leftArrow.setIcon(self.leftEnabled)
            self.parser.current_partition += 1
            print("entering completion")
        else:
            self.document.setHtml(self.parser.get_next(self.loadMileStone, self.loadTextBrowser))
            self.textBrowser.setDocument(self.document)
            self.progressBar.setValue(self.parser.current_partition - 1)
            if self.parser.current_partition > 1:
                self.leftArrow.setIcon(self.leftEnabled)
            tts.audio_unload()
            self.ttsLoaded = False
            if self.paused == False:
                self.playPauseTTS()

    def loadLastPartition(self):
        """Get the next partition or milestone"""
        if self.parser.current_partition > 2:
            self.document.setHtml(self.parser.get_last(self.loadTextBrowser, self.loadMileStone))
            self.textBrowser.setDocument(self.document)
            self.progressBar.setValue(self.parser.current_partition - 1)
        elif self.parser.current_partition == 2:
            self.leftArrow.setIcon(self.leftDisabled)
            self.document.setHtml(self.parser.get_last(self.loadTextBrowser, self.loadMileStone))
            self.textBrowser.setDocument(self.document)
            self.progressBar.setValue(self.parser.current_partition - 1)
        tts.audio_unload()
        self.ttsLoaded = False
        if self.paused == False:
            self.playPauseTTS()
        
    def loadMileStone(self):
        """Load generic milestone screen."""
        self.mileStoneScreen = mileStoneScreen.Ui_Generic_Milestone(self.gridLayout, self, self.milestoneIndex)
        self.milestoneIndex += 1
        self.textBrowser.hide()
        # make page invisible
        self.frame.setStyleSheet("border: 00px solid #324143;\n"
                "background: #FAF8F3;\n"
                "padding: -10 px;")
        self.muted = False
        self.toggleTTS()
        self.backgroundFrame.hide()
        self.textToSpeech.hide()
        self.gridLayout.update()

    def loadCompletion(self):
        """Load document completion screen."""
        self.completionScreen = complete.completion_Screen(self.gridLayout, self)
        self.textBrowser.hide()
         # make page invisible
        self.frame.setStyleSheet("border: 00px solid #324143;\n"
                "background: #FAF8F3;\n"
                "padding: -10 px;")
        self.muted = False
        self.toggleTTS()
        self.backgroundFrame.hide()
        self.textToSpeech.hide()
        self.gridLayout.update()


    def loadTextBrowser(self):
        """Check to see if text browser needs to be shown. Hide all other widgets in our grid except for our text browser"""
        if self.textBrowser.isHidden() is not True:
            return
         # make page visible
        self.frame.setStyleSheet("border: 00px solid #324143;\n"
                "background: #fff;\n"
                "padding: -10 px;")
        # Iterate through everything in the grid layout
        for index in range(self.gridLayout.count()):
            self.gridLayout.itemAt(index).widget().hide()
        
        self.textBrowser.show()
        self.backgroundFrame.show()
        self.textToSpeech.show()
        self.gridLayout.update()

    def instantiatePopUps(self):
        """Create and store instances of the configuration and settings UI classes."""
        self.configPopUp = config.Ui_MainWindow(self.adhdReader, self)
        self.configPopUp.hide()

        self.settingsPopUp = settings.Ui_MainWindow(self.adhdReader, self)
        self.settingsPopUp.hide() 

    def togglePopUp(self, popUp: QtWidgets.QMainWindow):
        """If the pop up is visible, hide it. Otherwise show it."""
        if popUp.isVisible():
            popUp.hide()
            self.overlay.hide()
        else:
            self.overlay.setGeometry(self.adhdReader.rect())
            self.overlay.show()
            popUp.show()

            
    def toggleTTS(self):
        """Toggle text to speech."""
        icon = QtGui.QIcon()
        if self.muted:
            self.muted = False
            self.textToSpeech.setStyleSheet(self.ttsOnStyle)
            icon.addPixmap(QtGui.QPixmap("UI/icons/speaker.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.textToSpeech.setIcon(icon)
            self.backgroundFrame.setFixedWidth(380)
            self.backgroundFrame.setStyleSheet("QFrame {border-radius: 25px; \n"
                                               "background-color: rgb(182, 194, 139)}")
            self.textToSpeechLabel.show()
            self.playPause.show()
        else:
            self.muted = True
            self.textToSpeech.setStyleSheet(self.ttsOffStyle)
            icon.addPixmap(QtGui.QPixmap("UI/icons/audio_off.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.textToSpeech.setIcon(icon)
            self.backgroundFrame.setFixedWidth(81)
            self.backgroundFrame.setStyleSheet("QFrame {border-radius: 25px; \n"
                                               "background-color: rgb(255, 255, 255); \n"
                                               "border: 3px solid rgb(182, 194, 139)}")
            self.textToSpeechLabel.hide()
            self.playPause.hide()

    def playPauseTTS(self):
        """Toggle play/pause"""
        icon = QtGui.QIcon()
        if self.paused:
            self.timer = QtCore.QTimer() # Timer for when to stop audio
            self.timer.timeout.connect(self.endAudio)
            if self.ttsLoaded == False:
                tts.text2aud(self.textBrowser.toPlainText(), 0)
                self.ttsLoaded = True
                self.audioLength = int(tts.get_audio_length() * 1000)
            else:
                tts.audio_unpause()
            icon.addPixmap(QtGui.QPixmap("UI/icons/pause.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.playPause.setIcon(icon)
            self.paused = False
            self.timer.start(self.audioLength - int(tts.get_audio_pos()))
            
        else:
            self.timer.stop()
            icon.addPixmap(QtGui.QPixmap("UI/icons/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.playPause.setIcon(icon)
            tts.audio_pause()
            self.paused = True

    def updateReaderToMatchSettings(self):
        """Apply the settings to their relative objects."""
        # Grab settings object
        settings:settings_backend.Settings = self.adhdReader.settings

        # Text
        self.document.setDefaultFont(QtGui.QFont(settings["text"]["style"], int(settings["text"]["size"])))

        # Partition Size
        if self.parser.partition_size != settings["pages"]["size"]:
            # self.parser.current_partition = max(math.floor(self.parser.current_partition * (self.parser.partition_size / settings["pages"]["size"]))-1, 0)
            new_partition_size = max(settings["pages"]["size"], self.parser.min_partition_size)
            print(f"new_partition_size: {new_partition_size}")
            print(f"old partition: {self.parser.current_partition}")
            
            # if self.parser.partition_size > new_partition_size:
            #     self.parser.current_partition = math.floor((self.parser.current_partition-1) * (self.parser.partition_size / new_partition_size))
            # else:
            #     back_step = self.parser.current_partition%math.ceil(new_partition_size/new_partition_size)+1
            #     print(f"back_step: {back_step}")
            #     self.parser.current_partition = math.floor((self.parser.current_partition-back_step) * (self.parser.partition_size / new_partition_size))
            self.parser.partition_size = settings["pages"]["size"]
            self.parser.start_sentence = self.parser.sentences_read + 1     # we have read sentences_read sentences so far, so we start at the next one
            self.parser.partition_text()
            # self.parser.go_to_sentence(target_sentence)
            self.loadNextPartition()
            print(f"new partition: {self.parser.current_partition}")
            self.progressBar.setMaximum(len(self.parser.partitions))
            self.progressBar.setValue(self.parser.current_partition - 1)
            print("Calling progress bar set val")
            settings["pages"]["size"] = self.parser.partition_size
            print(settings["pages"]["size"])

        # Milestones
        self.parser.set_milestone_frequency(settings["milestones"]["frequency"])

        check_boxes = self.settingsPopUp.grabMilestoneCheckBoxes()
        anyMilestonesEnabled = False 
        for key, value in check_boxes.items():
            settings["milestones"]["enabled"][key] = value.isChecked()
            # if a checkbox is checked, milestonesenabled will be true
            anyMilestonesEnabled = (anyMilestonesEnabled or value.isChecked())

        self.parser.set_milestones_enabled(anyMilestonesEnabled)
        if self.mileStoneScreen is not None:
            self.mileStoneScreen.updateRemainingMilestonesText(self.parser.milestones_remaining)
            self.mileStoneScreen.updateMilestonePicked()

            # I'm sorry about this
            if self.mileStoneScreen.mileStoneWidget is not None and self.mileStoneScreen.mileStoneChoice == "Reading Comprehension Questions":
                # In this specific scenario, allows changing font size and style of text box
                self.mileStoneScreen.mileStoneWidget.textBox.setFont(QtGui.QFont(settings["text"]["style"], int(settings["text"]["size"])))

            
    def endAudio(self):
        """End audio"""
        while tts.get_audio_playing():
            pass
        self.paused = False
        self.playPauseTTS()
        tts.audio_rewind()