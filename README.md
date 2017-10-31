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

    X
    ├── input
    │   └── itcont.txt
    ├── output
    ├── run.sh
    └── src
        └── find_political_donors.py
        
### Input Data

The script find_political_donors.py accepts as input a text file generically titled "itcont.txt" via sys.argv. The input file itcont.txt can be any file found at http://classic.fec.gov/finance/disclosure/ftpdet.shtml#a2017_2018 under "Contributions from Individuals" and pertaining to political campaign contributions between the years 2010 -- 2018. (Use any file beginning with the prefix "itcont" and ending with ".txt".) It is a text file where each line has 21 pipe-delimited fields, described at http://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml.

An very small example of the itcont.txt file may be downloaded at https://github.com/InsightDataScience/find-political-donors too.

### Output Data

The script find_political_donors.py ouputs two text files, respectively titled "medianvals_by_zip.txt" and "medianvals_by_date.txt" and described at https://github.com/InsightDataScience/find-political-donors.

### Run instructions

To run find_political_donors.py from the terminal, make X your present working directory, and then type the following into the command line:

python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

Alternatively, make X your present working directory, and run the shell script "run.sh" by typing the following into the command line:

./run.sh

### Required libraries

The python script find_political_donors.py uses the following python libraries:

| Library       | Use           
| ------------- |:-------------
| datetime      | comparing timestamps           
| time          | tracking run time 
| sys           | argv for input/output      
| statistics    | computing the median of a list of numbers

# How find_political_donors.py works

In this section, we explain how find_political_donors.py works.  


### Global variables

There is really only one global variable in find_political_donors.py, called "stream_dic." It is a dictionary with key, value pairs as follows:

Keys: The recipients of the political campaign donation. This is given as the first element of each line, as a string split over '|', of the input file itcont.txt.

Values: A list of two sub-dictionaries. The keys of the first dictionary are zip codes, given by the 11th element of each line, as a string split over '|', of the input file itcont.txt. Its values are a list of all donation amounts made to date to the corresponding key (recipient) of stream_dic. The keys of the second dictionary are transaction dates, given by the 14th element of each line, as a string split over '|', of the input file itcont.txt. Its values are a list of all donation amounts made to date to the corresponding key (recipient) of stream_dic.

### Global functions

**my_round**: The argument is an floating point number. The output is the integer nearest to the argument, with the convention that we round half-integers up to their nearest integer. For example, 2.5 rounds up to 3. This function uses the built-in python function "round," which instead rounds half-integers to their nearest even number. For example, round(2.5) = 2. Because we instead want, for example, 2.5 to round up to 3, we use the function "my_round."

**check_zip_code_format**: The argument is a single string. The output is True if the string has length 5 and comprises positive integers, and it returns False if otherwise. The purpose of this function is to check that the input string has the format of a zip code. (A better function would simply check that a given string is among the finite list of all U.S. zip codes. We do this in the jupyter notebook included with this repo.)

**check_date_format**: The argument is a single string. The output is True if the string is a date of the form MMDDYYYY in the years 2010--2018.

### Step-by-step

The following is a step-by-step description of find_political_donors.py (for brevity, we leave out some details, such as line-skipping rules, already explained at https://github.com/InsightDataScience/find-political-donors):

**1.** find_political_donors.py reads the input file itcont.txt line by line. At the i:th line, it splits that line into a list of variables across the pipe delimiter '|'. It then identifies the 1st, 11th, 14th, and 16th elements of that list as the recipient id ("cmte_id"), the donor zip code ("zip_code"), the donation date ("transaction_dt"), and the donation amount ("transaction_amt") respectively. 

**2.** Next, find_political_donors.py updates the first subdictionary stream_dic[cmte_id][0] by appending transaction_amt to the list stream_dic[cmte_id][0][zip_code]. It also updates the second subdictionary stream_dic[cmte_id][1] by appending transaction_amt to the list stream_dic[cmte_id][1][transaction_dt].

**3.** Next, find_political_donors.py writes a new line to the output file medianvals_by_zip.txt. The format and content of this new line is described at https://github.com/InsightDataScience/find-political-donors).

**4.** After completing steps 1-3 for all lines in the input file, find_political_donors.py writes to the output file medianvals_by_date.txt. The format and content of this output is described at https://github.com/InsightDataScience/find-political-donors).

# Testing find_political_donors.py

Two tests of find_political_donors.py are included in the directory "insights_testsuite."  To use them, paste insights_testsuite into the directory containing all other files for this project.  If this directory is called "X," then the file tree structure of X is now

    X
    ├── input
    │   └── itcont.txt
    ├── output
    ├── run.sh
    ├── src
    |   └── find_political_donors.py
    └── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   └── output
            └── test_2
                ├── input
                │   └── itcont_2018_20170530_20170830_small.txt
                ├── output
                ├── run.sh
                └── src
                    └── find_political_donors.py
                    
In the above, both versions of find_political_donors.py are the same, but both versions of run.sh are not the same. For the latter, the only difference between the two versions is that the second version is altered so find_political_donors.py accepts the file "itcont_2018_20170530_20170830_small.txt" as input.

To perform the basic Insights test (described at https://github.com/InsightDataScience/find-political-donors) at the command line, change the present working directory to insight_testsuite and enter

./run_tests.sh

To try find_political_donors.py on a larger (1.4MB) input file, change the present working directory to test_2 and enter

./run.sh



