import fitz
import sys
import heapq
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
import os
import re
import shutil

from img_ocr import *

# Class to partition text into strings of size partition_size
class Partition_Text(object):

    def __init__(self, partition_size=100, milestone_frequency=5, text=""):
        ''' This function initializes the Partition_Text class '''
        # Text variables
        self.text = text                                # string of text in file
        self.partitions = []                            # list of partitions
        self.file_title = "Unitled"
        self.isXHTML = False                            # boolean to check if text is in xhtml format


        # Partition variables
        self.partition_size = partition_size            # number of words per partition
        self.milestone_frequency = milestone_frequency  # number of partitions between milestones
        self.milestones_enabled = True                  # whether milestones are currently enabled at all in settings
        

        # Counter variables
        self.current_partition = 0                      # index of current partition
        self.milestone_counter = 0                      # number of partitions since last milestone (resets to 0 after each milestone)
        self.milestone_running_count = 0                # number of milestones encountered so far
        self.milestones_remaining = int(len(self.partitions) / self.milestone_frequency)  # total number of milestones for reading 
        if len(self.partitions) % self.milestone_frequency == 0:
            self.milestones_remaining -= 1

    def parse_file(self, file_type, file_name):
        ''' This function takes in a file type and file name and calls the respective parsing function for that file type '''
        # set file title to be used in title bar
        self.file_title = os.path.basename(file_name)
        # Parse txt file
        if file_type == "txt":
            self.parse_txt(file_name)
        # Parse pdf file
        if file_type == "pdf":
            is_pure_image = False
            if is_pure_image:
                self.parse_pdf_w_image(file_name)
            else:
                self.parse_pdf(file_name)
    
    def restart_file(self):
        self.current_partition = 0                     # index of current partition
        self.milestone_counter = 0                      # number of partitions since last milestone (resets to 0 after each milestone)
        self.milestone_running_count = 0
        print(str(self.get_partitions_list_size()))
        pass

    def parse_txt(self, file_name):
        ''' This function takes in a file name and parses the txt file corresponding to that file name, then calls the partition_text function '''
        with open(file_name, "r") as f:
            self.text = f.read()    # string of text in file

    def parse_pdf(self, file_name):
        ''' This function takes in a file name and parses the pdf file corresponding to that file name, then calls the partition_text function '''
        with fitz.open(file_name) as doc:
            text = ""
            json = ""
            for page in doc:
                xhtml = page.get_text("xhtml")
                text += xhtml
            # remove images from text
            text = re.sub(r'<img(?s:.)*?/>', '', text)
            # write xml to file
            self.text = text

            self.file_name = str(text[:20]) + "..."
            self.isXHTML = True

    def parse_pdf_w_image(self, file_name):
        path = "var"
        text = ""
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            shutil.rmtree(path)           # Removes all the subdirectories!
            os.mkdir(path)
        pdf2imgs(file_name)
        
        for filename in sorted(os.listdir(path)):
            full_file = os.path.join(path, filename)
            text += img2str(full_file)
            self.text = text

    def set_milestone_frequency(self, frequency):
        if self.milestone_frequency != frequency:
            self.milestone_frequency = frequency
            self.set_milestones_remaining()

    def set_milestones_remaining(self):
        partitions_remaining = len(self.partitions) - self.current_partition
        self.milestones_remaining = int(partitions_remaining / self.milestone_frequency) + self.milestone_running_count
        if partitions_remaining % self.milestone_frequency == 0:
            self.milestones_remaining -= 1
        self.milestone_counter = 0      

    def set_milestones_enabled(self, milestones_enabled):
        self.milestones_enabled = milestones_enabled

                
    def get_partitions_list_size(self):
        return len(self.partitions)

    def partition_text(self):
        ''' This function partitions the text into strings of size partition_size (or less) and stores them in a list '''
        self.partitions = []
        if self.isXHTML:
            self.partition_text_xhtml()
        else:
            # Format text and split into sentences
            self.text = " ".join(self.text.split())                                                 # remove extra whitespace
            sentences = sent_tokenize(self.text)                                                    # list of sentences in text

            # Check if partition size is too small
            max_sentence = heapq.nlargest(1, [len(sentence.split()) for sentence in sentences])[0]  # length of longest sentence
            if max_sentence > self.partition_size:                                                  # if the longest sentence is longer than the partition size
                print("Partition size is too small, increasing partition size to", max_sentence)
                self.partition_size = max_sentence                                                  # increase partition size to length of longest sentence

            # Partition text into strings of size partition_size (or less)
            while len(sentences) > 0:                                                               # while there are more sentences to partition
                partition = ""
                while len(sentences) > 0\
                    and len((partition + " " + sentences[0]).split())\
                        <= self.partition_size:                            # while the current partition would not exceed the partition size if the next sentence were added
                    partition = " ".join([partition, sentences.pop(0)])         # add next sentence to current partition
                
                self.partitions.append(partition.strip())                       # add current partition to list of partitions
        self.set_milestones_remaining()                                     # use new list size to determing remaining partitions


    def partition_text_xhtml(self):
        sentences = sent_tokenize(self.text)                                                    # list of sentences in text
        # split sentences with newlines
        i = 0
        while i < len(sentences):
            split = sentences[i].split("\n")
            split = [sentence.strip() for sentence in split if sentence != ""]
            sentences = sentences[:i] + split + sentences[i+1:]
            i += len(split)

        # Check if partition size is too small
        max_sentence = heapq.nlargest(1, [len(re.sub(r'<[^>]*>', '', sentence).split()) for sentence in sentences])[0]  # length of longest sentence
        if max_sentence > self.partition_size:                                                  # if the longest sentence is longer than the partition size
            print("Partition size is too small, increasing partition size to", max_sentence)
            self.partition_size = max_sentence                                                  # increase partition size to length of longest sentence
        
        while len(sentences) > 0:                                                               # while there are more sentences to partition
                partition = ""
                while len(sentences) > 0\
                    and len(re.sub(r'<[^>]*>', '', (partition + " " + sentences[0])).split())\
                        <= self.partition_size:                            # while the current partition would not exceed the partition size if the next sentence were added
                    partition = " ".join([partition, sentences.pop(0)])         # add next sentence to current partition
                
                # complete any tags that were started but not finished (detect using regex)
                start_tags = re.findall(r'<(\w+)>', partition)
                end_tags = re.findall(r'</(\w+)>', partition)
                while start_tags != []:
                    tag = start_tags[0]
                    if tag in end_tags:
                        start_tags.remove(tag)
                        end_tags.remove(tag)
                    else:
                        partition += "</" + tag + ">"
                        sentences[0] = "<" + tag + ">" + sentences[0]
                        start_tags.remove(tag)
                # add partition to list of partitions
                self.partitions.append(partition.strip())                       # add current partition to list of partitions

    # Return next partition or milestone
    def get_next(self, loadMileStone, loadTextBrowser):
        ''' This function returns the next partition or milestone or None if there are no more partitions '''
        if self.current_partition < len(self.partitions):           # if there are more partitions
            if self.milestone_counter >= self.milestone_frequency:      # if milestone
                self.milestone_counter = 0                                  # reset milestone counter
                self.milestone_running_count += 1                           # increment milestone counter
                if self.milestones_enabled:                                 
                    loadMileStone()                                       
                else:                                                     #still resets counter when no milestones enabled so milestone count will be correct if reenabled
                    loadTextBrowser()                                   # call to switch back over to text browser if necessary 
                    return self.partitions[self.current_partition - 1]                                     # return milestone 
            else:                                                       # if not milestone
                self.milestone_counter += 1                                 # increment milestone counter
                self.current_partition += 1                                 # increment current partition
                # print(len(self.partitions[self.current_partition - 1].split())
                loadTextBrowser()                                   # call to switch back over to text browser if necessary 
                print(self.milestone_counter)
                return self.partitions[self.current_partition - 1]          # return next partition
        else:                                                       # if no more partitions
            return None                                                 # return None (TODO: replace with front end call)
        
    # Return last partition or milestone
    def get_last(self, loadTextBrowser, milestoneScreen):
        ''' This function returns the last partition or milestone or None if there are no more partitions '''
        
        if self.current_partition > 1: 
            # deincrement milestone counter
            self.milestone_counter -= 1
            # increment current partition
            self.current_partition -= 1   
                    
            loadTextBrowser()                                   # call to switch back over to text browser if necessary 

            print(self.milestone_counter)

            return self.partitions[self.current_partition - 1]          # return prev partition
        else:                                                       # if no more partitions  
            return None 



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
    
