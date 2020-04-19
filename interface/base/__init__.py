import unittest
import requests
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from db_fixture import test_data


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.host_url = "http://127.0.0.1:8000/api"

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        """
        post请求
        """
        r = requests.post(url, data=None, json=None, **kwargs)
        return r

    @staticmethod
    def get(url, params=None, **kwargs):
        """
        get请求
        """
        r = requests.get(url, params=None, **kwargs)
        return r


def run():
    """初始化数据，运行测试"""
    test_data.init_data()
    unittest.main()
