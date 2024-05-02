import random
from datetime import datetime


class Article:
    def __init__(self, feed_type: str, text: str):
        self.feed_type = feed_type
        self.text = text


class News(Article):
    def __init__(self, feed_type, text, city):
        Article.__init__(self, feed_type=feed_type, text=text)
        self.city = city
        self.date = self.calculate_publish_date()

    def calculate_publish_date(self):
        current_date = datetime.now()
        formatted_date = current_date.strftime('%Y-%m-%d %H:%M-%S')
        return formatted_date


class Advertising(Article):
    def __init__(self, feed_type, text, expiration_date):
        Article.__init__(self, feed_type=feed_type, text=text)
        self.expiration_date = expiration_date
        self.days_left = self.calculate_days_left()

    def calculate_days_left(self):
        current_date = datetime.now().date()
        exp_date = datetime.strptime(self.expiration_date, "%Y-%m-%d").date()
        if exp_date < current_date:
            expired_string = "expired 0"
            return expired_string
        else:
            delta = exp_date - current_date
            return delta.days


class WeatherForecast(Article):
    def __init__(self, feed_type, text, region):
        Article.__init__(self, feed_type=feed_type, text=text)
        self.region = region
        self.is_weather_fine_tomorrow = self.forecast_weather_for_tomorrow()

    def forecast_weather_for_tomorrow(self):
        forecast = random.choices([True, False])[0]
        return f'The weather will be fine tomorrow: {forecast}'


class ArticleCreator():

    def generate_article(self):
        feed_type = self.input_feed_type()
        text = self.input_text()

        if feed_type == "news" or feed_type == "1":
            city = self.input_city()
            return News("news", text, city)

        elif feed_type == "advertising" or feed_type == "2":
            expiration_date = self.input_expiration_date()
            return Advertising("advertising", text, expiration_date)

        elif feed_type == "weather forecast" or feed_type == "3":
            region = self.input_region()
            return WeatherForecast("weather forecast", text, region)

    def input_feed_type(self):
        return input("Enter feed type: ")

    def input_text(self):
        return input("Enter text: ")

    def input_city(self):
        return input("Enter city: ")

    def input_expiration_date(self):
        return input("Enter expiration date: ")

    def input_region(self):
        return input("Enter region: ")


class Publisher():

    def __init__(self, article):
        self.article = article
        self.__file_name = ""

    def get_file_name(self):
        return self.__file_name

    def set_file_name(self, value):
        self.__file_name = value

    def publish_article(self):
        publication = ""
        for field in self.article.__dict__:
            if field == "feed_type":
                publication = (f"{article.__getattribute__(field)}----------------\n")
            elif field == "city":
                publication += (f"{article.__getattribute__(field)},")
            elif field == "expiration_date":
                publication += (f"Actual until: {article.__getattribute__(field)},")
            elif field == "days_left":
                publication += (f" {article.__getattribute__(field)} days left\n")
            else:
                publication += (f"{article.__getattribute__(field)}\n")
        publication += "\n"
        self.__write_to_file(publication)

    def __write_to_file(self, message):
        with open(self.__file_name, "a") as file:
            file.write(message)


if __name__ == '__main__':
    article_creator = ArticleCreator()
    article = article_creator.generate_article()
    publisher = Publisher(article)
    if publisher.get_file_name() == "":
        publisher.set_file_name("published_articles.txt")
    publisher.publish_article()
