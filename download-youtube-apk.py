#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup

def download_file(url, filename):
    with requests.get(url, headers=HEADERS, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

BASE_URL = 'https://www.apkmirror.com'
HEADERS = {
    'User-Agent': 'banana'
}

filename = sys.argv[1]
version = sys.argv[2].replace('.', '-')

page_url = f'{BASE_URL}/apk/google-inc/youtube/youtube-{version}-release/youtube-{version}-android-apk-download/'
download_page_url = BASE_URL + BeautifulSoup(requests.get(page_url, headers=HEADERS).text, 'lxml').select_one('.downloadButton')['href']
apk_url = BASE_URL + BeautifulSoup(requests.get(download_page_url, headers=HEADERS).text, 'lxml').select_one('.notes a')['href']

download_file(apk_url, filename)

