from django.urls import path
from .views import signupfunc, loginfunc, logoutfunc, fetchApi, fetchApiUs, getArticles


urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name="logout"),
    path('fetchApi/', fetchApi, name='fetchApi'),
    path('fetchApiUs/', fetchApiUs, name='fetchApiUs'),
    path('sample/', getArticles, name='getArticles'),
]