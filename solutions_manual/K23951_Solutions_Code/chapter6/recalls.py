#!/usr/bin/env python3

def printProducts():
    url = 'http://www.fda.gov/DataSets/Recalls/RecallsDataSet.xml'
    webpage = web.urlopen(url)
    
    line = ''
    while line[:14] != '<RECALLS_DATA>':   # read past headers
        line = webpage.readline()
        line = line.decode('utf-8')
    
    productNum = 1
    line = webpage.readline()              # read first <PRODUCT> line
    line = line.decode('utf-8')
    while line[:15] != '</RECALLS_DATA>':  # while more products
        print(productNum)
        while line[:10] != '</PRODUCT>':   # print one product element
            print(line.rstrip())
            line = webpage.readline()
            line = line.decode('utf-8')
        print(line.rstrip())
        productNum = productNum + 1
        line = webpage.readline()          # read next <PRODUCT> line
        line = line.decode('utf-8')   
               
    webpage.close()
