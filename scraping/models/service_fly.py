import pandas as pd

from scraping.models.dataset_fly import DatasetFly


class ServiceFly (object) :

    dataset = DatasetFly
    def model(self,payload):
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context+this.fname)