from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.neighborhood, name="neighbourhood"),
    path('edit/', views.businessedit, name="edit"),
    path('business/', views.business, name="business"),
    path('hood/', views.neighbourdisplay, name="hood"),
    path('account/', views.accountSettings, name="account"),
    re_path(r'^search/', views.search_results, name='search_results')
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)