from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from .models import Post
from django.http import HttpResponseRedirect
from .forms import DocumentForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    model= Post
    post_latest = Post.objects.order_by(ordering)[:6]
    context = {
        "post_latest":post_latest
    }
    return render(request, 'posts/index.html', context=context)

# 가장 메인에 보여줄 로직
# 북마크 모델을 불러와서 데이터 활용
class PostList(ListView):
    model = Post
    template_name_suffix = '_list'
    template_name = 'posts/post_list.html'

'''
class PostCreate(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    template_name_suffix = '_create'
    fields = ['author', 'text', 'image'] # 생성할 때 채워야 할 필드
    success_url = '/' # 성공하면 메인 페이지로 돌아가기 (이후 url로 연결)
    
    def form_vaild(self, form):
        form.instance.author_id = self.request.post_author.id
        # 입력받는 폼이 유효한지 확인하고 작성자 id 확인
        if form.is_vaild():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})



def PostCreate(request):
    if request.method == 'GET':
        form = CreateForm()

        return render(request, 'posts/post_create.html', {'form':form})
    
    elif request.method == 'POST':
        form = CreateForm(request.POST) # POST와 form을 묶어줌
        
        if form.is_valid():
            form.instance.save() # 저장
            
        return HttpResponseRedirect(reverse('posts:index'))
        #else:
        #    return self.render_to_response({'form':form})
'''

def PostCreate(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posts:index'))
    else:
        form = DocumentForm()
    return render(request, 'posts/post_create.html', {'form':form})
'''

def PostCreate(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'posts/post_create.html', {'uploaded_file_url':uploaded_file_url})
    return render(request, 'posts/post_create.html')
'''

class PostUpdate(UpdateView):
    model = Post
    fields = ['text', 'image',]
    template_name_suffix = '_update'
    success_url = '/'

class PostDelete(DeleteView):
    model = Post
    template_name_suffix = '_delete'
    success_url = '/'

class PostDetail(DetailView):
    model = Post
    template_name_suffix = '_detail'