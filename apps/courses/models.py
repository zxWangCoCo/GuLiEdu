from django.db import models
from datetime import datetime
from orgs.models import TeacherIfo,OrgInfo

# Create your models here.
########################################课程表###########################################
class CourseInfo(models.Model):
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
    course_need = models.CharField(max_length=200,verbose_name="课程须知")
    teacher_tell = models.CharField(verbose_name="老师告诉你",max_length=200)
    orgInfo = models.ForeignKey(OrgInfo,verbose_name="所属机构")
    teacherIfo = models.ForeignKey(TeacherIfo,verbose_name="所属讲师")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

class LessonInfo(models.Model):
    name = models.CharField(verbose_name="章节名称",max_length=10)
    courseInfo = models.ForeignKey(CourseInfo,verbose_name="所属课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "章节信息"
        verbose_name_plural = verbose_name

class videoInfo(models.Model):
    name = models.CharField(verbose_name="视频名称", max_length=10)
    study_time = models.IntegerField(default=0,verbose_name="视频时长")
    lessonInfo = models.ForeignKey(LessonInfo,verbose_name="所属章节")
    url = models.URLField(default='http://www.atguigu.com',verbose_name="视频连接",max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "视频信息"
        verbose_name_plural = verbose_name


class SourceInfo(models.Model):
    name = models.CharField(verbose_name="资源名称",max_length=50)
    down_load = models.FileField(upload_to='source/',verbose_name="下载路径",max_length=200)
    courseInfo = models.ForeignKey(CourseInfo,verbose_name="所属课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "资源信息"
        verbose_name_plural = verbose_name

