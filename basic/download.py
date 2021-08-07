from bs4 import BeautifulSoup


def enum_links(html, base):
    soup = BeautifulSoup(html,"html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")