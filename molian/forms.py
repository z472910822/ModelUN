from django import forms
from .models import Article#--
class ArticleForm(forms.ModelForm):
    class Meta:
        model =Article
        fields=('title','text','category')#对外暴露标题，内容和标签分类


