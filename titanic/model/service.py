import numpy as np
import pandas as pd

from titanic.model.dataset import Dataset
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier

class TitanicService(object):

    dataset = Dataset()

    def new_model(self,payload) -> object:
        # this = self.dataset
        # this.context = '/app/'
        # this.fname = payload
        return pd.read_csv(f"/data/{payload}.csv")


    def count_survived_dead(self, ):
        return []

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this)-> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature)-> object:
        for i in feature:
            this.train = this.train.drop([i],axis=1)
            this.test = this.test.drop([i],axis=1)
        return this
    # PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    # nominal / ordinal  : embarked, title
    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        this.train['Embarked']= this.train['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['Fare'] = this.train['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, labels={1,2,3,4})
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1,2,3,4})
        return this
        '''bins = [-1, 8, 15, 31, np.inf]
        this.train = this.train.drop(['Fare'])
        this.test = this.test.drop(['Fare'])'''
        # qcut() 사용 시, 자동으로 구간 등분 / titanic에서 bins = [-1, 8, 15, 31, np.inf]로 구분 됨.


    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown','Baby','Child','Teenager','Student','Young Adult','Adult', 'Senior']
        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        test['AgeGroup'] = pd.cut(test['Age'], bins, labels=labels)
        age_title_mapping = {0:'Unknown', 1:'Baby', 2:'Child', 3:'Teenager', 4:'Student', 5:'Young Adult', 6:'Adult', 7:'Senior'}
        for i in range(len(train['AgeGroup'])):
            if train['AgeGroup'][i] == 'Unknown':
                train['AgeGroup'][i] = age_title_mapping[train['Title'][i]]
        for i in range(len(test['AgeGroup'])):
            if test['AgeGroup'][i] == 'Unknown':
                test['AgeGroup'][i] = age_title_mapping[test['Title'][i]]
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6,'Senior': 7}
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        this.train = this.train
        this.test = this.test
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer','Dona', 'Mme'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mile', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Mater': 4, 'Royal': 5, 'Rare': 6}
        for dataset in combine:
            dataset['Title'] = dataset['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0)
        this.train = this.train
        this.test = this.test
        return this

    @staticmethod
    def gender_nominal(this) -> object:
        combine = [this.train, this.test]
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Gender'] = dataset['Sex'].map(sex_mapping)
        this.train = this.train
        this.test = this.test
        return this


    def create_k_fold(self):
        return None

    def accuracy_by_classfier(self):
        return None
