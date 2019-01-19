from django.urls import path
from . import views





app_name='users'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('deconnect/', views.deconnect, name='deconnect'),
    path('login/', views.login, name='login'),

]