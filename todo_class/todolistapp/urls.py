from . import views
from django.urls import path

urlpatterns = [
    path('',views.todoview.as_view(), name='home1'),
    path('home/',views.Todolist.as_view(), name='home'),
    path('detail/<int:pk>/', views.tododetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.Todoupdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.Tododelete.as_view(), name='delete'),
]