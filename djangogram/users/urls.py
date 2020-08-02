from django.urls import path
from . import views

# users 앱에서는 view함수 내부에 main함수와 연결 --> main함수 만들고 템플릿 만들자
app_name = "users"
urlpatterns = [
    path('', views.main, name='main'),
]
