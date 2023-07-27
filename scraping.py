from bs4 import BeautifulSoup
import requests
import json
import os
import time

startTime = time.time()
#Requesting HTML from the website
link = "https://onlinenonograms.com/"

#Functions
def extractNumbers(inputTable, numbersTable):
        for row in inputTable.findAll('tr'):
            for cell in row.findAll('td'):
                    numbersTable.append(cell.text)

#Splitting the lists into chunks
def splitNumberLists(inputList, splitBy):
    for i in range(0, len(inputList), splitBy):
        yield inputList[i:i + splitBy]

for i in range(600, 700):
    
    #Requesting HTML from the website
    with requests.session() as requestHTML:
        requestedHTML = requestHTML.get(f"{link}{i}")
    soup = BeautifulSoup(requestedHTML.content, 'lxml')
    
    # Defining colorCount of the puzzle
    divColor = soup.find('div', attrs = {'id':'maincolors'})  
    colorCount = len(divColor.findAll())

    # If the puzzle has more than 2 colors, skip it
    if colorCount > 2:
        continue   
   
    # Defining variables
    puzzleDimensions = {
    'width': int,
    'height': int
    }
    extractedColumnNumbers = []
    extractedRowNumbers = []
    columnNumbers = []
    rowNumbers = []

    # Extracting Puzzle ID
    extractID = soup.find('img', attrs = {'title':'Nonogram ID'})
    puzzleID = extractID.next_sibling
    puzzleID = puzzleID.strip()

    # Extracting Puzzle Dimensions
    extractDimensions = soup.find('img', attrs = {'title':'Nonogram size'})   
    puzzleDimensionsStr = extractDimensions.next_sibling
    puzzleDimensionsStr = puzzleDimensionsStr.strip()
    partitions = puzzleDimensionsStr.split('x')
    puzzleDimensions['width'] = int(partitions[0])
    puzzleDimensions['height'] = int(partitions[1])   
         
    # Creating file name
    fileName = f"{puzzleID}_{puzzleDimensionsStr}.json"
                
    # Extracting Column and Row numbers
    columnTable = soup.find('table', attrs = {'id':'cross_top'})
    rowTable = soup.find('table', attrs = {'id':'cross_left'})
    extractNumbers(columnTable, extractedColumnNumbers)
    extractNumbers(rowTable, extractedRowNumbers)

    #Splitting the lists into chunks
    columnNumbers = list(splitNumberLists(extractedColumnNumbers, puzzleDimensions['width']))
    rowNumbers = list(splitNumberLists(extractedRowNumbers, puzzleDimensions['height']))
    
    # Writing to JSON file
    jsonObject = {
        'puzzleLink': f'{link}{puzzleID}',
        'puzzleID': puzzleID,
        'puzzleDimensions': puzzleDimensions,
        'columnNumbers': columnNumbers,
        'rowNumbers': rowNumbers
    }

    #Write to file to puzzles folder
    with open(f"{fileName}", "w") as file:
        json.dump(jsonObject, file, indent=4)
        print(f"File {fileName} has been created")
        file.close()
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))