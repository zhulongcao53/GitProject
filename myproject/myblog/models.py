#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin  
#from DjangoUeditor.models import UEditorField
 
# Create your models here.  
class Menulist(models.Model):
    MenuName = models.CharField(u'菜单标题', max_length = 20)
    MenuLogo = models.CharField(u'菜单图标', max_length = 20)
    Timestamp = models.DateTimeField(u'时间')  
    MenuUrl = models.CharField(u'菜单地址', max_length = 200)
    class Meta:
        verbose_name = u'博客菜单'
        verbose_name_plural = u'博客菜单'

    def __str__(self):
        return u'%s %s %s' % (self.MenuName, self.MenuLogo, self.MenuUrl)


class MenulistAdmin(admin.ModelAdmin):  
    list_display = ( 'MenuName', 'MenuLogo', 'MenuUrl', 'Timestamp') 
    list_filter = ('Timestamp',)        # 过滤器
    search_fields = ('MenuName', 'MenuLogo') #快速查询栏
    date_hierarchy = 'Timestamp'
    ordering = ('-Timestamp',)

class Blog(models.Model):  
    Title = models.CharField(u'标题', max_length = 150)  
    Content = models.CharField(u'内容', max_length = 2000)
    Category = models.CharField(u'标签', max_length = 50, blank = True)
    Timestamp = models.DateTimeField(u'时间')  

    class Meta:
        ordering =('-Timestamp',)   #以最新时间显示
        verbose_name = u'博客文章'
        verbose_name_plural = u'博客文章'

    def __str__(self):
        return u'%s %s' % (self.Title, self.Timestamp)

class BlogAdmin(admin.ModelAdmin):  
    list_display = ( 'Title', 'Content', 'Category', 'Timestamp')  #后台blog栏目显示内容
    list_filter = ('Timestamp',)        # 过滤器
    search_fields = ('Title', 'Content', 'Category') #快速查询栏
    date_hierarchy = 'Timestamp'
    ordering = ('-Timestamp',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Menulist,MenulistAdmin)  
