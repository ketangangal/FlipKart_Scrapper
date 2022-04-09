import requests
import sys
from bs4 import BeautifulSoup as bs
from flipkart_scrapper_entity_layer.entity import Product
from flipkart_scrapper_utils.utils import read_config
from flipkart_scrapper_logging_layer.logging import CustomLogger
from flipkart_scrapper_exception_layer.exception import FlipkartCustomException

logger = CustomLogger('logic_layer_logs')
config = read_config()


class Scrapper:
    def __init__(self, search_result):
        """
        Creator: Ketan Gangal
        created date: 07 april 2022
        Organization: iNeuron
        :arg search_result: Enter product to scrap from flipkart.
        """
        self.search_string = search_result
        self.reviews = list()
        self.comment_boxes = None
        self.boxes = None
        self.result = None
        self.scraped_data = dict()

    def __read_url(self, link):
        """
        This is a private method used by get data
        :param link: Enter url to get data form webpage.
        :return: requests.Response
        """
        self.result = requests.get(link)
        self.result.encoding = 'utf-8'
        self.result = bs(self.result.text, "html.parser")
        return self.result

    def __flipkart_url(self):
        """
        This is an internal function used to get search results and stores product card information
        in self.boxes which is further used in getdata method of the class

        """
        flipkart_url = config['links']['flipkart_url'] + self.search_string
        page = self.__read_url(flipkart_url)
        self.boxes = page.findAll("div", {"class": "_1YokD2 _3Mn1Gg"})

    @staticmethod
    def __get_name(data):
        """
        :param data: Gets product card and returns name of the product
        :return: Name str
        """
        try:
            name = data.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
        except Exception as e:
            name = 'No Name'

        return name

    @staticmethod
    def __get_rating(data):
        """
        :param data: Gets product card and returns rating of the product
        :return: rating str
        """
        try:
            rating = data.div.div.div.div.text
        except Exception as e:
            rating = 'No Rating'

        return rating

    @staticmethod
    def __get_comment_head(data):
        """
        :param data: Gets product card and returns comment_head of the product
        :return: comment_head str
        """
        try:
            comment_head = data.div.div.div.p.text
        except Exception as e:
            comment_head = 'No Comment Heading'

        return comment_head

    @staticmethod
    def __get_comment(data):
        """
        :param data: Gets product card and returns comment of the product
        :return: comment str
        """
        try:
            comment_tag = data.div.div.find_all('div', {'class': ''})
            comment = comment_tag[0].div.text
        except Exception as e:
            comment = "No comment"
        return comment

    def get_data(self) -> Product:
        """
        This method make use of private methods to scrape data form flipkart
        :return: Reterived Information of the 5 products.
        """
        try:
            self.__flipkart_url()
            self.boxes[0].findAll("div", {"class": "_2kHMtA"})
            for box in self.boxes[0].findAll("div", {"class": "_2kHMtA"})[0:5]:
                product_url = config['links']['product_url'] + box.a['href']
                page = self.__read_url(product_url)
                self.comment_boxes = page.find_all('div', {'class': "_16PBlm"})
                logger.info(f"Scrapping Data {self.search_string} from Flipkart")

                Product_name = page.find_all('h1', {'class': "yhB1nd"})[0].span.get_text()

                for data in self.comment_boxes:
                    name = self.__get_name(data)
                    rating = self.__get_rating(data)
                    comment_head = self.__get_comment_head(data)
                    comment = self.__get_comment(data)

                    product = Product(Product_name=self.search_string, Name=name,
                                      Rating=rating, CommentHead=comment_head, Comment=comment)._asdict()
                    self.reviews.append(product)

                self.scraped_data[Product_name] = self.reviews
                self.reviews = list()
                logger.info(f"Scrapping Completed for {self.search_string}")
            return [self.scraped_data]
        except Exception as e:
            message = FlipkartCustomException(e, sys)
            logger.error(message.error_message)
            raise message.error_message

