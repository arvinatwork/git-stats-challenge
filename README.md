# Git Stats Summarizer

Create a summary of Github repositories given in a python script.

Current output format: 
- CSV

## How to run
### Prepare
Create a python 3 virtual environment or use `python3` directly. 

```bash
python3 -m venv venv && source venv/bin/activate
```

### Install Requirements
```bash
pip install -r requirements.txt
```

### Run
```bash
python git_summarizer.py [-h] repositories [repositories ...]
```

e.g. 
```bash
python git_summarizer.py facebook/react google/clusterfuzz
```

### Help
Use `python git_summarizer.py -h` for help

## Output
Current output is in CSV format. But it can be easily extended to support other formats.

## Python Version
Python 3+
