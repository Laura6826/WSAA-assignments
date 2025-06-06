# Web Services and Applications 24-25: 8640

## Assignments submitted as part of the module Web Services and Applications 24-25: 8640, Higher Diploma in Science, Data Analytics

## *Author: Laura Lyons*

***

This README file was written using the [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) as a guidance document
***

  &#x26a0;&#xfe0f; **DISCLAIMER**

  Microsoft Co-Pilot was used to generate ideas of the content of the following notebook. That said, the notebook is mainly my own work, as I had to re-work the code the text in generated to meet my own needs (*The warning icon was sourced from [Stackoverflow](https://stackoverflow.com/questions/50544499/how-to-make-a-styled-markdown-admonition-box-in-a-github-gist)*).

## **Table of contents**

1. [Introduction.](#1-introduction).
1. [The purpose of this module.](#2-the-purpose-of-this-module)
1. [How to get started.](#3-how-to-get-started)
1. [How to get help.](#4-how-to-get-help)
1. [How to contribute.](#5-how-to-contribute)
1. [Weekly Assignment.](#6-weekly-assignments)

    1. [Assignment 02- Card Draw](#assignment-02---card-draw)
    1. [Assignment 03- CSO](#assignment-03---cso)
    1. [Assignment 04- github authentication](#assignment-04---githubpy)

## 1. Introduction

This README was created to fulfill an assessment requirement of Web Services and Applications 24-25: 8640, as part of the H.Dip in Science in Data Analytics.

Each week, following a series of lectures, an assignment was set, to demonstrate both learning and additional reading/research on the topics discussed in the lectures.

This repository is a collection of my weekly assignments, including some additional guidance and instruction on how to run each assignment/program.

***

## 2. The purpose of this module

As noted on the [module introduction](https://vlegalwaymayo.atu.ie/course/view.php?id=12365),

- Introduce various means of retrieving data from external sources (for example CSO, weather servers, stock information).
- The module will look at the formats that data can come in (XML, JSON,CSV).
- How to retrieve (through an API) and process that data, using JavaScript and Python.
- Explore how to make your data available to the outside world by creating an API (Application Programmer's Interface) using the python module Flask.

## 3. How to get started

### Necessary software

In order to run the included files, you will need to ensure that you have access to the correct software. I would recommend downloading the following applications (ensuring sufficient space on your hard drive prior to installation):

1. [Anaconda](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf) (if Anaconda is too large, miniconda would also suffice).
2. [Visual Studio Code](https://code.visualstudio.com/Download) (this is a code editor).

### **Additions to** *.gitignore*

A number of [additional files](https://github.com/github/gitignore/tree/main/Global) were added to my .gitignore prior to running the programmes:

  1. python.gitignore
  2. macOS..gitignore
  3. VisualStudioCode.gitignore
  4. Linux.gitignore
  5. TeX.gitignore
  6. Vim.gitignore
  7. Windows.gitignore

## How to run these files

### Using Visual Studio Code & Anaconda or GitHub Codespaces

**Clone the Repository**:

```ruby
   git clone https://github.com/Laura6826/WSAA-assignments
```

**Install the required packages**:

For a seamless executition, I would also recommend you have access to the below libraries prior to running the files. The libraries required to run this file (as noted below), can be installed with the following code:

```ruby
pip install -r requirements.txt
```

,or you can manually install each of the libraries below.+

```ruby
import os
import json
import requests
from github import Github
from config import config as cfg
```

***

### Open the notebook in Visual Studio Code

- Open Visual Studio Code.
- Open the `computer_infrastructure_assignments` folder.
- Open the folder associated with the assignment you wish to look at.

## 4. How to get help

I have attached below, a number of helpful links, should you wish to extrapolate on any of the methods used within this project.

1. [Anaconda](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf)
1. [Visual Studio Code](https://code.visualstudio.com/Download)
1. [w3schools](https://www.w3schools.com/)

## 5. How to contribute

As this project was created to fulfil an assessment requirement of the Web Services and Applications 24-25: 8640, as part of the H.Dip in Science in Data Analytics, no contributions will be allowed, in order to comply with ATU Policy on [Plagiarism](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf) and the [Student Code of Conduct](https://www.atu.ie/sites/default/files/2022-08/Student%20Code_Final_August_2022.pdf).

Should you find any errors or have any recommendations, please submit a pull request on GitHub. or just wish to contact that author, you can do so at <maxwell6826@gmail.com>.

***

## **6. Weekly Assignments**

## **Assignment 02** - Card Draw

**Assignment Instructions:**

Using the [Deck of Cards API](https://deckofcardsapi.com/),

1. Write a program that "deals" (prints out) 5 cards (get the deck_id)
1. Print the value and the suit of each card.

Last few marks:
Check if the user has drawn a pair, triple, straight, or all of the same suit and congratulate the user.

***

## **Assignment 03** - CSO

**Assignment Instructions:**

Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".

1. Upload this program to the same repository you used for the first assignment
1. Save this assignment as "assignment03-cso.py"

***

## **Assignment 04** - github.py  

**Assignment Instructions:**

1. Write a program in python that will read a file from a repository.
1. The program should then replace all the instances of the text "Andrew" with your name.
1. The program should then commit those changes and push the file back to the repository.

**My notes:**

Is it very import that no API keys are pushed to github, it is best practice to store the 'keys' in a 'config.py' file and called upon each time there are needed.

Its also essential that you add 'config.py' to your '.ignore' file, as this will ensure that this file is not pushed up to github.

The code was amended so that the new content would be saved to a new file ad

***

### End.
