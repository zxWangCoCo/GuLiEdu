import xadmin
from .models import CityInfo,OrgInfo,TeacherIfo
################################城市###################################################
class CityInfoXadmin(object):
    list_display = ['name','add_time']

    # xadmin增加搜索框
    search_fields = ['name']

    # xadmin增加过滤器
    list_filter = ['name','add_time']

    model_icon = 'fa fa-asterisk'

##############################机构#####################################################
class OrgInfoXadmin(object):
    list_display = ['image','name','course_num','course_num','study_num','love_num','click_num','category','cityinfo']

    # xadmin增加搜索框
    search_fields = ['image','name','course_num','course_num','study_num','love_num','click_num','category','cityinfo']

    # xadmin增加过滤器
    list_filter = ['image','name','course_num','course_num','study_num','love_num','click_num','category','cityinfo']

    model_icon = 'fa fa-asterisk'

#####################################教师表############################################
class TeacherIfoXadmin(object):
    list_display = ['image', 'name', 'work_year', 'work_position','age', 'gender', 'love_num']

    search_fields = ['image', 'name', 'work_year', 'work_position', 'age', 'gender', 'love_num']

    list_filter = ['image', 'name', 'work_year', 'work_position', 'age', 'gender', 'love_num']

    model_icon = 'fa fa-asterisk'

xadmin.site.register(CityInfo,CityInfoXadmin)
xadmin.site.register(OrgInfo,OrgInfoXadmin)
xadmin.site.register(TeacherIfo,TeacherIfoXadmin)

