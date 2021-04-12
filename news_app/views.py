from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import IntegrityError



# Create your views here.

import requests
import json

apikey = "3156cce2dd144f1292bdfec6ce0a2161"

# サインアップ機能
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'this user has already been created.'})

    return render(request, 'signup.html')

# ログイン機能
def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # ユーザーが登録されている場合、userオブジェクトが返却される
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('fetchApi')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

# ログアウト機能
def logoutfunc(request):
    logout(request)
    return redirect('login')

#　APIへのリクエストとレスポンスの受け取り（日本版ニュース）
def fetchApi(request):

    apikey = "3156cce2dd144f1292bdfec6ce0a2161"
    searchFlg = False
    result = []
    country = "jp"
    
    if request.method == 'GET': 
        api = "https://newsapi.org/v2/top-headlines?country={co}&pageSize=100&apiKey={key}"

        url = api.format(co=country,key=apikey)
        r = requests.get(url)
        data = r.json()
        result = data["articles"]

        return render(request, 'fetchApi.html', {
            'result': result,
            'searchFlg': searchFlg,
            })

    #カテゴリ指定
    elif 'category' in request.POST: 
        api = "https://newsapi.org/v2/top-headlines?country={co}&category={ca}&pageSize=100&apiKey={key}"
        category = request.POST['category']
        url = api.format(co=country, ca=category, key=apikey)
        r = requests.get(url)
        data = r.json()
        result = data["articles"]

        return render(request, 'fetchApi.html', {
            'category': category,
            'result': result,
            'searchFlg': searchFlg,
            })

    # キーワード検索
    elif 'keyword' in request.POST: 
        searchFlg = True
        keyword = request.POST['keyword']
        cons = ['business', 'science', 'entertainment', 'general', 'health', 'sport', 'technology']

        api = "https://newsapi.org/v2/top-headlines?country={co}&category={ca}&pageSize=100&apiKey={key}"
        arr = []
        for con in cons:
            url = api.format(co=country, ca=con, key=apikey)
            r = requests.get(url)
            data = r.json()
            arr += (data["articles"])
            r = []
            data = []

        msg = 'Sorry. No news.'

        for res in arr:
            if keyword in res["title"]:
                result.append(res)
                msg = ''

        return render(request, 'fetchApi.html', {
            'keyword': keyword,
            'result': result,
            'searchFlg': searchFlg,
            'errormsg': msg,
            })

#　APIへのリクエストとレスポンスの受け取り（US版ニュース）
def fetchApiUs(request):

    apikey = "3156cce2dd144f1292bdfec6ce0a2161"
    searchFlg = False
    bookFlg = False
    result = []
    country = "us"

    
    if request.method == 'GET': 
        api = "https://newsapi.org/v2/top-headlines?country={co}&pageSize=100&apiKey={key}"

        url = api.format(co=country,key=apikey)
        r = requests.get(url)
        data = r.json()
        result = data["articles"]
        return render(request, 'fetchApiUs.html', {
            'result': result,
            'searchFlg': searchFlg,
            })

    
    elif 'category' in request.POST: 
        api = "https://newsapi.org/v2/top-headlines?country={co}&category={ca}&pageSize=100&apiKey={key}"
        category = request.POST['category']
        url = api.format(co=country, ca=category, key=apikey)
        r = requests.get(url)
        data = r.json()
        result = data["articles"]
        return render(request, 'fetchApiUs.html', {
            'result': result,
            'searchFlg': searchFlg,
            })

    elif 'keyword' in request.POST: 
        searchFlg = True
        keyword = request.POST['keyword']
        cons = ['business', 'science', 'entertainment', 'general', 'health', 'sport', 'technology']

        api = "https://newsapi.org/v2/top-headlines?country={co}&category={ca}&pageSize=100&apiKey={key}"
        arr = []
        for con in cons:
            url = api.format(co=country, ca=con, key=apikey)
            r = requests.get(url)
            data = r.json()
            arr += (data["articles"])
            r = []
            data = []

        msg = 'Sorry. No news.'

        for res in arr:
            if keyword in res["title"]:
                result.append(res)
                msg = ''

        return render(request, 'fetchApiUs.html', {
            'result': result,
            'searchFlg': searchFlg,
            'errormsg': msg
            })
    
    elif 'mark' in request.POST:
        bookFlg = True
        lists = bookmark.objects.filter(user=request.user, good=2)
        return render(request, 'fetchApi.html', {
                'lists': lists,
                })

def getArticles(request):
        api = "https://newsapi.org/v2/top-headlines?country=jp&pageSize=100&apiKey={key}"

        #リクエスト送信
        url = api.format(key=apikey)
        #レスポンスの格納
        r = requests.get(url)
        data = r.json()

        articles = data["articles"]
        return render(request, 'sample.html', {
            'articles': articles,
            })

def good(request):
        api = "https://newsapi.org/v2/top-headlines?country=jp&pageSize=100&apiKey={key}"

        #リクエスト送信
        url = api.format(key=apikey)
        #レスポンスの格納
        r = requests.get(url)
        data = r.json()

        articles = data["articles"]
        return render(request, 'sample.html', {
            'articles': articles,
            })