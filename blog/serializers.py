from rest_framework import serializers
from .models import Post


class PostSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PostSerlizer,self).__init__(*args, **kwargs)
