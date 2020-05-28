#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin  
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
#from DjangoUeditor.models import UEditorField
 
# Create your models here. 

class About(models.Model):
    AboutName = models.CharField(u'姓名', max_length = 20)
    Birthday = models.CharField(u'出生日期', max_length = 20)
    Nationality = models.CharField(u'国籍', max_length = 20)
    Introduce = models.CharField(u'介绍', max_length = 500)
    Timestamp = models.DateTimeField(u'时间')
    class Meta:
        verbose_name = u'自我介绍'
        verbose_name_plural = u'自我介绍'
    
    def __str__(self):
        return u'%s %s %s %s' % (self.AboutName, self.Birthday, self.Nationality, self.Introduce)


class AboutAdmin(admin.ModelAdmin):
    list_display = ( 'AboutName', 'Birthday', 'Nationality', 'Introduce', 'Timestamp')
    list_filter = ('Timestamp',)        # 过滤器
    search_fields = ('AboutName','Nationality') #快速查询栏
    date_hierarchy = 'Timestamp'
    ordering = ('-Timestamp',)


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
    #Category = models.CharField(u'标签', max_length = 50, blank = True)
    Category = models.ForeignKey('BlogType', on_delete=models.CASCADE, verbose_name = '标签')
    Timestamp = models.DateTimeField(u'时间')  
    avatar_thumbnail = ProcessedImageField(upload_to='images',
                                           processors=[ResizeToFill(540, 303)],
                                           format='JPEG',
                                           options={'quality': 90},null = True, blank = True, verbose_name = '图片')     
    
    class Meta:
        ordering =('-Timestamp',)   #以最新时间显示
        verbose_name = u'博客文章'
        verbose_name_plural = u'博客文章'
    
    def __str__(self):
        return u'%s %s' % (self.Title, self.Timestamp)

class BlogAdmin(admin.ModelAdmin):  
    list_display = ( 'Title', 'Content', 'Category', 'avatar_thumbnail', 'Timestamp')  #后台blog栏目显示内容
    list_filter = ('Timestamp',)        # 过滤器
    search_fields = ('Title', 'Content', 'Category') #快速查询栏
    date_hierarchy = 'Timestamp'
    ordering = ('-Timestamp',)

class BlogType(models.Model):
    Category = models.CharField(u'标签', max_length = 50, blank = True)
    Timestamp = models.DateTimeField(u'时间')
    
    class Meta:
        ordering =('-Timestamp',)   #以最新时间显示
        verbose_name = u'文章标签'
        verbose_name_plural = u'文章标签'
    
    def __str__(self):
        return u'%s' % (self.Category)

class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ( 'Category', 'Timestamp')  #后台blog栏目显示内容
    list_filter = ('Timestamp',)        # 过滤器
    date_hierarchy = 'Timestamp'
    ordering = ('-Timestamp',)


class Photo(models.Model):
    Title = models.CharField(u'标题', max_length = 150) 
    Category = models.ForeignKey('PhotoType', on_delete=models.CASCADE, verbose_name = '标签')
    avatar_thumbnail = ProcessedImageField(upload_to='images',
                                           processors=[ResizeToFill(100, 50)],
                                           format='JPEG',
                                           options={'quality': 90}, verbose_name = '图片')    
    Timestamp = models.DateTimeField(u'时间')    
    
    class Meta:
        ordering =('-Timestamp',)   #以最新时间显示
        verbose_name = u'图片分享'
        verbose_name_plural = u'图片分享'
    
    def __str__(self):
        return u'%s %s %s' % (self.Title, self.avatar_thumbnail, self.Timestamp)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ( 'Title', 'avatar_thumbnail', 'Category', 'Timestamp')  #后台blog栏目显示内容
    list_filter = ('Timestamp',)        # 过滤器
    search_fields = ('Title', 'Category') #快速查询栏
    date_hierarchy = 'Timestamp'
    ordering = ('-Timestamp',)

class PhotoType(models.Model):
    Category = models.CharField(u'标签', max_length = 50, blank = True)
    Timestamp = models.DateTimeField(u'时间')
    
    class Meta:
        ordering =('-Timestamp',)   #以最新时间显示
        verbose_name = u'图片标签'
        verbose_name_plural = u'图片标签'
    
    def __str__(self):
        return u'%s' % (self.Category)

class PhotoTypeAdmin(admin.ModelAdmin):
    list_display = ( 'Category', 'Timestamp')  #后台blog栏目显示内容
    list_filter = ('Timestamp',)        # 过滤器
    date_hierarchy = 'Timestamp'
    ordering = ('-Timestamp',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogType, BlogTypeAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoType, PhotoTypeAdmin)
admin.site.register(Menulist,MenulistAdmin) 
admin.site.register(About, AboutAdmin)
