'''
This file cleans the dataset, takes every video transcript from their individually stored file,
and combines them all into one large file. This will be our dat file.
'''

import os

# List to find all subdirectories
allDirectories = [x[0] for x in os.walk("cs-410")]

# Build a text file for all the transcripts to be written to


import re

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    print(newString)


# Loop through all of the directories
for i in allDirectories:
    # Looking at just the transcripts folders
    if i.endswith("-lessons"):
        # Looping through all of the videos in a week
        for file in os.listdir(i):
            if file.endswith(".en.txt"):
                modified = replacenth(file, '-','.',2)
                if modified is not None:
                    print(modified)

