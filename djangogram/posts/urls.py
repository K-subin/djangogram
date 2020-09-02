from django.urls import path
from .views import PostList, PostCreate, PostDelete, PostDetail, PostUpdate, PostLike, PostFavorite

app_name = 'posts'
 
# path(url pattern, view, url pattern name),
urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('create/', PostCreate.as_view(), name='create'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='detail'),
    #path('create/', PostCreate, name='create'),
    path('like/<int:post_id>/', PostLike.as_view(), name='like'),
    path('favorite/<int:post_id>/', PostFavorite.as_view(), name='favorite'),

]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)