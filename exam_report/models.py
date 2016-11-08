from django.db import models
from django.utils.translation import ugettext_lazy as _
from sample_bind.models import Bind
from mezzanine.core.fields import RichTextField

# Create your models here.


class Report(models.Model):
    risk = models.FloatField(_("Multiple_Risk"))
    muta_rate = models.FloatField(_("Mutation rate(%)"))
    hgb = models.FloatField(_("HGB(ug/ml)"))
    bind = models.OneToOneField(Bind, verbose_name=_("Sample code"))
    explanation = RichTextField(_("Explanation"))

    class Meta:
        verbose_name = _("report")
        verbose_name_plural = _("reports")

    def __str__(self):
        return "%s" % self.bind
