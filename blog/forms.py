from django import forms
from .models import Post
from math import sin
from users.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PostForm,self).__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        title = self.cleaned_data.get("title")
        leatest_post = Post.objects.all().order_by('-date_posted')[:1].get()
        # validation for 5 post
        count_post = Post.objects.filter(author=self.user).count()

        if title in Post.get_prohopeted():
            raise forms.ValidationError(f'not a valid title', code='not_valid_title')
        if count_post > 10:
            raise forms.ValidationError(f'you cant add more then 10 post', code='not_valid_title')
        # if leatest_post.author == self.user:
        #     raise forms.ValidationError(f'you cant add two post in a row', code='not_valid_title')
