from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from exam_report.models import Report
from sample_bind.models import Code, Bind

# Create your views here.


def report(request, sample_code=None, template="exam_report/report.html"):
    if not sample_code:
        raise Http404

    try:
        bind_lists = Bind.objects.filter(code=Code.objects.filter(sample_code=sample_code)[0].id).filter(user_id=
                                                                                                         request.user.id)
        report_lists = Report.objects.filter(bind=bind_lists[0].id)
        progress_rate = report_lists[0].risk/15*100
        context = {'progress_rate': progress_rate, 'report_list': report_lists[0], 'bind_list': bind_lists[0], 'title': _('Colon Examing Report')}
    except IndexError:
        raise Http404

    return render(request, template, context)
