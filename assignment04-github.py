# Weekly Assignment 04. github.py
# The aim of this program is to write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with my name "Laura" and write the file back to the repository.
# Author: Laura Lyons

from github import Github
import requests
from config import config as cfg
'''
apikey = cfg["githubkey"]

def replace_text_in_file():
    try:
        g = Github(apikey)
        repo = g.get_repo("Laura6826/wsaa_test")
        fileInfo = repo.get_contents("test.txt")
        urlOfFile = fileInfo.download_url
        response = requests.get(urlOfFile)
        contentOfFile = response.text

        # Replace all instances of "Andrew" with "Laura"
        newContents = contentOfFile.replace("Andrew", "Laura")
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
import os
from config import config as cfg

def fetch_file_from_github(repo, filepath, branch="main", token=None):
    url = f"https://raw.githubusercontent.com/{repo}/{branch}/{filepath}"
    headers = {'Authorization': f'token {token}'} if token else None
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching file: {e}")
        return None

def replace_text_and_save(content, old_text, new_text, output_filepath):
    try:
        modified_content = content.replace(old_text, new_text)
        with open(output_filepath, "wt") as fp:
            fp.write(modified_content)
        print(f"File has been saved to '{output_filepath}'")
    except IOError as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    # Prompt the user to enter the repository name, file path, and branch name
    repo = input("Enter the repository name (e.g., username/repository): ")
    filepath = input("Enter the file path within the repository: ")
    branch = input("Enter the branch name (default is 'main'): ") or "main"
    
    # Get the GitHub API token from the config file
    token = cfg["github_token"]
    output_filepath = "data/modified_file.txt"
    
    # Fetch the file content from GitHub
    content = fetch_file_from_github(repo, filepath, branch, token)
    
    if content:
        # Replace all instances of "Andrew" with "Laura" and save the modified content
        replace_text_and_save(content, "Andrew", "Laura", output_filepath)
    else:
        print("Failed to retrieve file.")



