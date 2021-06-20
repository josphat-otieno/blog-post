import unittest 
from app.models import Quote

class QuoteTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Quote  class
    '''

    def setUp(self):
        '''
        set up method to run before each every test
        '''
        self.new_quote = Quote("josephat", "coding is challenging")

    def test_instance(self):
        '''
        test case to confirm new_quote is an instance of the quote class
        '''
        self.assertTrue(isinstance(self.new_quote, Quote))

    def test_init(self):
        '''test case to confirm the object is intialised correctly
        '''
        self.assertEqual(self.new_quote.author, "josephat")
        self.assertEqual(self.new_quote.quote, "coding is challenging")

