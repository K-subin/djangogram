from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, ProfileForm
from . import models
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

def main(request):
    # GET과 POST 분기 처리

    # 페이지를 보기 위한 GET방식
    if request.method == 'GET':
        return render(request, 'users/main.html')
    # 로그인을 위한 POST방식
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # 로그인 성공하면 posts 페이지로 이동
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('posts:index'))
        # 로그인 실패하면 메인페이지로 이동
        else:
            return render(request, 'users/main.html')

# 회원가입
def signup(request):
    if request.method == 'GET':
        form = SignUpForm()

        return render(request, 'users/signup.html', {'form':form})
    
    elif request.method == 'POST':
        form = SignUpForm(request.POST) # POST와 form을 묶어줌

        if form.is_valid():
            form.save() # 저장

            # 회원가입 후 자동 로그인 기능
            # cleaned 데이터에 저장된 것을 불러온다.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
 
            # 로그인 성공하면 posts 페이지로 이동
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
        # 회원가입 실패하면 메인페이지로 이동            
        return render(request, 'users/main.html')


class ProfileList(DetailView):
    model = models.User
    fields = ['profile_photo','username', 'email', 'phone_number', 'gender']
    template_name = 'users/profile_list.html'
    context_object_name = 'profile_user'
    def get_object(self):
        return models.User.objects.get(username=username)

'''
  
def ProfileList(request, username):
    if request.method == 'GET':
        return render(request, 'users/profile_update.html')

    elif request.method == 'POST': 
        profile_user = get_object_or_404(User, username)
        #user = models.User.objects.get(username=username)
        
        #username=request.user.username
        
        return render(request, 'users/profile_list.html')
'''


def ProfileUpdate(request, username):
    if request.method == 'GET':
        form = ProfileForm()
          
        return render(request, 'users/profile_update.html', {'form':form})
    
    elif request.method == 'POST':
        context_object_name = 'profile_user' 
        form = ProfileForm(request.POST) # POST와 form을 묶어줌
        found_user = models.User.objects.get(username=username)

        if found_user is None:
            return render(request, 'users/main.html')
        elif found_user != request.user.username:
            return render(request, 'users/main.html')
        else:
            if form.is_valid():
                form.save() # 저장

                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                
            return render(request, 'users/profile_update.html')


'''    
def ProfileUpdateView(request):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        user_form = UserForm(initial = {
            'username' : user.username,
        })

        if hasattr(user, 'profile'):
            profile = user.profile
            profile_form = ProfileForm(initial={
                'nickname':profile.nickname,
                'profile_photo':profile.profile_photo,
            })
        else:
            profile_form = ProfileForm()
        
        return render(request, 'user/profile_update.html', {"user_form":user_form, "profile_form":profile_form})
'''