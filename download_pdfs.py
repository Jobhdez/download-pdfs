import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url")
parser.add_argument("folder")

args = parser.parse_args()

def downloads_pdfs(url, folder):
    
    if not os.path.exists(folder):os.mkdir(folder)
        
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    for link in soup.select("a[href$='.pdf']"):
        filename = os.path.join(folder, link['href'].split('/')[-1])
        
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)

    print("download complete!")

downloads_pdfs(args.url, args.folder)


