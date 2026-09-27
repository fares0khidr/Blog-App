from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from .forms import PostForm, SignUpForm
from .models import Category, Post, Tag


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class AuthenticationStatusView(TemplateView):
    template_name = 'authentication/status.html'


class PublishedPostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ('-updated_at', '-created_at')

    def get_queryset(self):
        queryset = Post.objects.filter(published=True)

        query = self.request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))

        category_id = self.request.GET.get('category', '')
        if category_id.isdigit():
            queryset = queryset.filter(category_id=int(category_id))

        tag_id = self.request.GET.get('tag', '')
        if tag_id.isdigit():
            queryset = queryset.filter(tags__id=int(tag_id))

        return (
            queryset.select_related('author', 'category')
            .prefetch_related('tags')
            .order_by(*self.ordering)
            .distinct()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context.update(
            categories=Category.objects.order_by('name'),
            tags=Tag.objects.order_by('name'),
            current_query=self.request.GET.get('q', ''),
            current_category=self.request.GET.get('category', ''),
            current_tag=self.request.GET.get('tag', ''),
            query_string=query_params.urlencode(),
        )
        return context


class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/my_posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ('-created_at', '-updated_at')

    def get_queryset(self):
        return (
            Post.objects.filter(author=self.request.user)
            .select_related('category')
            .prefetch_related('tags')
            .order_by(*self.ordering)
        )


class PublishedPostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Post.objects.select_related('author', 'category').prefetch_related('tags'),
            pk=self.kwargs['pk'],
            published=True,
        )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class OwnedPostMixin(LoginRequiredMixin):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class PostUpdateView(OwnedPostMixin, UpdateView):
    form_class = PostForm
    template_name = 'blog/post_form.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')


class PostDeleteView(OwnedPostMixin, DeleteView):
    template_name = 'blog/post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('post-list')
