from django.db import models
from django.utils import timezone#默认为时区时间，引入内置的timezone模块
from django.contrib.auth.models import User
# Create your models here.
#生成数据表
#python manage.py makemigrations + appname
#python manage.py migrate + appname//数据表迁移
class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)#不加后面这句话会报错
    title=models.CharField(max_length=200)#标题
    category=models.CharField(max_length=50,blank=True)#标签
    text=models.TextField()#文章内容
    created_date =models.DateTimeField(default=timezone.now)#默认为时区时间
    published_date=models.DateTimeField(blank=True,null=True)
    def publish(self):#用publish方法发布文章
        self.published_date=timezone.now()
        self.save()
    def _str_(self):
        return self.title#告诉系统使用title这个字段来表示这个Article对象的
    ###charFiled：普通的文本，用来存储字符串,max_length设置最大长度
    #TextField:长文本，存储大量文本
    #DateTimeField:日期时间类型，default=timezone.now表示默认时间就是系统当前时间
    #ForeignKey:外键类型
    ###
