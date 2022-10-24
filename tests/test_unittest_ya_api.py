import unittest
import yadisk
from api_ya import ya_api, delete_fold


class TestFunctions(unittest.TestCase):
    
    def test_ya_api(self):
        result = ya_api('3')
        self.assertEqual('3', result)
        delete_fold()











