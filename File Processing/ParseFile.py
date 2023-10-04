import pdftotext
import sys
import re

# Class to partition text into strings of size partition_size
class Partition_Text(object):

    def __init__(self, partition_size=50, milestone_frequency=5):
        ''' This function initializes the Partition_Text class '''
        # Text variables
        self.text = ""                                  # string of text in file
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
            self.text = "\n\n".join(pdf)    # string of text in file
            self.partition_text()           # call partition_text function

    def partition_text(self):
        ''' This function partitions the text into strings of size partition_size and stores them in a list '''
        words = self.text.split()   # list of words in text
        num_words = len(words)      # number of words in text
        num_partitions = num_words // self.partition_size  # number of partitions
        # Add extra partition if necessary
        if num_words % self.partition_size != 0:    # if there are extra words
            num_partitions += 1                         # add extra partition
        # Partition text into list of strings of size partition_size
        for i in range(num_partitions):             # for each partition
            self.partitions.append(" ".join(words[i*self.partition_size:(i+1)*self.partition_size])) # add partition to list of partitions

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
                return self.partitions[self.current_partition - 1]          # return next partition
        else:                                                       # if no more partitions
            return None                                                 # return None (TODO: replace with front end call)
        
    

if __name__ == "__main__":
    parser = Partition_Text()                                   # create parser
    parser.parse_file(sys.argv[1], sys.argv[2])                 # parse file
    # FOR TESTING PURPOSES
    next_partition = parser.get_next()                          # get first partition
    while next_partition != None:                               # while there are more partitions
        if next_partition == "milestone":                           # if milestone
            print("milestone")                                          # print milestone
        else:                                                       # if not milestone
            print("partition #", parser.current_partition, ":")         # print partition number
            print(next_partition)                                       # print partition
        next_partition = parser.get_next()                          # get next partition
    print("end of file")                                        # print end of file
    # END TESTING
    
