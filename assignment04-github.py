# Weekly Assignment 04. github.py
# The aim of this program is to write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with my name "Laura" and write the file back to the repository.
# Author: Laura Lyons
'''
from github import Github
import requests
from config import config as cfg

apikey = cfg["WSAA-assignments"]

def replace_text_in_file():
    try:
        g = Github(apikey)

        # Get the specific repository and print its clone URL
        repo = g.get_repo("Laura6826/WSAA-assignments")

        # Get the contents of the file
        fileInfo = repo.get_contents("data/assignment04andrew.txt")
        urlOfFile = fileInfo.download_url
        response = requests.get(urlOfFile)
        contentOfFile = response.text

        # Replace all instances of "Andrew" with "Laura", written in red
        newContents = contentOfFile.replace("Andrew", "<span style='color:red'>Laura</span>")
        print("Updated Contents:\n", newContents)

        # Update the file with new contents
        gitHubResponse = repo.update_file(fileInfo.path, "Replaced 'Andrew' with 'Laura'", newContents, fileInfo.sha)
        print("File updated successfully:", gitHubResponse)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    replace_text_in_file()
'''
from github import Github
import requests
from config import config as cfg

apikey = cfg["WSAA-assignments"]

def replace_text_in_file():
    try:
        g = Github(apikey)
        repo = g.get_repo("Laura6826/WSAA-assignments")
        fileInfo = repo.get_contents("data/assignment04andrew.txt")
        urlOfFile = fileInfo.download_url
        response = requests.get(urlOfFile)
        contentOfFile = response.text

        # Replace all instances of "Andrew" with "Laura" written in red
        newContents = contentOfFile.replace("Andrew", "<span style='color:red'>Laura</span>")
        print("Updated Contents:\n", newContents)

        # Save the new content to a separate file in the repository
        new_file_path = "data/assignment04andrew_modified.txt"  # Specify the new file path
        repo.create_file(new_file_path, "Created new file with 'Andrew' replaced by 'Laura'", newContents)
        print(f"New file created successfully at: {new_file_path}")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    replace_text_in_file()






