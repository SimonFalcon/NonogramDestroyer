from bs4 import BeautifulSoup
import requests

linkNano = "https://onlinenonograms.com/12"
requestHTML = requests.get(linkNano)
soup = BeautifulSoup(requestHTML.content, 'html5lib') 

puzzleDimensions = {
    'width': int,
    'height': int
}
columnNumbers = []
rowNumbers = []

# Extracting Column and Row numbers
columnTable = soup.find('table', attrs = {'id':'cross_top'})
rowTable = soup.find('table', attrs = {'id':'cross_left'})

def extractNumbers(inputTable, numbersTable):
    for row in inputTable.findAll('tr'):
        for cell in row.findAll('td'):
            numbersTable.append(cell.text)

extractNumbers(columnTable, columnNumbers)
extractNumbers(rowTable, rowNumbers)
print(columnNumbers)
print(rowNumbers)

# Extracting Puzzle Dimensions
extractDimensions = soup.find('img', attrs = {'title':'Nonogram size'})   
dim = extractDimensions.next_sibling
dim = dim.strip()
partitions = dim.split('x')
puzzleDimensions['width'] = int(partitions[0])
puzzleDimensions['height'] = int(partitions[1])   
print(puzzleDimensions)        

