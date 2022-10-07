from django.urls import  path
from . import views

app_name = 'api'

urlpatterns = [

     # Blog APIurls

    path('blog/list/' , views.BlogListView.as_view()),
    path('blog/list/<int:pk>/' , views.BlogDeleteUpdateView.as_view()),
    path('blog/important/' , views.BLogImportantList.as_view()),
    path('blog/important/<int:pk>' , views.BlogToImportant.as_view()),

    # Project APIurls

    path('project/list/' , views.ProjectListView.as_view() ),
    path('project/list/<int:pk>' , views.ProjectUpdateDelete.as_view() ),

]