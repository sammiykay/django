from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    path('', home, name= ''),
    path('<int:new_id>/', info),
    path('sub-upload', sub_upload, name ='sub-upload'),
    path('main-upload', main_upload, name ='main-upload'),
    path('login/', auth_views.LoginView.as_view(template_name='temi/login.html'), name ='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='temi/logout.html'), name ='logout'),

]