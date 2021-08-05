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
        data_a = pd.read_csv('../data/한림읍_기온_202101_202107.csv',encoding='UTF-8')
        self.df_a = pd.DataFrame(data_a, columns = data_a.keys())
        data_b = pd.read_csv('../data/한림읍_강수_202101_202107.csv',encoding='UTF-8')
        self.df_b = pd.DataFrame(data_b, columns = data_b.keys())
        self.df_b = data_b.iloc[:, [2]]
        data_c = pd.read_csv('../data/한림읍_강수형태_202101_202107.csv',encoding='UTF-8')
        self.df_c = pd.DataFrame(data_c, columns= data_c.keys())
        self.df_c = data_c.iloc[:, [2]]
        data_d = pd.read_csv('../data/한림읍_습도_202101_202107.csv',encoding='UTF-8')
        self.df_d = pd.DataFrame(data_d, columns=data_d.keys())
        self.df_d = data_d.iloc[:, [2]]
        data_e = pd.read_csv('../data/한림읍_풍속_202101_202107.csv',encoding='UTF-8')
        self.df_e = pd.DataFrame(data_e, columns=data_e.keys())
        self.df_e = data_e.iloc[:, [2]]
        data_f = pd.read_csv('../data/한림읍_풍향_202101_202107.csv',encoding='UTF-8')
        self.df_f = pd.DataFrame(data_f, columns=data_f.keys())
        self.df_f = data_f.iloc[:, [2]]
        data_g = pd.read_csv('../data/한림읍_하늘상태_202101_202107.csv',encoding='UTF-8')
        self.df_g = pd.DataFrame(data_g, columns=data_g.keys())
        self.df_g = data_g.iloc[:, [2]]
        data_i = pd.read_csv('../data/한림읍_뇌전_202101_202107.csv',encoding='UTF-8')
        self.df_i = pd.DataFrame(data_i, columns=data_i.keys())
        self.df_i = data_i.iloc[:, [2]]
        # result = pd.merge(self.df_a, self.df_b, self.df_c, self.df_d, self.df_e, self.df_f, self.df_g, self.df_h, self.df_i, on= "day", how="right")
        # print(self.df_b)
        result = pd.concat([self.df_a, self.df_b, self.df_c, self.df_d, self.df_e, self.df_f, self.df_g, self.df_h, self.df_i], axis = 1)
        print(result)
        result.to_csv('../data/제주도_한림읍_날씨.csv', sep=',', na_rep='NaN')
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