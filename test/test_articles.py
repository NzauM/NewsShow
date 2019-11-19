import unittest
from model import Articles

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


    def test_to_check_articles(self):
        '''
        This test will check if articles from the API are picked correctly
        '''
        self.assertEquals(self.new_id,'abc')
        self.assertEquals(self.new_title,'War raises')
        self.assertEquals(self.new_description,'Korea and US set to fight')
        self.assertEquals(self.new_image,'https.image.com')
        self.assertEquals(self.new_publishedAt,2018-6-5)
        self.assertEquals(self.new_readMore,'https.abcnews.com')

    def test_process_articles(self):
        '''
        This will check if results from the article list in the API are appended to the artcles-list
        '''
        self.new_article_results_list.save_articles()
        self.assertEquals(len(Articles.news_article_results_list),1)
        

if __name__ == '__main__':
    unittest.main()