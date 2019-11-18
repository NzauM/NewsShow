import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test behavior of the articles class
    '''

    def setUp(self):
        '''
        This method will run before each test
        '''

        self.new_article = Articles('abc','new weapon in market','new weapon released','url',2010-8-8,'read more')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))