# Weekly Assignment 04. github.py
# The aim of this program is to write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with my name "Laura" and write the file back to the repository.
# Author: Laura Lyons

import requests
from github import Github
from config import config as cfg

api_key = cfg["WSAA-assignments"]

def replace_text_in_file():
    try:
        g = Github(api_key)
        repo = g.get_repo("Laura6826/WSAA-assignments")
        file_path = "data/assignment04laura.txt"
        
        # Check if the file already exists
        try:
            file_info = repo.get_contents(file_path)
            sha = file_info.sha
            file_exists = True
        except:
            sha = None
            file_exists = False

        # Fetch the original file content
        original_file_info = repo.get_contents("data/assignment04andrew.txt")
        url_of_file = original_file_info.download_url
        response = requests.get(url_of_file)
        content_of_file = response.text

        # Replace all instances of "Andrew" with "Laura" written in red
        new_contents = content_of_file.replace("Andrew", "<span style='color:red'>Laura</span>")
        print("Updated Contents:\n", new_contents)

        # Update or create the file with new contents
        if file_exists:
            gitHubResponse = repo.update_file(file_path, "Replaced 'Andrew' with 'Laura'", new_contents, sha)
        else:
            gitHubResponse = repo.create_file(file_path, "Created new file with 'Andrew' replaced by 'Laura'", new_contents)
        
        print("File operation successful:", gitHubResponse)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    replace_text_in_file()







