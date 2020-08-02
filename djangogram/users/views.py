from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

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
                return HttpResponseRedirect(reverse('posts:index'))
        # 회원가입 실패하면 메인페이지로 이동            
        return render(request, 'users/main.html')
