from django import forms
from sample_bind.models import Bind, Code
from django.utils.translation import ugettext_lazy as _


def validate_code(sample_code):
    """
    1、检查是否重复绑定样品编号
    2、判断样品编号是否正确
    :param sample_code:
    :return: raise error
    """
    for e in Bind.objects.all():
        if sample_code == str(e.code):
            raise forms.ValidationError(_("This code has been bound"))
        else:
            try:
                Code.objects.exclude(sold_out=False).get(sample_code=sample_code)
            except Code.DoesNotExist:
                raise forms.ValidationError(_("Invalid sample code"))


class BindForm(forms.Form):
    """
    Form class for bind
    """
    # RELATION_NAME = (
    #     ('ME', '本人'),
    #     ('FA', '父亲'),
    #     ('MO', '母亲'),
    #     ('DA', '女儿'),
    #     ('SO', '儿子'),
    #     ('OT', '其他'),
    # )

    sample_code = forms.CharField(label=_('Sample code'), max_length=12, required=True, validators=[validate_code])
    # relation_name = forms.CharField(label='关系', max_length=5, widget=forms.Select(choices=RELATION_NAME),
    #                                 required=True)
    full_name = forms.CharField(label=_('Full name'), max_length=20, required=True)

    def get_bind_object(self):
        """
        获取bind对象
        :return: bind object
        """
        if not self.is_valid():
            raise ValueError("get_bind_object may only be called on valid forms")

        bind_model = self.get_bind_model()
        obj_bind = bind_model(**self.get_bind_create_data())
        sample_code = self.cleaned_data['sample_code']
        obj_code = Code.objects.exclude(sold_out=False).get(sample_code=sample_code)
        obj_bind.code = obj_code

        return obj_bind

    def get_bind_model(self):
        return Bind

    def get_bind_create_data(self):
        return dict(
            full_name=self.cleaned_data["full_name"],
        )

