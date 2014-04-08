from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def error_404(request, template_name = "404.html", **kwargs):
    context = RequestContext(request)
    return render_to_response(template_name, kwargs, context)


def error_500(request, template_name = "500.html", **kwargs):
    context = RequestContext(request)
    return render_to_response(template_name, kwargs, context)


def home(request):
    context = RequestContext(request)
    return render_to_response('base.html', {}, context)
