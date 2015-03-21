#Created by Panagiotis Roubatsis

#Description:A python script that adds
#a header to all the file types with given
#extensions in the current directory

#Usage:     add-header.py header_file (file extensions)
#Example:   add-header.py header.txt txt cpp h

#sys.argv and os.listdir
import sys
import os

#Creates a generator for all the file names that
#have one of the given extensions and is not
#the script or header file.
def getFileNames(argv):
    #Exclude script and header files
    exclude = [argv[0], argv[1]]

    #Include only these file extensions
    filters = argv[2:]

    allFiles = os.listdir(".")
    for f in allFiles:
        dotIndex = f.rfind(".")
        if dotIndex == -1:
            continue
        
        extension = f[dotIndex + 1:]
        if f in exclude or extension not in filters:
            continue

        yield f


#Load the header's data
headerFile = open(sys.argv[1], "r")
headerString = headerFile.read()
headerFile.close()

#Add the header to the beginning of the appropriate files
fileNames = getFileNames(sys.argv)
for name in fileNames:
    dataFile = open(name, "r+")
    dataString = dataFile.read()
    
    dataFile.seek(0)
    dataFile.write(headerString + dataString)
    dataFile.close()

