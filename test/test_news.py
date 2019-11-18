import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test class to test behaviors of the news class
    '''

    def setUp(self):
        '''
        This method will run before each test
        '''
        self.new_news = News('ABC','All of news worldwide','abc')

    def test_instance(self):
        self.asserTrue(isinstance(self.new_news,News))