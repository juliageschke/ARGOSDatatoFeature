##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: John.Fay@duke.edu (for ENV859)
##---------------------------------------------------------------------

#Import modules/packages
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

#Construct a while loop to iterate through all lines in the datafile

#Open the ARGOS data file for reading
inputFileObj = open(inputFile, 'r')

#Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()
while lineString:
    #Set code to run only if the line contains the string "Date: "
    if("Date :" in lineString):
        #parse the line into a list
        lineData=lineString.split()
        #extract attributes from the datum header line
        tagID=lineData[0]
        #extract location info from the next line
        line2String=inputFileObj.readline()
        #parse the line into a list
        line2Data=line2String.split()
        #extract the data we need to variables
        obsLat=line2Data[2]
        obsLon=line2Data[5]
        #print results to see how we're doing
        print(tagID,"Lat:"+obsLat,"Long:"+obsLon)
    #Move to the next line so the while loop progresses
    lineString=inputFileObj.readline()

#close the file object
inputFileObj.close()