from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ( ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,)
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseForbidden
from rest_framework.views import APIView
from .serializers import PostSerlizer
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.contrib.auth.mixins import PermissionRequiredMixin
from .mixins import PostCreatorRequiredMixin
from rest_framework import viewsets


# Create your views here.



def home(request):
	context = {'posts': Post.objects.all()}

	return render(request, 'blog/home.html', context)


class PostViewSet(viewsets.ViewSet):


    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerlizer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerlizer(post)
        return Response(serializer.data)


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5



class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_post.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(PostCreatorRequiredMixin,DetailView):
	model = Post






class PostCreateView(CreateView):
	model = Post
	fields = ['title','content']

	

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(PermissionRequiredMixin,PostCreatorRequiredMixin,UpdateView):
	model = Post
	fields = ['title','content']

	

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

def about(request):
	return render(request, 'blog/about.html')



















def loc(request):


	if request.method == 'POST':
		form = PostForm(data=request.POST, user=request.user)
		if form.is_valid():
			Profile = form.save(commit=False)
			Profile.author = request.user
			Profile.save()
			messages.success(request, f'the post !')
			return redirect('blog-loc')
		# else:
		#
		# 	return HttpResponseBadRequest('test')
	else:

		form = PostForm(user=request.user)

	context = {
		'form': form,
	}

	return render(request, 'blog/user_loc.html',context)


# def loc(request):
#
#
# 	if request.method == 'POST':
# 		form = PostSerlizer(data=request.POST, user=request.user)
# 		if form.is_valid():
# 			Profile = form.save()
# 			Profile.author = request.user
# 			Profile.save()
# 			messages.success(request, f'the post !')
# 			return redirect('blog-loc')
# 		# else:
# 		#
# 		# 	return HttpResponseBadRequest('test')
# 	else:
#
# 		form = PostForm(user=request.user)
#
# 	context = {
# 		'form': form,
# 	}
#
# 	return render(request, 'blog/user_loc.html',context)


class PostList(APIView):

	def get(self,request):
		posts = Post.objects.all()
		serializer = PostSerlizer(posts,many=True)
		return Response(status=200,data=serializer.data)










