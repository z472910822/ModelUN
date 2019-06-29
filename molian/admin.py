from django.contrib import admin
import xadmin
from .models import Article
# Register your models here.
#注册相应的模型,方便后台管理
xadmin.site.register(Article)
