from app.models import Subscriber
import unittest

class SubscriberTest(unittest.TestCase):

    def setUp(self):

        self.new_subscriber=Subscriber(email='jose@gmail.com')

    def tearDown(self):
        Subscriber.query.delete()

    def test_check_instance_variables(self):
        self.assertEqual(self.new_subscriber.email, 'jose@gmail.com')

    def test_save_subscriber(self):
        self.new_subscriber.save_subscriber()
        self.assertTrue(len(Subscriber.query.all())==1)
       
       
