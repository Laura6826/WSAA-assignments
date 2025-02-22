# Weekly Assignment 03. cso.py
# The aim of this program is to write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".
# Author: Laura Lyons

import requests
import json

# url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
# response = requests.get(url)
# data = response.json()

urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)
    
if __name__ == "__main__":
    getAllAsFile("FIQ02")

print("Dataset has been saved to 'cso.json'")