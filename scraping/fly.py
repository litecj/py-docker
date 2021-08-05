import pandas as pd
import requests
from bs4 import BeautifulSoup

from common.menu import print_menu


class Fly(object):
    domain = ''
    query_string = ''
    html = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    tag_name = ''
    fname = ''
    artists = []
    titles = []
    dict = {}
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        #print(f'Crawling HTML is {self.html}')

    def get_raking(self):
        soup = BeautifulSoup(self.html, 'lxml')
        n_ = 0
        ls = soup.find_all(name='div', attrs={'class': 'serch-area-btn accordionsecond-tit'}, )

        ls2 = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[1]})
        print(f'List size is {len(ls)}')
        for i, j in zip(ls,ls2):
            n_ += 1
            self.artists.append(i.find('a').text)
            self.titles.append(j.find('a').text)
            print( i.find('a').text, j.find('a').text)

    def insert_dict(self):
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j

        print(self.dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')



def main():
    mr = Fly()
    while 1:
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', 'Output',
                           'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV' ])
        if menu == 0:
            break
        elif menu == 1:
            mr.domain = 'https://www.weather.go.kr/w/index.do#'
            mr.set_html()
        elif menu == 2:
            pass
        elif menu == 3:
            music = input('1.bugs, 2.melon')
            if music == '2':
                mr.fname = 'jejudo_jejusi'
                mr.tag_name = 'div'
                mr.class_name.append('ellipsis rank02')
                mr.class_name.append('ellipsis rank01')
                mr.get_raking()
            elif music == '1':
                mr.fname = 'bugs'
                mr.tag_name ='p'
                mr.class_name.append('artist')
                mr.class_name.append('title')
                mr.get_raking()
        elif menu == 4:
            mr.insert_dict()
        elif menu == 5:
            mr.dict_to_dataframe()
        elif menu == 6:
            mr.df_to_csv()



if __name__ == '__main__':
    main()