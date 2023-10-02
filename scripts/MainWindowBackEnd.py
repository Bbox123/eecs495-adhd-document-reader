from PyQt6 import QtWidgets
## For File Parsing
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Add parent directory to path
from FileProcessing import parse_file
##

def collectTextFromTextBox(self, inputText):
    """inputText contains all the text that was placed in the text box before submit was clicked"""
    # If user clicks submit and they haven't added any text, return
    if (len(inputText) == 0 or inputText == "Paste into text box..."):
        return
    self.headerText.setText(f"input complete: {inputText}")
    self.submitButton.setVisible(False)
#    print(inputText)

def importFile():
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
    
    ## Parsing the specified file
    file_type = ""
    # Specifying the file type (this is just the first idea that came to mind, might need to change)
    if ".pdf" in filepath:
        file_type = "pdf"
    elif ".txt" in filepath:
        file_type = "txt"
    else:
        print("ERROR: Invalid file type")

    # Parsing the file
    file_text = parse_file(file_type, filepath)
    print(file_text)
    ##
    

    with open(filepath) as file:
        for line in file:
            print(line)
