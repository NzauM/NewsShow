import unittest
from .model import News

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


    def test_to_check_newssources(self):
        '''
        This test will check if news sources are received correctly
        '''
        self.assertEquals(self.new_name,'Daily Nation')
        self.assertEquals(self.new_description,'Nation news')
        self.assertEquals(self.new_url,'dailynation.co.ke')

    def test_process_results(self):
        '''
        This will check if results from the news sources are appended correctly
        '''
        self.new_newslist.save_news()
        self.assertEquals(len(News.news_list),1)
        

if __name__ == '__main__':
    unittest.main()
