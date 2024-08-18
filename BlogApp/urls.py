from django.urls import path
from BlogApp import views


urlpatterns = [
    path('',views.HomeView,name='home'),
    path('about/', views.AboutView,name='about'),
    path('dashboard/', views.DashboardView,name='dashboard'),
    path('signup/',views.SignupView,name='signup'),
    path('login/',views.LoginView,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('contact/', views.ContactView,name='contact'),
    path('add-post/',views.AddPostView,name='addpost'),
    path('update-post/<int:id>/',views.UpdatePostPage,name='updatepost'),
    path('delete-post/<int:id>/', views.DeletePostView,name='deletepost'),
]
