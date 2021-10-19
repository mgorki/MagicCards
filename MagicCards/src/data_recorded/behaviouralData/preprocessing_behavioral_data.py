### A simple program for preprocessing the raw behavioral data into a more usefull csv format ###
### It creates to separate csv files: one for metadata and another for the behavioral data itself ###
# You may have to adjust the paths in the paths section # 
# Make sure the files for preprocessed output are not already existing (you would get an error) #


import os
import ast
import csv


cwd = os.getcwd()
print("CWD =", cwd)

## paths for loading the raw data and saving the preprocessed one. You may have to adjust them ##
loadPath = str(cwd + "\\data_recorded\\behaviouralData\magic_cards_behaviour.csv")
saveBehavioralDataPath = str(cwd + "\\data_recorded\\behaviouralData\PREPROCESSED_magic_cards_behaviour.csv")
saveMetadataPath = str(cwd + "\\data_recorded\\behaviouralData\PREPROCESSED_METADATA_magic_cards_behaviour.csv")

rawData = open(loadPath, "r")
rawLines = rawData.readlines()
behavioralDataList = []
metadataList = []

headerBehavioralData = ""
headerMetadata = ""

for line in rawLines:
    a = line
    if not "experiment completed" in a:
        a = ast.literal_eval(a)
        if not 'Age' in list(a.keys()):
            if headerBehavioralData == "":
                headerBehavioralData = list(a.keys())
                print(headerBehavioralData)
            behavioralDataList.append(a)  # For testing only
        else: 
            if headerMetadata == "":
                headerMetadata = list(a.keys())
                print(headerBehavioralData)  # For testing only
            metadataList.append(a)


try:
    with open(saveBehavioralDataPath, 'x') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headerBehavioralData)
        writer.writeheader()
        for data in behavioralDataList:
            writer.writerow(data)
except IOError:
    print("I/O error for behavioral data. Is the path well defined? Make also sure the file is not already existing.")

try:
    with open(saveMetadataPath, 'x') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headerMetadata)
        writer.writeheader()
        for data in metadataList:
            writer.writerow(data)
except IOError:
    print("I/O error for Metadata. Is the path well defined? Make also sure the file is not already existing.")