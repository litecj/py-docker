import pandas as pd

from titanic.model.dataset import Dataset

class TitanicService(object):

    dataset = Dataset()

    def new_model(self,payload) -> object:
        # this = self.dataset
        # this.context = '/app/'
        # this.fname = payload
        return pd.read_csv(f"/data/{payload}.csv")

    def count_survived_dead(self, ):
        return []

    def create_train(self):
        return None

    def create_label(self):
        return None

    def drop_feature(self, *feature):
        return None

    def embarked_nominal(self):
        return None

    def fare_oridnal(self):
        return None

    def title_nominal(self):
        return None

    def gender_norminal(self):
        return None

    def age_ordinal(self):
        return None

    def create_k_fold(self):
        return None

    def accuracy_by_classfier(self):
        return None
