from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, FormView
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from .forms import CreateForm
from .models import Post
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from urllib.parse import urlparse


# 가장 메인에 보여줄 로직
# 북마크 모델을 불러와서 데이터 활용
class PostList(ListView):
    model = Post
    template_name_suffix = '_list'
    template_name = 'posts/post_list.html'

class PostCreate(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    template_name_suffix = '_create'
    form_class = CreateForm
    success_url = '/posts' # 성공하면 메인 페이지로 돌아가기 (이후 url로 연결)
   
    def form_valid(self, form):        
        # 입력받는 폼이 유효한지 확인하고 작성자 id 확인
        if form.is_valid():
            form.instance.author = self.request.user
            form.instance.save()
            return super().form_valid(form)
        else:
            return self.render_to_response({'form':form})

class PostUpdate(UpdateView):
    model = Post
    fields = ['text', 'image',]
    template_name_suffix = '_update'
    #success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)

class PostDelete(DeleteView):
    model = Post
    template_name_suffix = '_delete'
    success_url = '/posts'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/posts')
        else:
            return super(PostDelete, self).dispatch(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name_suffix = '_detail'


class PostLike(View):
    def get(self, request, *args, **kwargs):
        # 로그인이 확인되지 않으면 자료를 숨기기
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'post_id' in kwargs:
                post_id = kwargs['post_id']
                post = Post.objects.get(pk=post_id)
                user = request.user
                # 이미 좋아요 했으면 지우기
                if user in post.like.all():
                    post.like.remove(user)
                # 안했으면 더하기
                else:
                    post.like.add(user)
            # referer_url을 통해 좋아요 누른 페이지 그대로 있도록
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)

class PostFavorite(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'post_id' in kwargs:
                post_id = kwargs['post_id']
                post = Post.objects.get(pk=post_id)
                user = request.user
                if user in post.favorite.all():
                    post.favorite.remove(user)
                else:
                    post.favorite.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)
