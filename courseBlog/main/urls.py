from django.urls import path

from main.views import mainView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView

urlpatterns = [
    path('main/', mainView.as_view(), name='main'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('add_post', AddPostView.as_view(), name='add_post'),
    path('add_category', AddCategoryView.as_view(), name='add_category'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name='delete_post'),
]