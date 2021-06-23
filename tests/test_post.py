import unittest
from app.models import Post, User

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.user_jose=User(username='oti', password_hash='josephat', email='josiah@gmail.com')
        self.new_post=Post(title='jose', content='race with time',  user=self.user_jose)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEqual(self.new_post.title, 'jose')
        self.assertEqual(self.new_post.content, 'race with time')
        self.assertEqual(self.new_post.user, self.user_jose)

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())==1)

    def test_get_posts(self):
        self.new_post.save_post()
        got_posts=Post.get_all_posts()
        self.assertTrue(len(got_posts)>0)


    def test_delete_post(self):
        self.new_post.delete_post()
        self.assertTrue(len(Post.query.all()==0))