'''
This file cleans the dataset, takes every video transcript from their individually stored file,
and combines them all into one large file. This will be our dat file.
'''

import os

# List to find all subdirectories
allDirectories = [x[0] for x in os.walk("cs-410")]

# Build a text file for all the transcripts to be written to
f = open("allData.txt", "w")

# Loop through all of the directories
for i in allDirectories:
    # Looking at just the transcripts folders
    if i.endswith("-lessons"):
        # Looping through all of the videos in a week
        for file in os.listdir(i):
            if file.endswith(".en.txt"):
                g = open(i+'/'+file, "r")
                newFile = ""
                # Loop to make every file one single line
                for line in g:
                    newFile += line.strip() + " "
                f.write(newFile+"\n")
f.close()


#f.write("Now the file has more content!")
f.close()