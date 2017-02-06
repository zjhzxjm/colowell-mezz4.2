from django.db import models
from django.utils.translation import ugettext_lazy as _
from sample_bind.models import Bind
from mezzanine.core.fields import RichTextField

# Create your models here.


class Report(models.Model):
    risk = models.FloatField(_("Multiple_Risk"), help_text='0~0.8 低于平均风险；0.8~1.2 平均风险；1.2~5 低风险；5~15 中等风险； ≥15 高风险')
    muta_rate = models.FloatField(_("Mutation rate(%)"), help_text='不适用于贵州版本')
    hgb = models.FloatField(_("HGB(ug/ml)"), help_text='不适用于贵州版本')
    bind = models.OneToOneField(Bind, verbose_name=_("Sample code"))
    explanation = RichTextField(_("Explanation"))

    class Meta:
        verbose_name = _("report")
        verbose_name_plural = _("reports")

    def __str__(self):
        return "%s" % self.bind
