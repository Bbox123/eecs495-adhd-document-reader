from .ParseFile import File_Parser
def parse_file(file_type, file_name):
    parser = File_Parser() # Create a File_Parser object
    if file_type == "txt":
        return parser.parse_txt(file_name)
    if file_type == "pdf":
        return parser.parse_pdf(file_name)
    return "ERROR: Invalid file type"
