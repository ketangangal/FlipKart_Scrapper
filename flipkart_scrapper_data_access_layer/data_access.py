from flipkart_scrapper_exception_layer.exception import FlipkartCustomException
from flipkart_scrapper_logging_layer.logging import CustomLogger
from flipkart_scrapper_utils.utils import read_config
from pymongo import MongoClient
import sys

config = read_config()
logger = CustomLogger('data_access_logs')


class Database:
    def __init__(self):
        """Database Layer to make connection with mongodb easy. Contains Create, Drop and Get collection"""
        self.client = MongoClient(config['secrets']['mongodb'])
        self.database = self.client['Flipkart_store']

    def create_collection(self, collection_name, data):
        """
        create_collection : Create a collection in the database initialized using config.
        :param collection_name: Requires Collection Name
        :param data: Data(documents) to put into collection
        :return: success message to the user
        """
        try:
            collection = self.database[collection_name]
            response = collection.insert_many(data)
            if response:
                return response.acknowledged
            else:
                return False
        except Exception as e:
            message = FlipkartCustomException(e, sys)
            logger.error(message.error_message)
            raise message.error_message

    def drop_collection(self, collection_name):
        """
        create_collection : Create a collection in the database initialized using config.
        :param collection_name: Requires Collection Name
        :return: Drops collection from mongodb and returns success message
        """
        try:
            collection = self.database[collection_name]
            collection.drop()
            return True
        except Exception as e:
            message = FlipkartCustomException(e, sys)
            logger.error(message.error_message)
            raise message.error_message

    def get_collection(self, collection_name):
        """
        create_collection : Create a collection in the database initialized using config.
        :param collection_name: Requires Collection Name
        :return: collection documents to the user as [Documents]
        """
        try:
            collection = self.database[collection_name]
            data = list(collection.find())
            return data
        except Exception as e:
            message = FlipkartCustomException(e, sys)
            logger.error(message.error_message)
            raise message.error_message
