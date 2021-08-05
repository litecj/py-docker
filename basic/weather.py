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
        data_c = pd.read_csv('../data/한림읍_강수형태_202101_202107.csv',encoding='UTF-8')
        self.df_c = pd.DataFrame(data_c, columns= data_c.keys())
        data_d = pd.read_csv('../data/한림읍_습도_202101_202107.csv',encoding='UTF-8')
        self.df_d = pd.DataFrame(data_d, columns=data_d.keys())
        data_e = pd.read_csv('../data/한림읍_풍속_202101_202107.csv',encoding='UTF-8')
        self.df_e = pd.DataFrame(data_e, columns=data_e.keys())
        data_f = pd.read_csv('../data/한림읍_풍향_202101_202107.csv',encoding='UTF-8')
        self.df_f = pd.DataFrame(data_f, columns=data_f.keys())
        data_g = pd.read_csv('../data/한림읍_하늘상태_202101_202107.csv',encoding='UTF-8')
        self.df_g = pd.DataFrame(data_g, columns=data_g.keys())
        data_i = pd.read_csv('../data/한림읍_뇌전_202101_202107.csv',encoding='UTF-8')
        self.df_i = pd.DataFrame(data_i, columns=data_i.keys())

        # result = pd.merge(self.df_a, self.df_b, self.df_c, self.df_d, self.df_e, self.df_f, self.df_g, self.df_h, self.df_i, on= "day", how="right")
        # print(self.df_b)
        result = pd.concat([self.df_a, self.df_b, self.df_c, self.df_d, self.df_e, self.df_f, self.df_g, self.df_h, self.df_i], axis = 1)
        print(result.head(3))
        # print(type(self.df_b))

    def data_merge(self):
        # frames = [self.df_a, self.df_b, self.df_c, self.df_d, self.df_e, self.df_f, self.df_g, self.df_h, self.df_i]
        result = pd.concat([self.df_a, self.df_b], axis = 1)
        # result = pd.merge(self.df_a, self.df_b)

        # print(result.head(3))