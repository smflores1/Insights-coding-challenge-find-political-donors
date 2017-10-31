# Insights-coding-challenge-find-political-donors
This repository contains my response to the Insights Data Engineering coding challenge, found at https://github.com/InsightDataScience/find-political-donors.

# Table of Contents
1. [Author](README.md#summary)
2. [Summary](README.md#summary)
3. [What find_political_donors.py does](README.md#what-find_political_donors.py-does)
4. [How to use find_political_donors.py](README.md#how-to-use-find_political_donors.py)
5. [How find_policitcal_donors.py works](README.md#how-find_political_donors.py-works)
6. [Testing find_political_donors.py](README.md#testing-find_political_donors.py)

# Author

Steven Flores

# Summary

This is the readme for find_political_donors.py, a python script that answers the coding challenge posted at https://github.com/InsightDataScience/find-political-donors.

# What find_political_donors.py does

A thorouhg description of what find_political_donors.py does may be found at https://github.com/InsightDataScience/find-political-donors.

# How to use find_political_donors.py

In this section, we explain how to use find_political_donors.py.

### File tree structure

Create the following file tree structure inside a directory with any name, labeled 'X' below:

### File tree structure

Create the following file tree structure inside a directory with any name, labeled 'X' below:

    X
    ├── input
    │   └── itcont.txt
    ├── output
    ├── run.sh
    ├── src
        └── find_political_donors.py

The file itcont.txt can be any file found at http://classic.fec.gov/finance/disclosure/ftpdet.shtml#a2017_2018 under "Contributions from Individuals." (Use any file beginning with the prefix "itcont" and ending with .txt.) It is a text file where each line has 21 pipe-delimited fields, described at http://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml

An very small example of the itcont.txt file may be downloaded at https://github.com/InsightDataScience/find-political-donors too.

### Run instructions

To run find_political_donors.py from the terminal, make X your present working directory, and then type the following into the command line:

python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

Alternatively, make X your present working directory, and run the shell script run.sh by typing the following into the command line:

./run.sh

