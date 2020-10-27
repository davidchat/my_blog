from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Post, Comment
from .forms import PostForm


# def home(request):
# 	context = {'posts': Post.objects.all()}
# 	return render(request, 'blog/home.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	# <app>/<model>_<viewtype>.html is the conventional template name for a class-based view
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	# <app>/<model>_<viewtype>.html is the conventional template name for a class-based view
	context_object_name = 'posts'
	paginate_by = 5

	# Override default get_query_set function to filter by user
	def get_queryset(self):
		# We pull the username from the URL itself
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		# Finish the query filtering by user
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post


def create_post(request):
	form = PostForm

	try:
		if request.user.groups.first().name == 'admin':
			if request.method == 'POST':
				form = PostForm(data=request.POST)
				if form.is_valid():
					new_post = form.save(commit=False)
					new_post.author = request.user
					new_post.save()
					return redirect('/')
	except:
		messages.info(request, 'Sorry, you are not authorized to make blog posts.')
		return redirect('/')
	
	context = {'form': form}
	return render(request, 'blog/post_form.html', context)


# class PostCreateView(LoginRequiredMixin, CreateView):	
# 	# if self.request.user.groups.first().name == 'admin':
# 	model = Post
# 	fields = ['title', 'content']

# 	# Override default form_valid function to add author field
# 	def form_valid(self, form):
# 		# Author is set automatically to current user
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)
# 	# else:
# 	# 	raise Http404


def update_post(request, pk):
	post = get_object_or_404(Post, id=pk)

	try:
		if request.user.groups.first().name == 'admin':
			if request.method == 'POST':
				form = PostForm(data=request.POST, instance=post)
				if form.is_valid():
					updated_post = form.save(commit=False)
					updated_post.author = request.user
					updated_post.save()
					return redirect('/')
			else:
				form = PostForm(instance=post)
	except:
		messages.info(request, 'Sorry, you are not authorized to make blog posts.')
		return redirect('/')
	
	context = {'form': form}
	return render(request, 'blog/post_form.html', context)


# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
# 	model = Post
# 	fields = ['title', 'content']
# 	template_name = 'blog/post_form.html'

# 	# Override default form_valid function to add author field
# 	def form_valid(self, form):
# 		# Author is set automatically to current user
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)

# 	def test_func(self):
# 		# Get the current post
# 		post = self.get_object()
# 		if self.request.user == post.author:
# 			return True
# 		return False


def delete_post(request, pk):
	post = get_object_or_404(Post, id=pk)

	try:
		if request.user.groups.first().name == 'admin':
			if request.method == 'POST':
				post.delete()
				return redirect('/')
	except:
		messages.info(request, 'Sorry, you are not authorized to delete blog posts.')
		return redirect('/')
	
	context = {'post': post}
	return render(request, 'blog/post_confirm_delete.html', context)	


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		# Get the current post
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	fields = ['body']

	# Override default form_valid function to add author field
	def form_valid(self, form):
		# Author is set automatically to current user
		form.instance.author = self.request.user
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Comment
	fields = ['body']

	# Override default form_valid function to add author field
	def form_valid(self, form):
		# Author is set automatically to current user
		return super().form_valid(form)

	def test_func(self):
		# Get the current comment
		comment = self.get_object()
		if self.request.user == comment.author:
			return True
		return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	success_url = '/'

	def test_func(self):
		# Get the current comment
		comment = self.get_object()
		if self.request.user == comment.author:
			return True
		return False


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})


