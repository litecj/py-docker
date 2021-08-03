from titanic.model.dataset import Dataset
from titanic.model.service import TitanicService


class TitanicView(object):
    dataset = Dataset()
    service = TitanicService()

    def modeling(self):
        this = self.preprocessing()
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
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'1.Type Of Train is{type(this.train)},\n Type Of Test is{type(this.test)}')
        print(f'2.Columns Of Train is{this.train.columns},\n Columns Of Test is{this.test.columns}')
        print(f'3.Top Row Of Train is{this.train.head(3)},\n Top Row Of Test is{this.test.head(3)}')
        print(f'4.Null Count Of Train is{this.train.isnull().sum()},'
              f'\nNull Count Of Test is{this.test.isnull().sum()}')

