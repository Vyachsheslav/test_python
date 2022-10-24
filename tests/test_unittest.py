import unittest

from main import get_all_doc_owners_names


class TestFunctions(unittest.TestCase):
    
    def test_get_all_doc_owners_name(self):
        result = get_all_doc_owners_names()
        self.assertEqual({'Василий Гупкин'}, result)



