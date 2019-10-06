from django.test import TestCase,Client
from django.urls import reverse
from .models import  Post
from .forms import PostForm
from users.models import User




# Create your tests here.

class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='almandah',email='akmandah17@gmail.com')
        self.user.set_password('testing321')
        self.user.save()
        self.post = Post.objects.create(title='post 5',content='RANDOM CONTENT',author=self.user)

        self.random = User.objects.create(username='saud',email='saud@gmail.com')
        self.random.set_password('testing1111')
        self.random.save()

    def test_project_form(self):
       form = PostForm(data={'title': "cat", 'content':"RANDOM CONTENT"})
       self.assertFalse(form.is_valid())
       form.has_error('title', code='not_valid_title')

    def test_title_valid(self):
        data = {'title': "titne", 'content':"RANDOM CONTENT"}
        self.client.login(username='almandah', password='testing321')
        response = self.client.post(reverse('blog-loc'), data)
        self.assertEqual(response.status_code, 302)
        post = Post.objects.get(title="titne")
        self.assertEqual(post.title,data.get('title'))

    def test_title_invalid(self):
        data = {'title': "car", 'content': "RANDOM CONTENT"}
        self.client.login(username='almandah', password='testing321')
        response = self.client.post(reverse('blog-loc'), data)
        self.assertEqual(response.status_code, 400)

    def test_number_of_post_invalid(self):
        self.client.login(username='almandah', password='testing321')
        data = {'title': "sdfsdfd", 'content': "RANDOM CONTENT"}
        self.post = Post.objects.create(title='post 5', content='RANDOM CONTENT', author=self.user)
        self.post = Post.objects.create(title='post 5', content='RANDOM CONTENT', author=self.user)
        self.post = Post.objects.create(title='post 5', content='RANDOM CONTENT', author=self.user)
        self.post = Post.objects.create(title='post 5', content='RANDOM CONTENT', author=self.user)
        response = self.client.post(reverse('blog-loc'), data)
        self.assertEqual(response.status_code, 400)

    def test_two_post_in_a_raw_invalid(self):
        self.client.login(username='almandah', password='testing321')
        data = {'title': "sdfsdfd", 'content': "RANDOM CONTENT"}
        self.client.post(reverse('blog-loc'), data)
        self.client.logout()
        self.client.login(username='almandah', password='testing321')
        response = self.client.post(reverse('blog-loc'), data)
        self.assertEqual(response.status_code, 400)

    def test_two_post_in_a_raw_valid(self):
        data = {'title': "sdfsdfd", 'content': "RANDOM CONTENT"}

        self.client.login(username='saud', password='testing1111')
        self.client.post(reverse('blog-loc'), data)
        self.client.logout()

        self.client.login(username='almandah', password='testing321')
        response = self.client.post(reverse('blog-loc'), data)
        self.assertEqual(response.status_code, 302)

        #test_project_validation(self):








     #   response = self.client.get(reverse('blog-loc'))

      #  self.assertEqual(response.status_code, 200)