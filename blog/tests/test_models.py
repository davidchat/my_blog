from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Post, Comment


class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='1234'
        )
        self.user1.save()

        # Create dummy post
        self.post1 = Post.objects.create(
            title='Post1',
            content='Post 1 Content',
            author=self.user1,
        )

        # Create dummy comment
        self.comment1 = Comment.objects.create(
            post=self.post1,
            author=self.user1,
            body = 'Comment 1 Content',
        )

        def test_post_string_representation(self):
            self.assertEqual(str(self.post1), 'Post1')

        


