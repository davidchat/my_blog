from django.test import TestCase
from django.urls import reverse, resolve

from blog.views import *


class TestUrls(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='1234'
        )
        self.user1.save()

    def test_blog_home_url_resolves(self):
        url = reverse('blog-home')
        self.assertEqual(resolve(url).func.__name__, PostListView.as_view().__name__)

    def test_user_posts_url_resolves(self):
        url = reverse('user-posts', args=['user1'])
        self.assertEqual(resolve(url).func.__name__, UserPostListView.as_view().__name__)

    def test_post_detail_url_resolves(self):
        url = reverse('post-detail', args=['1'])
        self.assertEqual(resolve(url).func.__name__, PostDetailView.as_view().__name__)
    
    def test_post_create_url_resolves(self):
        url = reverse('post-create')
        self.assertEqual(resolve(url).func.__name__, PostCreateView.as_view().__name__)

    def test_post_update_url_resolves(self):
        url = reverse('post-update', args=['1'])
        self.assertEqual(resolve(url).func.__name__, PostUpdateView.as_view().__name__)
    
    def test_post_delete_url_resolves(self):
        url = reverse('post-delete', args=['1'])
        self.assertEqual(resolve(url).func.__name__, PostDeleteView.as_view().__name__)

    def test_comment_create_url_resolves(self):
        url = reverse('comment-create', args=['1'])
        self.assertEqual(resolve(url).func.__name__, CommentCreateView.as_view().__name__)

    def test_comment_update_url_resolves(self):
        url = reverse('comment-update', args=['1'])
        self.assertEqual(resolve(url).func.__name__, CommentUpdateView.as_view().__name__)
    
    def test_comment_delete_url_resolves(self):
        url = reverse('comment-delete', args=['1'])
        self.assertEqual(resolve(url).func.__name__, CommentDeleteView.as_view().__name__)

    def test_blog_about_url_resolves(self):
        url = reverse('blog-about')
        self.assertEqual(resolve(url).func, about)
    
