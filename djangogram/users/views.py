from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


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
    