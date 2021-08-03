import pandas as pd


from sklearn.ensemble import RandomForestClassifier

from titanic_3.model.dataset import Dataset
from titanic_3.model.service import TitanicService


class TitanicView(object):
    dataset = Dataset()
    service = TitanicService()

    def modeling(self):
        this = self.preprocessing()
        self.learning(this)
        return this

    def preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        this.id = this.test['PassengerId']
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.age_ordinal(this)
        this = service.gender_nominal(this)
        this = service.fare_ordinal(this)
        this = service.drop_feature(this, 'Name','Cabin', 'Sex', 'Fare', 'Age', 'SibSp', 'Ticket', 'Parch')
        # self.print_this(this)
        return this

    def learning(self,this):
        print(f'SKLearn Algorithmic Accuracy is : {self.service.accuracy_by_classfier(this)}')

    def submit(self):
        this = self.modeling()
        clf = RandomForestClassifier()
        clf.fit(this.train, this.test)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived':prediction}).to_csv('/data/submission.csv',index=False)

    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'1-1.Type Of Train is{type(this.train)},\n1-2.Type Of Test is{type(this.test)}')
        print(f'2-1.Columns Of Train is{this.train.columns},\n2-2.Columns Of Test is{this.test.columns}')
        print(f'3-1.Top Row Of Train is{this.train.head(3)},\n3-2.Top Row Of Test is{this.test.head(3)}')
        print(f'4-1.Null Count Of Train is{this.train.isnull().sum()},'
              f'\n4-2.Null Count Of Test is{this.test.isnull().sum()}')
