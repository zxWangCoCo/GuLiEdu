from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser) :
    #头像
    image = models.ImageField(upload_to='user/',max_length=200,verbose_name="用户头像",null=True,blank=True)
    #昵称
    nick_name = models.CharField(max_length=20,verbose_name="用户昵称",null=True,blank=True)
    #生日
    birthday = models.DateTimeField(verbose_name="用户生日",null=True,blank=True)
    #性别
    gender = models.CharField(choices=(('girl','女'),('boy','男')),max_length=10,verbose_name="用户性别",default='gril')
    #会员地址
    address = models.CharField(max_length=20,verbose_name="地址",null=True,blank=True)
    #会奥运手机
    phone = models.CharField(max_length=11,verbose_name="用户手机",null=True,blank=True)
    #创建时间
    add_time = models.DateTimeField(default=datetime.now,verbose_name="创建时间")

    def __str__(self):
        return self.username

    class Meta :
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
########################################################################################################################
    #轮播
class BannerInfo(models.Model) :
    #轮播图片
    image = models.ImageField(upload_to='banner/',verbose_name="轮播图片",max_length=200)
    #链接地址
    url = models.URLField(default='http://www.atguigu.com',verbose_name="图片链接",max_length=200)
    # 创建时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = '轮播图信息'
        verbose_name_plural = verbose_name
########################################################################################################################
#邮箱验证
class EmailVerifyCode(models.Model) :
     code = models.CharField(max_length=20,verbose_name="邮箱验证码")
     email = models.EmailField(max_length=200,verbose_name="验证邮箱")