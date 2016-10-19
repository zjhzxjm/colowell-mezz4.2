from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages import info
from django.utils.translation import ugettext_lazy as _

from sample_bind.forms import BindForm
from sample_bind.models import Bind, Code


@login_required
def index(request, template="sample_bind/index.html"):
    """
    sample_bind/index.html 显示绑定的样品信息
    :param request:
    :param template:
    :return:
    """
    user_id = request.user.id
    bind_lists = Bind.objects.all().filter(user_id=user_id)
    context = {"bind_lists": bind_lists, "title": _("My COLOWELL")}
    return render(request, template, context)


@login_required
def results(request, user_id):
    """
    不开发
    :param request:
    :param user_id:
    :return:
    """
    response = "You are looking at the results of binding %s."
    return HttpResponse(response % user_id)


@login_required
def bind(request, template="sample_bind/sample.html"):
    """
    sample_bind/sample.html 样品绑定界面Bind a sample code
    """
    if request.method == 'POST':
        form = BindForm(request.POST)
        if form.is_valid():
            obj_bind = form.get_bind_object()
            obj_bind.user = request.user
            obj_bind.save()
            info(request, _("Bind the sample code successfully"))
            return HttpResponseRedirect("/sample_bind")
    else:
        form = BindForm()

    context = {"form": form, "title": _("Sample bind")}

    return render(request, template, context)


