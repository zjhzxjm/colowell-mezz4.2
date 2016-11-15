from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Report

# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    list_display = ("bind", "risk", "muta_rate", "hgb")
    list_editable = ("risk", "muta_rate", "hgb")
    list_per_page = 15
    raw_id_fields = ('bind',)

    fieldsets = (
        (None, {
            "fields": ("bind",)
        }),
        (_("Report Result Admin"), {
            "fields": ("muta_rate", "hgb", "risk", "explanation")
        })
    )

admin.site.register(Report, ReportAdmin)