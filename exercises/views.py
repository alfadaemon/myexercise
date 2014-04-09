from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from exercises.models import Exercise, ExerciseForm


@login_required
def dashboard(request):
    context = RequestContext(request)
    workouts = Exercise.objects.filter(user=request.user).order_by('date', 'starts')
    return render_to_response('exercises/dashboard.html', {'workouts': workouts}, context)

@login_required
def workout(request):
    context = RequestContext(request)
    if request.method == 'POST':
        exercise = Exercise()
        exercise.user = request.user
        form_exercise = ExerciseForm(request.POST, instance=exercise)
        if form_exercise.is_valid():
            form_exercise.save()
            return HttpResponseRedirect('/exercises/')
        else:
            return render_to_response('exercises/workout.html', {'form': form_exercise}, context)

    form = ExerciseForm()
    return render_to_response('exercises/workout.html', {'form': form}, context)
