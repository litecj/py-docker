import pandas as pd


class Weather (object):

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
        ls2 = ['한림읍','애월읍','구좌읍', '조천읍','한경면','추자면','우도면','일도1동','일도2동','이도1동','이도2동','삼도1동',
               '삼도2동','용담1동','용담2동','건입동','화북동','삼양동','봉개동','아라동','오라동','연동','노형동','외도동','이호동','도두동']
        ls3 = ['대정읍/마라도포함','남원읍','성산읍','안덕면','표선면','송산동','정방동','중앙동','천지동','효돈동','영천동','동홍동','서홍동','대륜동','대천동','중문동','예래동']
        ls4 = ['202101', '202102','202103','202104','202105','202106','202107','202012','202011','202010']
        for j in ls2:
            name = j
            for i in ls:
                print(name)
                test1 = pd.read_csv(f'../data/weather/{name}_{i}_202101_202107.csv', encoding='UTF-8')
                test2 = pd.DataFrame(test1, columns = test1.keys())
                if i == '기온':
                    test3.append(test2)
                else:
                    test3.append(test2.iloc[:, [2]])
            result = pd.concat(test3, axis=1)
            print(result)
            result.to_csv(f'../data/제주시_{name}_날씨.csv', sep=',', na_rep='NaN')

        # data_a = pd.read_csv('../data/weather/한림읍_기온_202101_202107.csv', encoding='UTF-8')
        # self.df_a = pd.DataFrame(data_a, columns = data_a.keys())
        # data_b = pd.read_csv('../data/weather/한림읍_강수_202101_202107.csv', encoding='UTF-8')
        # self.df_b = pd.DataFrame(data_b, columns = data_b.keys())
        # self.df_b = data_b.iloc[:, [2]]
        # data_c = pd.read_csv('../data/weather/한림읍_강수형태_202101_202107.csv', encoding='UTF-8')
        # self.df_c = pd.DataFrame(data_c, columns= data_c.keys())
        # self.df_c = data_c.iloc[:, [2]]
        # data_d = pd.read_csv('../data/weather/한림읍_습도_202101_202107.csv', encoding='UTF-8')
        # self.df_d = pd.DataFrame(data_d, columns=data_d.keys())
        # self.df_d = data_d.iloc[:, [2]]
        # data_e = pd.read_csv('../data/weather/한림읍_풍속_202101_202107.csv', encoding='UTF-8')
        # self.df_e = pd.DataFrame(data_e, columns=data_e.keys())
        # self.df_e = data_e.iloc[:, [2]]
        # data_f = pd.read_csv('../data/weather/한림읍_풍향_202101_202107.csv', encoding='UTF-8')
        # self.df_f = pd.DataFrame(data_f, columns=data_f.keys())
        # self.df_f = data_f.iloc[:, [2]]
        # data_g = pd.read_csv('../data/weather/한림읍_하늘상태_202101_202107.csv', encoding='UTF-8')
        # self.df_g = pd.DataFrame(data_g, columns=data_g.keys())
        # self.df_g = data_g.iloc[:, [2]]
        # data_i = pd.read_csv('../data/weather/한림읍_뇌전_202101_202107.csv', encoding='UTF-8')
        # self.df_i = pd.DataFrame(data_i, columns=data_i.keys())
        # self.df_i = data_i.iloc[:, [2]]
        # # result = pd.merge(self.df_a, self.df_b, self.df_c, self.df_d, self.df_e, self.df_f, self.df_g, self.df_h, self.df_i, on= "day", how="right")
        # # print(self.df_b)
        # result = pd.concat([self.df_a, self.df_b, self.df_c, self.df_d, self.df_e, self.df_f, self.df_g, self.df_h, self.df_i], axis = 1)
        # print(result)
        # print(type(self.df_b))
        # for i in result:
        #     self.df = self.df.drop(['day'],['hour'],axis=1)



    # def data_merge(self):
    #     # frames = [self.df_a, self.df_b, self.df_c, self.df_d, self.df_e, self.df_f, self.df_g, self.df_h, self.df_i]
    #     result = pd.concat([self.df_a, self.df_b], axis = 1)
    #     # result = pd.merge(self.df_a, self.df_b)

        # print(result.head(3))

    def drop_feature(self, *feature)-> object:
        for i in feature:
            self.df = self.df.drop([i],axis=1)
        return self.df