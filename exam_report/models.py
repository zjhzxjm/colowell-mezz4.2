from django.db import models
from django.utils.translation import ugettext_lazy as _
from sample_bind.models import Bind

# Create your models here.


class Report(models.Model):
    risk = models.FloatField(_("Multiple_Risk"))
    muta_rate = models.FloatField(_("Mutation rate"))
    hgb = models.FloatField(_("HGB"))
    bind = models.OneToOneField(Bind, verbose_name=_("Sample code"))
    explanation = models.TextField()

    class Meta:
        verbose_name = _("report")
        verbose_name_plural = _("reports")

    def __str__(self):
        return "%s %s %s" % (self.risk, self.muta_rate, self.hgb)
