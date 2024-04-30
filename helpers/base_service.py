import logging

import allure
from logging import StreamHandler, Formatter, FileHandler

import requests

from data.urls import DOMEN_API


class BaseServices:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
    @allure.step('GET: {path}')
    def get(self, path, headers):
        response = requests.get(DOMEN_API + path, headers=headers)
        if response.status_code == 200:
            self.logger.info('OK')
            return response.json()
        elif response.status_code == 404:
            self.logger.info(f'Response: {response.status_code}, {response.text}')
            return True
        else:
            self.logger.error(f'FAIL - {response.status_code}: {response.text}')
            raise ValueError(f"GET request to {path} failed with status code {response.status_code}")

    @allure.step('POST: {path}')
    def post(self, path, headers, body):
        response = requests.post(DOMEN_API + path, headers=headers, json=body)
        if response.status_code == 200:
            self.logger.info('OK')
            return response.json()
        else:
            self.logger.error('FAIL')
            assert False

    @allure.step('PUT: {path}')
    def put(self, path, headers, body):
        response = requests.put(DOMEN_API + path, headers=headers, json=body)
        if response.status_code == 200:
            self.logger.info('OK')
            return response.json()
        else:
            self.logger.error('FAIL')
            assert False

    @allure.step('PATCH: {path}')
    def patch(self, path):
        response = requests.patch(DOMEN_API + path)
        if response.status_code == 200:
            self.logger.info('OK')
            return response.json()
        else:
            self.logger.error('FAIL')
            assert False

    @allure.step('UPLOAD')
    def upload(self, path, headers, file):
        response = requests.post(DOMEN_API + path, headers=headers, files=file)
        if response.status_code == 200:
            self.logger.info('OK')
            return response.json()
        else:
            self.logger.error('FAIL')
            assert False

    @allure.step('DELETE: {path}')
    def delete(self, path, code):
        response = requests.delete(DOMEN_API + path)
        if response.status_code == code:
            self.logger.info('OK')
            assert True
        else:
            self.logger.error('FAIL')
            assert False

    # def _logger(self):
    #     self.logger = logging.getLogger(self.__class__.__name__)
    #     self.logger.setLevel(logging.DEBUG)
    #     handler = StreamHandler()
    #     handler.setFormatter(Formatter(fmt='%(asctime)s %(levelname)s %(message)s'))
    #     file_handler = FileHandler('logging_api.log')
    #     self.logger.addHandler(file_handler)
    #     self.logger.addHandler(handler)

