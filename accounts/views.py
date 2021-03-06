from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = RequestContext(request)
    return render_to_response('base.html', {}, context)
