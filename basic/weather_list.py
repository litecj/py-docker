import pandas as pd


class WeatherList (object):

    df = None
    df_a = None
    df_b = None
    df_c = None
    df_d = None
    df_e = None
    df_f = None
    df_g = None
    df_h = None
    df_i = None

    def read_data(self):
        name = ''
        test1 = None
        test2 = None
        test3 = []
        result = None
        ls = ['기온', '강수', '강수형태', '습도', '풍속', '풍향', '하늘상태', '뇌전']
        ls2 = ['이도2동']
        ls4 = ['2021','2020','2019','2018']
        ls5 = ['01','02','03','04','05','06','07','08','09','10','11','12']
        for h in ls4:
            print('h : '+h)
            for a in ls5:
                print('\ta : '+a)
                for j in ls2:
                    print('\t\tj : '+j)
                    for i in ls:
                        imsi = str(f'../data/weather/{j}_{i}_{h}{a}_{h}{a}.csv')
                        print('\t\t\ti : '+imsi)
                        test1 = pd.read_csv(imsi, encoding='UTF-8')
                        test1 = test1.rename(columns={f'value location:53_38 Start : {h}{a}01 ': i})
                        test2 = pd.DataFrame(test1, columns = test1.keys())
                        test2.insert(0,'Year', h)
                        test2.insert(1, 'Month', a)
                        #test2 = test2.assign(Month=[a],Year=[h])
                        if i == '기온':
                            test3.append(test2)
                        else:
                            test3.append(test2.iloc[:, [4]])
                        # result = pd.concat(test3, axis=1)
                        # print(result)
                        # result.to_csv(f'../data/제주시_{h}_{a}_날씨.csv', sep=',', na_rep='NaN')


    def drop_feature(self, *feature)-> object:
        for i in feature:
            self.df = self.df.drop([i],axis=1)
        return self.df

    def change_index(self):
        test1 = None
        test2 = None
        ls = ['기온', '강수', '강수형태', '습도', '풍속', '풍향', '하늘상태', '뇌전']
        ls2 = ['이도2동', '서홍동']
        ls4 = ['2021', '2020', '2019', '2018']
        ls5 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
