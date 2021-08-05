from scraping.models.dataset_fly import DatasetFly
from scraping.models.service_fly import ServiceFly


class View (object):
    dataset = DatasetFly()
    service = ServiceFly()

    def modeling(self,fly):
        service = self.service
        this = self.preprocessing(fly)
        print(f'The Type of This is {type(this.fly)}')
        print(f'The head of weather is\n{this.fly.head(3)}')

    def preprocessing(self, fly) -> object:
        service = self.service
        this = self.dataset
        this.weather = service.model(fly)
        return this


if __name__ == '__main__':
    view = View()
    view.modeling('fly.csv')