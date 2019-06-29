from django.shortcuts import render,redirect
from .forms import ArticleForm
from .models import Article
from django.http.response import HttpResponse,JsonResponse
import json
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.
#API接口，当收到get请求时，返回全部文章信息
def getAllArticles(request):
    if request.method == "GET":
        queryset =Article.objects.all()
        resList = []
        for i in queryset:
            resList += [{
                'author': i.author.username,
                'title': i.title,
                'text':i.text,
                'published_date':i.published_date,
                'created_date':i.created_date,
            }]
        return JsonResponse(resList, safe=False)
def post_new(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('post_detail',pk=post.pk)
        else:
            form =ArticleForm()
    return render(request,'post_new.html',{'form':form})
def base(request):
    return render(request,'base.html')
def post_list(request):
    posts=Article.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request,'post_list.html',{'posts':posts})
