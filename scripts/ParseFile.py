import fitz
from bs4 import BeautifulSoup
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

    def __init__(self, partition_size=50, milestone_frequency=5, text=""):
        ''' This function initializes the Partition_Text class '''
        # Text variables
        self.text = text                                # string of text in file
        self.partitions = []                            # list of partitions
        self.file_title = "Unitled"
        self.isXHTML = False                            # boolean to check if text is in xhtml format


        # Partition variables
        self.partition_size = partition_size            # number of words per partition
        self.milestone_frequency = milestone_frequency  # number of partitions between milestones
        

        # Counter variables
        self.current_partition = 0                      # index of current partition
        self.milestone_counter = 0                      # number of partitions since last milestone (resets to 0 after each milestone)
        self.milestone_running_count = 0                # number of milestones encountered so far
        self.milestones_remaining = int(len(self.partitions) / self.milestone_frequency) + 1 # total number of milestones for reading 

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
                json += page.get_text("json")
                text += xhtml
            # remove images from text
            text = re.sub(r'<img(?s:.)*?/>', '', text)
            # write xml to file
            self.text = text

            self.file_name = str(text[:20]) + "..."
            self.partition_text()
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
            partitions_remaining = len(self.partitions) - self.current_partition
            self.milestones_remaining = int(partitions_remaining / self.milestone_frequency) + self.milestone_running_count
            self.milestone_counter = 0
               
                
    def get_partitions_list_size(self):
        return len(self.partitions)

    def partition_text(self):
        ''' This function partitions the text into strings of size partition_size (or less) and stores them in a list '''
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
                self.partition_size = max_sentence                                                  # increase partition size to length of longest sentence (TODO: should we do this or just throw an error?)

            # Partition text into strings of size partition_size (or less)
            while len(sentences) > 0:                                                               # while there are more sentences to partition
                partition = ""
                while len(sentences) > 0\
                    and len((partition + " " + sentences[0]).split())\
                        <= self.partition_size:                            # while the current partition would not exceed the partition size if the next sentence were added
                    partition = " ".join([partition, sentences.pop(0)])         # add next sentence to current partition
                
                self.partitions.append(partition.strip())                       # add current partition to list of partitions

    def partition_text_xhtml(self):
        soup = BeautifulSoup(self.text, "html.parser")
        # go through all elements in soup
        children = []
        # go through soup and store all single child elements in sentences as a tuple of (text, [tags]]))
        for child in soup.recursiveChildGenerator():
            if child.name:
                if len(child.contents) == 1:
                    if child.name == "b" or child.name == "i" or child.name == "u":
                        # the previous element should be bolded, italicized, or underlined, so add it to the previous element
                        children[-1] = (children[-1][0], children[-1][1] + [child.name])
                    else:
                        children.append((child.text, [child.name]))
        # now we have our children as a list of tuples (text, [tags]), tokenize the text by sentence
        for i in range(len(children)):
            children[i] = (sent_tokenize(children[i][0]), children[i][1])
        # now we have a list of tuples (list of sentences, [tags]), we want a list of tuples (individual sentence, [tags])
        sentences = []
        for child in children:
            for sentence in child[0]:
                sentences.append((sentence, child[1]))

        # Check if partition size is too small
        max_sentence = heapq.nlargest(1, [len(sentence[0].split()) for sentence in sentences])[0]  # length of longest sentence
        if max_sentence > self.partition_size:                                                  # if the longest sentence is longer than the partition size
            print("Partition size is too small, increasing partition size to", max_sentence)
            self.partition_size = max_sentence                                                  # increase partition size to length of longest sentence (TODO: should we do this or just throw an error?)

        # Partition text into strings of size partition_size (or less)
        while len(sentences) > 0:                                                               # while there are more sentences to partition
            partition = ("",[]) # will be a list of tuples (partition text without tags, [(sentence, [tags])])
            while len(sentences) > 0\
                and len((partition[0] + " " + sentences[0][0]).split())\
                    <= self.partition_size:                            # while the current partition would not exceed the partition size if the next sentence were added
                next_sentence = sentences.pop(0)                     # get next sentence
                partition = (" ".join([partition[0], next_sentence[0]]),partition[1]+ [next_sentence])         # add next sentence to current partition
            # now we have a partition with text of size partition_size (or less) and a list of tuples (sentence, [tags]) that make up that partition
            # take the sentences and tags from the partition and add them to the list of partitions
            text = ""
            for sentence in partition[1]:
                tagged_sentence = sentence[0]
                sentence[1].reverse()
                for tag in sentence[1]: # reverse the list of tags so that the tags are in the correct order
                    tagged_sentence = "<" + tag + ">" + tagged_sentence + "</" + tag + ">" # add tags to sentence
                text += tagged_sentence
            # remove adjacent tags of the same type (i.e. if there is an end tag followed by a start tag OF THE SAME TYPE, remove both)
            text = re.sub(r'</(\w+)><\1>', ' ', text)
            self.partitions.append(text)                        # add partition to list of partitions

        self.milestones_remaining = int(len(self.partitions) / self.milestone_frequency) # use new list size to determing remaining partitions

    # Return next partition or milestone
    def get_next(self, loadMileStone, loadTextBrowser):
        ''' This function returns the next partition or milestone or None if there are no more partitions '''
        if self.current_partition < len(self.partitions):           # if there are more partitions
            if self.milestone_counter == self.milestone_frequency:      # if milestone
                self.milestone_counter = 0                                  # reset milestone counter
                self.milestone_running_count += 1                           # increment milestone counter
                loadMileStone()                                     # return milestone 
            else:                                                       # if not milestone
                self.milestone_counter += 1                                 # increment milestone counter
                self.current_partition += 1                                 # increment current partition
                # print(len(self.partitions[self.current_partition - 1].split())
                loadTextBrowser()                                   # call to switch back over to text browser if necessary 
                return self.partitions[self.current_partition - 1]          # return next partition
        else:                                                       # if no more partitions
            return None                                                 # return None (TODO: replace with front end call)
        
    # Return last partition or milestone
    def get_last(self, loadTextBrowser):
        ''' This function returns the last partition or milestone or None if there are no more partitions '''
        if self.current_partition > 1: 
            if self.milestone_counter > 1:           
                # deincrement milestone counter
                self.milestone_counter -= 1
                self.current_partition -= 1                                 # increment current partition
                # print(len(self.partitions[self.current_partition - 1].split())
            elif self.milestone_counter == 1:
                self.current_partition -= 1 
            else:   # if milestone_counter = 0, that means we are on a milestone screen
                self.milestone_counter = self.milestone_frequency
                self.milestone_running_count -= 1               # keeps us from counting the same milestone we've yet to pass
            loadTextBrowser()                                   # call to switch back over to text browser if necessary 
            return self.partitions[self.current_partition - 1]          # return next partition
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
    
