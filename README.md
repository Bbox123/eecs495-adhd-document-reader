This is an ADHD document reading assistant project as a part of an EECS495 project. This project is being developed by Sophia Johnecheck, Jacob Harwood, Shuyu Wu, and Brandon Fox.

# Table of Contents

1. [Developer Setup Instructions](#Developer-Setup-Instructions)
2. [Alpha Release Usage Instructions](#alpha-release-usage-instructions)

## Developer Setup Instructions

Set up environment (do this in project directory):

### Make sure you have python3 installed:
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip python3-venv python3-wheel python3-setuptools
$ sudo apt install tesseract-ocr
$ sudo apt install libtesseract-dev

### Create a virtual environment and activate it:
$ python3 -m venv env
$ source env/bin/activate

### Install the required packages for the project:
$ pip install -r requirements.txt

### To run the project:
$ ./bin/ADHDReaderRun

### ParseFile.py Usage:
$ python3 scripts/ParseFile.py <file type (txt or pdf)> <file name/path>
Prints out the parsed and partitioned text to the console

## Alpha Release Usage Instructions

1. [Download Files](#download-files)
2. [Navigate and Unpack](#navigate-and-unpack)
3. [Setup](#setup)

### Download Files:
Download the .zip containing our project files:
(https://github.com/Bbox123/eecs495-adhd-document-reader/archive/refs/heads/main.zip)

Setup a Linux environment of your choice (most of our team uses WSL)

Move the .zip file from your downloads directory into this environment:  
$ cp -R <source_directory> <dest_directory>

### Navigate and Unpack:
Navigate to <dest_directory> and run the following commands 

$ sudo apt-get install unzip  
$ unzip eecs495-adhd-document-reader-main.zip  
$ mv eecs495-adhd-document-reader-main/* .  
$ rm -r eecs495-adhd-document-reader-main eecs495-adhd-document-reader-main.zip

### Setup:
./bin/alphaSetup

### To run the project:
$ ./bin/ADHDReaderRun
