from PyQt5 import QtWidgets
import ReadingScreen as rs
import PyPDF2

def collectTextFromTextBox(self, inputText, widget):
    """inputText contains all the text that was placed in the text box before submit was clicked"""
    # If user clicks submit and they haven't added any text, return
    if (len(inputText) == 0 or inputText == "Paste into text box..."):
        return
    self.headerText.setText(f"input complete: {inputText}")
    self.submitButton.setVisible(False)
    goToReadingScreen(self, widget, inputText)
    

def importFile(self, widget):
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

    if filepath.endswith('.txt'):
        with open(filepath, 'r') as file:
            # first case: txt
            text = file.read()
            goToReadingScreen(self, widget, text)
    else:  # pdf
        with open(filepath, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            goToReadingScreen(self, widget, text)

# Will be adjusted to display text
def goToReadingScreen(self, widget, text):
    ReadingScreen = QtWidgets.QMainWindow()
    ui_rs = rs.Ui_ReadingScreen()
    ui_rs.setupUi(ReadingScreen, widget, text)

    widget.addWidget(ReadingScreen)
    widget.setCurrentIndex(1)
