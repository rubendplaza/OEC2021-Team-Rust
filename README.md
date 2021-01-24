---
title: 'User Document:'
created: '2021-01-24T00:27:48.258Z'
modified: '2021-01-24T00:50:23.950Z'
---

# User Document:

## Required to run:

- Python Version 3
- pip package manager

## To install and run:
1) Download the github repository
2) Within the repository’s directory run following commands from your terminal: ensure python and pip are installled correctly (the version # should be returned)
```$ python --version```
```$ pip --version```
3) install the openpyxl package (for parsing the input from the .xlsx file)
```$ pip install openpyxl```
4) Now you are able to run the program
```$ python3 main.py``` 

# Developer Document:

## Key Components:

### Libraries and packages used: csv, openpyxl

The program is split in between three major parts. We have the parser, the infection checker, and the data processor. The parser takes the school records that were provided and inputs them into dictionaries. The infection checker attempts at simulating the spread of ZBY1 among the school. We took into account all locations that students or teachers that are confirmed to have ZBY1 and determined a probability of whether a teacher or student has ZBY1 as well as who they have been infected by. Then come in our data processor where we made our correlations and exported the data into a readable format.

