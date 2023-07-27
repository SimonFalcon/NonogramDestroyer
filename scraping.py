from bs4 import BeautifulSoup
import requests

#Requesting HTML from the website
linkNano = "https://onlinenonograms.com/12"
requestHTML = requests.get(linkNano)
soup = BeautifulSoup(requestHTML.content, 'html5lib') 

# Defining variables
puzzleDimensions = {
    'width': int,
    'height': int
}
extractedColumnNumbers = []
extractedRowNumbers = []
columnNumbers = []
rowNumbers = []

# Extracting Puzzle Dimensions
extractDimensions = soup.find('img', attrs = {'title':'Nonogram size'})   
dim = extractDimensions.next_sibling
dim = dim.strip()
partitions = dim.split('x')
puzzleDimensions['width'] = int(partitions[0])
puzzleDimensions['height'] = int(partitions[1])   
print(puzzleDimensions)        


# Extracting Column and Row numbers
columnTable = soup.find('table', attrs = {'id':'cross_top'})
rowTable = soup.find('table', attrs = {'id':'cross_left'})

def extractNumbers(inputTable, numbersTable):
    for row in inputTable.findAll('tr'):
        for cell in row.findAll('td'):
                numbersTable.append(cell.text)

extractNumbers(columnTable, extractedColumnNumbers)
extractNumbers(rowTable, extractedRowNumbers)
print(extractedColumnNumbers)
print(extractedRowNumbers)

# Splitting the lists into chunks
def splitNumberLists(inputList, splitBy):
    for i in range(0, len(inputList), splitBy):
        yield inputList[i:i + splitBy]


columnNumbers = list(splitNumberLists(extractedColumnNumbers, puzzleDimensions['width']))
print(columnNumbers)
rowNumbers = list(splitNumberLists(extractedRowNumbers, puzzleDimensions['height']))
print(rowNumbers)


