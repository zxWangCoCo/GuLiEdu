from django.db import models

# Create your models here.
########################################课程表###########################################
class Course(models.Model):
    image = models.ImageField(upload_to='course/',max_length=200,verbose_name="课程封面")
    name = models.CharField(max_length=20,verbose_name="课程名称")
    study_time = models.IntegerField(default=0,verbose_name="学习时长")
    study_num = models.IntegerField(default=0,verbose_name="学习人数")
    leave = models.CharField(choices=(('gj',"高级"),('zj',"中级"),('cj',"初级")),max_length=5,verbose_name="课程难度")
    love_num = models.IntegerField(default=0,verbose_name="收藏量")
    click_num = models.IntegerField(default=0,verbose_name="点击量")
    desc = models.CharField(max_length=200,verbose_name="课程简介")
    detail = models.TextField(verbose_name="课程详情")
    category = models.CharField(choices=(('qd',"前端"),('hd',"后端")),max_length=6,verbose_name="课程分类")
    course_notice = models.CharField(max_length=200,verbose_name="课程公告")