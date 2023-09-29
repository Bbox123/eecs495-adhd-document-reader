import pdftotext
import sys

class File_Parser(object):

    # call respective parsing function per file type
    def parse_file(self, file_type, file_name):
        if file_type == "txt":
            self.parse_txt(file_name)
        if file_type == "pdf":
            self.parse_pdf(file_name)

    # parse txt file corresponding to file name
    def parse_txt(self, file_name):
        with open(file_name, "r") as f:
            print(f.read())

    # parse pdf file corresponding to file name
    def parse_pdf(self, file_name):
        with open(file_name, "rb") as f:
            pdf = pdftotext.PDF(f)
            print("\n\n".join(pdf))

if __name__ == "__main__":
    parser = File_Parser()
    print()
    parser.parse_file(sys.argv[1], sys.argv[2])
