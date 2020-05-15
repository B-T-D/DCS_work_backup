import urllib.request as web

##url = 'http://www.fda.gov/DataSets/Recalls/RecallsDataSet.xml'
##url = 'https://www.fda.gov/about-fda/open-government-fda-data-sets/recalls-data-sets'
url = 'https://www.fda.gov/media/124800/download' # xml with content the book had in mind
webpage = web.urlopen(url)
for i in range(20):
    line = webpage.readline()
    print(line.decode('utf-8'))

##line = ''
##while line[:14] != '<RECALLS_DATA>':
##    line = webpage.readline()
##    line = line.decode('utf-8')
##    print(line)
