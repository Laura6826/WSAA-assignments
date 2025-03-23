# Weekly Assignment 03. cso.py
# The aim of this program is to write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".
# Author: Laura Lyons

import os
import json
import requests

# url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
# response = requests.get(url)
# data = response.json()

# Define the base URLs
urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

# Function to fetch the dataset
def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# Function to save the file into the 'data' folder
def getAllAsFile(dataset):
    # Ensure the 'data' folder exists
    os.makedirs("data", exist_ok=True)
    
    # Save the file in the 'data' folder
    file_path = os.path.join("data", "cso.json")
    with open(file_path, "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

    print(f"Dataset has been saved to '{file_path}'")

# Main execution
if __name__ == "__main__":
    getAllAsFile("FIQ02")
