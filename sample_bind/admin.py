from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from .models import Bind, Code
from sms.models import MyProfile
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from sms.conf import settings
import top
try:
    import json
except ImportError:
    from django.utils import simplejson as json


class CodeResource(resources.ModelResource):
    """
    Class for ImportExportModel
    """
    class Meta:
        model = Code
        fields = ('id', 'sample_code',)


class BindAdmin(admin.ModelAdmin):
    """
    Admin class for bind
    """
    list_display = ('code', 'user_id', 'full_name', 'submit_date', 'receive_date', 'receive_sms', 'analysis_date',
                    'finish_date', 'finish_sms', 'status_node')
    ordering = ['-receive_date']
    date_hierarchy = 'finish_date'
    actions = ['make_rec', 'make_ing', 'make_fin', 'delete_selected']
    list_filter = ['status_node']
    list_per_page = 15
    readonly_fields = ('code',)
    search_fields = ['code__sample_code', 'user__username', 'full_name']

    def make_rec(self, request, queryset):
        """
        1、批量操作已收样，记录时间戳，或用于回退操作，后续节点初始化数据
        2、调用阿里大鱼发送通知短信，密钥保存于sms conf中
        3、
        :param request:
        :param queryset:
        :return:
        """
        for obj in queryset:
            # print(MyProfile.objects.get(user_id=obj.user_id).mobile_phone)
            phone_num = int(MyProfile.objects.get(user_id=obj.user_id).mobile_phone)
            full_name = obj.full_name
            sample_code = obj.code.sample_code

            appkey = settings.ALIDAYU_APPKEY
            secret = settings.ALIDAYU_SECRET

            req = top.api.AlibabaAliqinFcSmsNumSendRequest()
            req.set_app_info(top.appinfo(appkey, secret))

            # req.extend = "123456"
            req.sms_type = "normal"
            req.sms_free_sign_name = "锐翌医学"
            req.sms_param = json.dumps({'name': full_name, 'code': sample_code})
            req.rec_num = phone_num
            req.sms_template_code = "SMS_8560712"
            try:
                resp = req.getResponse()
                self.message_user(request, _("%s 's sms has been sent successfully") % full_name)
                rows_updated = queryset.update(status_node='REC', receive_date=now(), receive_sms=True,
                                               analysis_date=None, finish_date=None)
                if rows_updated == 1:
                    message_bit = _("1 sample was")
                else:
                    message_bit = _("%s samples were") % rows_updated
                self.message_user(request, _("%s successfully marked as sample received,") % message_bit)
            except Exception as e:
                self.message_user(request, _("Fail to send sms: %s 's phone %s, Error: %s") % (full_name, phone_num, e))

    make_rec.short_description = _("Make selected samples as received")

    def make_ing(self, request, queryset):
        """
        1、批量操作分析中，记录时间戳，或用于回退操作，后续节点初始化数据
        2、新增记录值到 Report 数据表以便健康管理师操作 （待开发）
        :param request:
        :param queryset:
        :return:
        """
        rows_updated = queryset.update(status_node='ING', analysis_date=now(), finish_date=None)
        if rows_updated == 1:
            message_bit = _("1 sample was")
        else:
            message_bit = _("%s samples were") % rows_updated
        self.message_user(request, _("%s successfully marked as analysing,") % message_bit)
    make_ing.short_description = _("Make selected samples as analysing")

    def make_fin(self, request, queryset):
        """
        1、批量操作已完成，记录时间戳
        2、调用阿里大鱼发送通知短信，密钥保存于sms conf中
        :param request:
        :param queryset:
        :return:
        """
        for obj in queryset:
            # print(MyProfile.objects.get(user_id=obj.user_id).mobile_phone)
            phone_num = int(MyProfile.objects.get(user_id=obj.user_id).mobile_phone)
            full_name = obj.full_name
            sample_code = obj.code.sample_code

            appkey = settings.ALIDAYU_APPKEY
            secret = settings.ALIDAYU_SECRET

            req = top.api.AlibabaAliqinFcSmsNumSendRequest()
            req.set_app_info(top.appinfo(appkey, secret))

            # req.extend = "123456"
            req.sms_type = "normal"
            req.sms_free_sign_name = "锐翌医学"
            req.sms_param = json.dumps({'name': full_name, 'code': sample_code})
            req.rec_num = phone_num
            req.sms_template_code = "SMS_12841789"
            try:
                resp = req.getResponse()
                self.message_user(request, _("%s 's sms has been sent successfully") % full_name)
                rows_updated = queryset.update(status_node='FIN', finish_date=now(), finish_sms=True)
                if rows_updated == 1:
                    message_bit = _("1 sample was")
                else:
                    message_bit = _("%s samples were") % rows_updated
                self.message_user(request, _("%s successfully marked as finished") % message_bit)
            except Exception as e:
                self.message_user(request, _("Fail to send sms: %s 's phone %s, Error: %s") % (full_name, phone_num, e))

    make_fin.short_description = _("Make selected samples as finished")

    fieldsets = (
        (None, {
            'fields': ('code',)
        }),
        (_("Customer information"), {
            'fields': ('user', 'full_name')
        })
    )

admin.site.register(Bind, BindAdmin)


class CodeAdmin(ImportExportModelAdmin):
    """
    Admin class for code
    """
    resource_class = CodeResource
    list_display = ('sample_code', 'add_date', 'sold_out', 'sold_date')
    date_hierarchy = 'sold_date'
    actions = ['make_sold']
    list_filter = ['sold_out']
    list_per_page = 15

    def make_sold(self, request, queryset):
        """
        1、批量操作已售出，记录时间戳
        :param request:
        :param queryset:
        :return:
        """
        rows_updated = queryset.update(sold_out='True', sold_date=now())
        if rows_updated == 1:
            message_bit = _("1 code was")
        else:
            message_bit = _("%s codes were") % rows_updated
        self.message_user(request, _("%s successfully marked as sold,") % message_bit)
    make_sold.short_description = _("Make selected codes as sold")

    fieldsets = (
        (None, {
            'fields': ('sample_code',)
        }),
        # ('出货设置', {
        #     'fields': (('sold_out', 'sold_date'),)
        # }),
    )

admin.site.register(Code, CodeAdmin)

