"""
Extract a dataset from a URL
"""
import requests

def extract(url="https://raw.githubusercontent.com/laxmimerit/All-CSV-ML-Data-Files-Download/master/IMDB-Movie-Data.csv",\
            file_path="/workspaces/sqlite-lab-mcg/master/IMDB-Movie-Data.csv"):
    """Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



