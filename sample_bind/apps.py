from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SampleBindConfig(AppConfig):
    name = 'sample_bind'
    verbose_name = _("Sample Bind Manage")
