from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from blog.models import Post, Comment


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        # Create dummy user
        self.user1 = User.objects.create_user(
            username='user1',
            password='1234',
        )
        self.user1.save()

        self.post1 = Post.objects.create(
            title='PostTitle1',
            content='PostContent1',
            author=self.user1,
        )

        self.comment1 = Comment.objects.create(
            post=self.post1,
            author=self.user1,
            body='CommentContent1',
        )

        self.blog_home_url = reverse('blog-home')
        self.user_posts_url = reverse('user-posts', args=['user1'])
        self.post_detail_url = reverse('post-detail', args=['1'])
        self.post_create_url = reverse('post-create')
        self.post_update_url = reverse('post-update', args=['1'])
        self.post_delete_url = reverse('post-delete', args=['1'])
        self.comment_create_url = reverse('comment-create', args=['1'])
        self.comment_update_url = reverse('comment-update', args=['1'])
        self.comment_delete_url = reverse('comment-delete', args=['1'])
        self.blog_about_url = reverse('blog-about')

    def tearDown(self):
        self.client.logout()

    def test_post_list_view_get(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get(self.blog_home_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_user_post_list_view_get(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get(self.user_posts_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/user_posts.html')

    def test_post_detail_view_get(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get(self.post_detail_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_create_view_get(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get(self.post_create_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')
    
    def test_post_create_view_post(self):
        self.client.login(username='user1', password='1234')
        response = self.client.post(self.post_create_url, {
            'title': 'Post 2',
            'content': 'Post 2 Content',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'Post 2')
        self.assertEqual(Post.objects.last().content, 'Post 2 Content')
        self.assertEqual(Post.objects.last().author, self.user1)

    def test_post_update_view_get(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get(self.post_update_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')
    
    def test_post_update_view_post(self):
        self.client.login(username='user1', password='1234')
        response = self.client.post(self.post_update_url, {
            'title': 'Post A',
            'content': 'Post A Content',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.first().title, 'Post A')
        self.assertEqual(Post.objects.first().content, 'Post A Content')

    def test_post_delete_view_get(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get(self.post_delete_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_confirm_delete.html')
    
    def test_post_delete_view_post(self):
        self.client.login(username='user1', password='1234')
        response = self.client.post(self.post_delete_url, args=['1'])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)

    def test_comment_create_view_get(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get(self.comment_create_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/comment_form.html')

    def test_comment_create_view_post(self):
        self.client.login(username='user1', password='1234')
        response = self.client.post(self.comment_create_url, {
            'body': 'Comment 2 Content',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.last().body, 'Comment 2 Content')
        self.assertEqual(Comment.objects.last().author, self.user1)

    def test_comment_update_view_get(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get(self.comment_update_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/comment_form.html')
    
    def test_comment_update_view_post(self):
        self.client.login(username='user1', password='1234')
        response = self.client.post(self.comment_update_url, {
            'body': 'Comment A Content',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.first().body, 'Comment A Content')

    def test_comment_delete_view_get(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get(self.comment_delete_url)

        self.assertEqual(str(response.context['user']), 'user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/comment_confirm_delete.html')
    
    def test_comment_delete_view_post(self):
        self.client.login(username='user1', password='1234')
        response = self.client.post(self.comment_delete_url, args=['1'])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 0)

    def test_about_view_get(self):
        response = self.client.get(self.blog_about_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')
