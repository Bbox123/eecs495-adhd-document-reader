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

    def __init__(self, settings, text="", start_sentence=0, ):
        ''' This function initializes the Partition_Text class '''
        # Text variables
        self.text = text                                # string of text in file
        self.partitions = []                            # list of partitions
        self.file_title = "Unitled"
        self.isXHTML = False                            # boolean to check if text is in xhtml format


        # Partition variables
        self.partition_size = settings["pages"]["size"]            # number of words per partition
        self.milestone_frequency = settings["milestones"]["frequency"]   # number of partitions between milestones
        self.milestones_enabled = True                  # whether milestones are currently enabled at all in settings
        self.start_sentence = start_sentence            # sentence number to start reading from
        self.partition_to_num_sentences = {}            # dictionary mapping partition number to number of sentences in that partition (used to determine which partition a given sentence number is in)
        

        # Counter variables
        self.current_partition = 0                      # index of current partition (technically the next partition to be read)
        self.milestone_counter = 0                      # number of partitions since last milestone (resets to 0 after each milestone)
        self.milestone_running_count = 0                # number of milestones encountered so far
        self.milestones_remaining = int(len(self.partitions) / self.milestone_frequency)  # total number of milestones for reading 
        if len(self.partitions) % self.milestone_frequency == 0:
            self.milestones_remaining -= 1
        self.sentences_read = 0                         # number of sentences read so far

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
        self.sentences_read = 0
        self.set_milestones_remaining()
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
            self.min_partition_size = max_sentence
            if max_sentence > self.partition_size:                                                  # if the longest sentence is longer than the partition size
                print("Partition size is too small, increasing partition size to", max_sentence)
                self.partition_size = max_sentence                                                  # increase partition size to length of longest sentence

            num_sentences = 0                                                                      # number of sentences processed so far
            start_point_set = False                                                                # boolean to check if start point has been set
            i = 0                                                                                   # index of current partition
            # Partition text into strings of size partition_size (or less)
            while len(sentences) > 0:                                                               # while there are more sentences to partition
                partition = ""
                len_partition = 0                                                              # number of sentences in current partition
                while len(sentences) > 0\
                    and len((partition + " " + sentences[0]).split())\
                        <= self.partition_size:                            # while the current partition would not exceed the partition size if the next sentence were added
                    len_partition +=1                                                  # increment number of sentences in current partition
                    if not start_point_set and num_sentences + len_partition >= self.start_sentence: # if the start point has not been set and the current partition contains the start sentence
                        self.current_partition = i                                # set current partition to current partition
                        self.sentences_read = num_sentences if i == 0 else num_sentences - self.partition_to_num_sentences[i - 1] # set number of sentences read to number of sentences processed so far
                        start_point_set = True                                          # set start point to true
                    partition = " ".join([partition, sentences.pop(0)])         # add next sentence to current partition
                num_sentences += len_partition                                         # increment number of sentences processed so far
                self.partition_to_num_sentences[i] = len_partition
                i += 1                                                                 # increment index of current partition
                
                self.partitions.append(partition.strip())                       # add current partition to list of partitions
        self.set_milestones_remaining()                                     # use new list size to determing remaining partitions


    def partition_text_xhtml(self):
        
        self.text = re.sub(r'<p><\/p>', '', self.text)
        self.text = re.sub(r'<p>\d+</p>\s*</div>', '', self.text)
        self.text = re.sub(r'<div id="page0">', '', self.text)

        sentences = re.split(r'(<p>.*?<\/p>)', self.text)
        # remove empty strings
        i = 0
        while i < len(sentences):
            if sentences[i] == "":
                sentences.pop(i)
            else:
                i += 1
        # split sentences more using sentence tokenizer
        i = 0
        while i < len(sentences):
            split = sent_tokenize(sentences[i])
            # replace the sentence with the split sentences (end result should still be a list of sentences)
            sentences.pop(i)
            for sentence in split:
                if sentence != "":
                    sentences.insert(i, sentence)
                    i += 1
        # remove newlines
        i = 0
        while i < len(sentences):
            sentences[i] = sentences[i].replace("\n", " ")
            i += 1
            
        # Check if partition size is too small
        max_sentence = heapq.nlargest(1, [len(re.sub(r'<[^>]*>', '', sentence).split()) for sentence in sentences])[0]  # length of longest sentence
        self.min_partition_size = max_sentence
        if max_sentence > self.partition_size:                                                  # if the longest sentence is longer than the partition size
            print("Partition size is too small, increasing partition size to", max_sentence)
            self.partition_size = max_sentence                                                  # increase partition size to length of longest sentence
        
        # while building partitions, find the partition containing the start sentence (the sentence we left off on last time)
        num_sentences = 0                                                                      # number of sentences processed so far
        start_point_set = False                                                                # boolean to check if start point has been set
        i = 0                                                                                   # index of current partition
        while len(sentences) > 0:                                                               # while there are more sentences to partition
                partition = ""
                len_partition = 0                                                              # number of sentences in current partition
                while len(sentences) > 0\
                    and len(re.sub(r'<[^>]*>', '', (partition + " " + sentences[0])).split())\
                        <= self.partition_size:                            # while the current partition would not exceed the partition size if the next sentence were added
                    # finding the start sentence
                    len_partition +=1                                                  # increment number of sentences in current partition
                    if not start_point_set and num_sentences + len_partition >= self.start_sentence: # if the start point has not been set and the current partition contains the start sentence
                        self.current_partition = i                                # set current partition to current partition
                        self.sentences_read = num_sentences if i == 0 else num_sentences - self.partition_to_num_sentences[i - 1] # set number of sentences read to number of sentences processed so far
                        start_point_set = True                                          # set start point to true
                    
                    partition = " ".join([partition, sentences.pop(0)])         # add next sentence to current partition
                num_sentences += len_partition                                         # increment number of sentences processed so far
                self.partition_to_num_sentences[i] = len_partition
                i += 1                                                                 # increment index of current partition

                
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
        # remove occurrences of "</p> <p>" IF AND ONLY IF there is no punctuation immediately before the "</p>"
        i = 0
        while i < len(self.partitions):
            self.partitions[i] = re.sub(r'(?<![.,;:!?>])<\/p> *<p>', ' ', self.partitions[i])
            i += 1

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
                if self.current_partition > 0:
                    self.sentences_read += self.partition_to_num_sentences[self.current_partition - 1]
                self.milestone_counter += 1                                 # increment milestone counter
                self.current_partition += 1                                 # increment current partition
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

            self.sentences_read -= self.partition_to_num_sentences[self.current_partition - 1]
                    
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
    
