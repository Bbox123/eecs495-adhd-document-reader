import pdftotext
import sys
import heapq
from nltk import sent_tokenize
import os
import re

# Class to partition text into strings of size partition_size
class Partition_Text(object):

    def __init__(self, partition_size=50, milestone_frequency=5, text=""):
        ''' This function initializes the Partition_Text class '''
        # Text variables
        self.text = text                                # string of text in file
        self.partitions = []                            # list of partitions

        # Partition variables
        self.partition_size = partition_size            # number of words per partition
        self.milestone_frequency = milestone_frequency  # number of partitions between milestones

        # Counter variables
        self.current_partition = 0                      # index of current partition
        self.milestone_counter = 0                      # number of partitions since last milestone (resets to 0 after each milestone)

    def parse_file(self, file_type, file_name):
        ''' This function takes in a file type and file name and calls the respective parsing function for that file type '''
        # Parse txt file
        if file_type == "txt":
            self.parse_txt(file_name)
        # Parse pdf file
        if file_type == "pdf":
            self.parse_pdf(file_name)

    def parse_txt(self, file_name):
        ''' This function takes in a file name and parses the txt file corresponding to that file name, then calls the partition_text function '''
        with open(file_name, "r") as f:
            self.text = f.read()    # string of text in file
            self.partition_text()   # call partition_text function

    def parse_pdf(self, file_name):
        ''' This function takes in a file name and parses the pdf file corresponding to that file name, then calls the partition_text function '''
        with open(file_name, "rb") as f:
            pdf = pdftotext.PDF(f)          # list of strings of text in file

            # Note: Added to handle columned pdfs, this used to work like below but it's not working anymore
            # Generates a text file from the pdf, and then parses that text file
            os.system("pdftotext " + file_name)     # run command line pdftotext
            text = re.sub(".pdf",".txt",file_name)  # name of text file that pdftotext creates
            self.parse_txt(text)                    # parse text file that pdftotext creates

            # Note: This is how it used to work
            # self.text = "\n\n".join(pdf)    # string of text in file
            # self.partition_text()           # call partition_text function

    def partition_text(self):
        ''' This function partitions the text into strings of size partition_size (or less) and stores them in a list '''
        # Format text and split into sentences
        self.text = " ".join(self.text.split())                                                 # remove extra whitespace
        sentences = sent_tokenize(self.text)                                                    # list of sentences in text

        # Check if partition size is too small
        max_sentence = heapq.nlargest(1, [len(sentence.split()) for sentence in sentences])[0]  # length of longest sentence
        if max_sentence > self.partition_size:                                                  # if the longest sentence is longer than the partition size
            print("Partition size is too small, increasing partition size to", max_sentence)
            self.partition_size = max_sentence                                                  # increase partition size to length of longest sentence (TODO: should we do this or just throw an error?)

        # Partition text into strings of size partition_size (or less)
        while len(sentences) > 0:                                                               # while there are more sentences to partition
            partition = ""
            while len(sentences) > 0\
                and len((partition + " " + sentences[0]).split())\
                    <= self.partition_size:                            # while the current partition would not exceed the partition size if the next sentence were added
                partition = " ".join([partition, sentences.pop(0)])         # add next sentence to current partition
            
            self.partitions.append(partition.strip())                       # add current partition to list of partitions

    # Return next partition or milestone
    def get_next(self):
        ''' This function returns the next partition or milestone or None if there are no more partitions '''
        if self.current_partition < len(self.partitions):           # if there are more partitions
            if self.milestone_counter == self.milestone_frequency:      # if milestone
                self.milestone_counter = 0                                  # reset milestone counter
                return "milestone"                                          # return milestone (TODO: replace with front end call)
            else:                                                       # if not milestone
                self.milestone_counter += 1                                 # increment milestone counter
                self.current_partition += 1                                 # increment current partition
                # print(len(self.partitions[self.current_partition - 1].split())
                return self.partitions[self.current_partition - 1]          # return next partition
        else:                                                       # if no more partitions
            return None                                                 # return None (TODO: replace with front end call)

## Partition_Text usage
    # if using a txt or pdf file:
        # parser = Partition_Text()     # create parser
    # if using a string (i.e. from text box input):
        # parser = Partition_Text(text="This is a test string")    # create parser with text argument
    # parser.parse_file("txt", "test.txt")    # parse file by calling parse_file function with file type and file name as arguments
    # next_partition = parser.get_next()      # get first partition or milestone by calling get_next function, will return either partition or milestone or None if there are no more partitions
    # parser.partition_text()                                  # partition text by calling partition_text function

## End Partition_Text usage

if __name__ == "__main__":
    parser = Partition_Text()                                   # create parser
    parser.parse_file(sys.argv[1], sys.argv[2])                 # parse file
    # FOR TESTING PURPOSES
    next_partition = parser.get_next()                          # get first partition
    while next_partition != None:                               # while there are more partitions
        if next_partition == "milestone":                           # if milestone
            print("---milestone---", "\n")                              # print milestone
        else:                                                       # if not milestone
            print("partition #", parser.current_partition, ":")         # print partition number
            print(next_partition, "\n")                                 # print partition
        next_partition = parser.get_next()                          # get next partition
    print("end of file")                                        # print end of file
    # END TESTING
    
