import xadmin
from xadmin import views
from .models import BannerInfo,EmailVerifyCode

class BannerInfoXadmin(object) :
    list_display = ['image','url','add_time']

    #xadmin增加搜索框
    search_fields = ['image','url','add_time']

    #xadmin增加过滤器
    list_filter = ['image','url','add_time']
########################################################################################################################
#邮箱验证
class EmailVerifyCodeXadmin(object) :
    list_display = ['code', 'email', 'send_type','add_time']

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title="后台管理系统" #更改后天名称
    site_footer="青岛联众科技有限公司"
    menu_style="accordion"

#注册到xadmin
xadmin.site.register(BannerInfo,BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeXadmin)
#试修改的样式生效
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)