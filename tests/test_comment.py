import unittest
from app.models import Comment, User
from app import db

class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.user_jose=User(username='kevin', password_hash='josephat', email = 'kevin@gmail.com')

        self.new_comment=Comment( post_id=1,name='jose', comment='realy', user=self.user_jose)

    def tearDown(self):
        User.query.delete()
        Comment.query.delete()

    def check_instance_variables(self): 
        self.assertEqual(self.new_comment.name, 'jose')
        self.assertEqual(self.new_comment.comment, 'realy')
        self.assertEqual(self.new_comment.pitch_id, 1)
        

    def test_save_comments(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())==1)

    def test_get_comments(self):
        self.new_comment.save_comment()
        got_comments= Comment.get_comments(1)
        self.assertTrue(len(got_comments)>0)

    def test_delete_comment(self):
        self.new_comment.delete_comment()
        self.assertTrue(len(Comment.query.all())==0)