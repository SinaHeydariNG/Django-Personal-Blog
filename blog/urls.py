
from django.urls import  path
from . import views
app_name = 'blog'

urlpatterns = [
    path('list/' , views.list , name='list'),
    path('<slug:slug>/' , views.detail , name='detail'),
    path('categories/<int:id>' , views.list_by_category , name='category'),
    path('likes/<int:id>' , views.likePost , name='like')
]
