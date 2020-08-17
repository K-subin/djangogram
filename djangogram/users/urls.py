from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

# users 앱에서는 view함수 내부에 main함수와 연결 --> main함수 만들고 템플릿 만들자
app_name = "users"
urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    #path('UserProfile/', views.UserProfile, name='UserProfile'),
    #path('profile/', views.ProfileList.as_view(), name='profile'),
    #path('profile/', views.ProfileList, name='profile'),
    url(r'^profile/(?P<username>\d+)/$', views.ProfileList.as_view(), name="profile"),
    url(r'^profile/update/(?P<username>\d+)/$',views.ProfileUpdate,name="profileupdate"),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 