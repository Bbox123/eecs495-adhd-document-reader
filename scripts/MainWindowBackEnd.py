from PyQt5 import QtWidgets

def collectTextFromTextBox(inputText):
    """inputText contains all the text that was placed in the text box before submit was clicked"""
    print(inputText)

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
    
    with open(filepath) as file:
        for line in file:
            print(line)