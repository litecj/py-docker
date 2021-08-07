import re
import time
from urllib.parse import urljoin, urlparse
from os import makedirs
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


def enum_links(html, base):
    soup = BeautifulSoup(html,"html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    result = []
    for a in links:
        href = a.attrs['href']
        url = urljoin(base,href)
        result.append(url)
    return result
def download_file(url):
    o = urlparse(url)
    savepath = "./"+o.netloc + o.path
    if re.search(r"/$",savepath):
        savepath+= "index.html"
    savedir = os.path.dirname(savepath)
    if os.path.exists(savepath): return savepath
    if not os.path.exists(savedir):
        print("mkdir+",savedir)
        makedirs(savedir)
    try:
        print("download=",url)
        urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print("다운 실패 : ", url)
        return None