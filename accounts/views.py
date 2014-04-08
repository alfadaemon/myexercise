from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    context = RequestContext(request)
    return render_to_response('base.html', {}, context)
