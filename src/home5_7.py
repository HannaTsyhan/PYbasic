import csv
import os
import random
from datetime import datetime

from src.HW_4_3 import to_lower_case


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


class ArticleCreator:

    def generate_article(self, feed_type):
        feed_type = self.validate_feed_type(feed_type)
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

    def validate_feed_type(self, feed_type):
        while feed_type not in ("news", "1", "advertising", "2", "weather forecast", "3"):
            next_try = input(
                "This feed type does not exist. Please enter feed type: news, advertising, weather forecast: ")
            return self.validate_feed_type(next_try)
        return feed_type

    def input_text(self):
        return input("Enter text: ")

    def input_city(self):
        return input("Enter city: ")

    def input_expiration_date(self):
        return input("Enter expiration date: ")

    def input_region(self):
        return input("Enter region: ")


class Publisher:

    def __init__(self, list_of_articles, file_name):
        self.list_of_articles = list_of_articles
        self.__file_name = file_name

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        if value == "":
            self.__file_name = "published_articles.txt"
        else:
            self.__file_name = value

    def publish_articles(self):
        for item in self.list_of_articles:
            self.publish_article(item)

    def publish_article(self, article):
        publication = ""
        for field in article.__dict__:
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


class ArticleReader:
    def read_articles(self, file_path) -> list[Article]:
        article_list = []
        if os.path.isfile(file_path):
            with open(file_path) as f:
                article_string = f.read()
                articles = article_string.split("\n\n")
                for article in articles:
                    article_object: Article = self.parse_article(article)
                    article_list.append(article_object)
            os.remove(file_path)
            return article_list

    @staticmethod
    def parse_article(article_string) -> Article:

        feed_type, text, data = article_string.split("\n")
        text = to_lower_case(text)

        if feed_type == "news" or feed_type == "1":
            return News("news", text, data)

        elif feed_type == "advertising" or feed_type == "2":
            return Advertising("advertising", text, data)

        elif feed_type == "weather forecast" or feed_type == "3":
            return WeatherForecast("weather forecast", text, data)


class InputSwitcher:
    def get_articles(self) -> list[Article]:
        input_string = input("Enter valid feed type or path to txt file: ")
        if input_string.endswith('.txt'):
            article_reader = ArticleReader()
            articles = article_reader.read_articles(input_string)
            return articles
        else:
            article_creator = ArticleCreator()
            articles = [article_creator.generate_article(input_string)]
            return articles


class WordsLettersCounter:
    def __init__(self, output_file):
        self.output_file_string = self.read_file_to_string(output_file)

    def read_file_to_string(self, output_file):
        if os.path.isfile(output_file):
            with open(output_file) as f:
                return f.read()

    def format_string(self, file_string):
        formatted_file_string = file_string\
            .replace("\n", " ") \
            .replace(",", " ") \
            .replace("----------------", "") \
            .replace(":", " ") \
            .replace("  ", " ")
        return formatted_file_string

    def count_words(self):
        output_string_lower = self.format_string(self.output_file_string)\
            .lower()
        print(output_string_lower)

        output_lower_words: list = output_string_lower.split(" ")

        words_count_dict = {}
        for word in output_lower_words:
            if word.isalpha():
                words_count_dict[word] = words_count_dict.get(word, 0) + 1
        print(words_count_dict)

        with open("words_count.csv", 'w', newline='') as csw_file:
            writer = csv.writer(csw_file, delimiter='-')
            for word, count in sorted(words_count_dict.items()):
                writer.writerow([word.ljust(10), str(count).rjust(5)])

    def count_letters(self):
        letter_string = self.format_string(self.output_file_string)
        letter_dict = {}
        upper_letter_dict = {}
        letter_counter = 0
        for char in letter_string:
            if char.isalpha():
                letter_counter +=1
                if char.isupper():
                    upper_letter_dict[char] = upper_letter_dict.get(char, 0) + 1
                else:
                    letter_dict[char] = letter_dict.get(char, 0) + 1

        with open("letters_count.csv", 'w', newline='') as csw_file:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.writer(csw_file)
            writer.writerow(headers)
            for letter, count in sorted(letter_dict.items()):
                writer.writerow([letter, str(count), str(upper_letter_dict.get(letter.upper(), 0)),
                                 str(round((count + upper_letter_dict.get(letter.upper(), 0))/letter_counter*100, 2))])
        print(letter_counter)
        print(letter_dict)
        print(upper_letter_dict)

if __name__ == '__main__':
    input_switcher = InputSwitcher()
    articles_objects: list[Article] = input_switcher.get_articles()
    publisher = Publisher(articles_objects, "wrong.txt")
    publisher.file_name = "published_articles.txt"
    publisher.publish_articles()
    words_letters_counter = WordsLettersCounter("published_articles.txt")
    words_letters_counter.count_words()
    words_letters_counter.count_letters()
