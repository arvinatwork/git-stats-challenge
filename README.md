# Git Stats Summarizer

Create a summary of Github repositories given in a python script.

Current output format: 
- CSV

## Python Version
Python 3+

## How to run
### Prepare
Create a python3 virtual environment or use python3 directly in the command line. 
`python3 -m venv venv && source venv/bin/activate`

### Install Requirements
`pip install -r requirements.txt`

### Run
`python git_summarizer.py [-h] repositories [repositories ...]`

e.g. 
`python git_summarizer.py facebook/react google/clusterfuzz`

### Help
Use `python git_summarizer.py -h` for help

## Output
Current output is in CSV format. But it can be easily extended to support other formats.