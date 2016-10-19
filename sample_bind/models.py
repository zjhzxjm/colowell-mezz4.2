from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Code(models.Model):
    """
    Code class
    """
    sample_code = models.CharField(_("Sample code"), max_length=12, unique=True)
    sold_out = models.BooleanField(_("Sold out"), default=False)
    add_date = models.DateTimeField(_("Add date"), auto_now_add=True)
    sold_date = models.DateTimeField(_("Sold date"), null=True)

    class Meta:
        verbose_name = _("code")
        verbose_name_plural = _("codes")

    def __str__(self):
        return "%s" % self.sample_code


class Bind(models.Model):
    """
    Bind class
    """
    code = models.OneToOneField(Code, verbose_name=_("Sample code"))
    submit_date = models.DateTimeField(_("Submit date"), auto_now_add=True)
    receive_date = models.DateTimeField(_("Receive date"), null=True)
    receive_sms = models.BooleanField(_("Receive sms send"), default=False)
    analysis_date = models.DateTimeField(_("Analysis date"), null=True)
    finish_date = models.DateTimeField(_("Finish date"), null=True)
    finish_sms = models.BooleanField(_("Finish sms send"), default=False)
    # status_date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, verbose_name=_("User"))
    # RELATION_NAME = (
    #     ('ME', 'Self'),
    #     ('FA', 'Father'),
    #     ('MO', 'Mother'),
    #     ('DA', 'Daughter'),
    #     ('SO', 'Son'),
    #     ('OT', 'Other relatives'),
    # )
    full_name = models.CharField(_("Full name"), max_length=10)
    # relation_name = models.CharField(max_length=2,
    #                                  choices=RELATION_NAME)
    STATUS_NODE = (
        ('SAM', _("Sampling")),
        ('REC', _("Received")),
        ('ING', _("Analysing")),
        ('FIN', _("Finished")),
    )
    status_node = models.CharField(_("Status"), max_length=3,
                                   choices=STATUS_NODE,
                                   default='SAM')

    class Meta:
        verbose_name = _("bind")
        verbose_name_plural = _("binds")

    def __str__(self):
        # return "%s %s %s %s" % (self.code, self.status_node, self.full_name, self.relation_name)
        return "%s" % self.code
