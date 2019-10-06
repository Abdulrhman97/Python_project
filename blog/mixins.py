from django.shortcuts import get_object_or_404, redirect
from .models import Post
from django.http import Http404

class PostCreatorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if post.author != request.user:
            raise Http404("not permissoned")
        return super().dispatch(request, *args, **kwargs)
