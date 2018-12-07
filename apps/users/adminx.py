import xadmin
from xadmin import views
from .models import BannerInfo,EmailVerifyCode

class BannerInfoXadmin(object) :
    list_display = ['image','url','add_time']

    #xadmin增加搜索框
    search_fields = ['image','url','add_time']

    #xadmin增加过滤器
    list_filter = ['image','url','add_time']

    model_icon = 'fa fa-user'
########################################################################################################################
#邮箱验证
class EmailVerifyCodeXadmin(object) :
    list_display = ['code', 'email', 'send_type','add_time']

    model_icon = 'fa fa-user'

#配置胡天管理系统开关开启
class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True #启用bootstarp自己的主题

class GlobalSettings(object):
    site_title="后台管理系统" #更改后台名称
    site_footer="青岛联众科技有限公司"#更改后台尾部名称
    menu_style="accordion"#设置折叠效果

#注册到xadmin
xadmin.site.register(BannerInfo,BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeXadmin)
#试修改的样式生效
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)