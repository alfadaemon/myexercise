from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, NumberInput
from django.forms.extras import SelectDateWidget
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from decimal import *
from datetime import datetime


class Exercise(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(_('Exercised on'), blank=True, null=True)
    starts = models.TimeField(_('Started'), auto_now=False, auto_now_add=False, null=True)
    ends = models.TimeField(_('Finished'), auto_now=False, auto_now_add=False, null=True)
    heart_rate = models.DecimalField(_('Average heart rate'), max_digits=5, decimal_places=2, default=0)
    description = models.CharField(_('Description'), max_length=128, null=True)

    #Men use the following formula:
    #Calories Burned = [(Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) -- 55.0969] x Time / 4.184.
    #Women use the following formula:
    #Calories Burned = [(Age x 0.074) -- (Weight x 0.05741) + (Heart Rate x 0.4472) -- 20.4022] x Time / 4.184.
    #get kcal/min
    #@property
    def get_burned_calories(self):
        start_dt = datetime(self.date.year, self.date.month, self.date.day, self.starts.hour, self.starts.minute,
                            self.starts.second)
        end_dt = datetime(self.date.year, self.date.month, self.date.day, self.ends.hour, self.ends.minute,
                            self.ends.second)
        time = (end_dt - start_dt)
        time = time.seconds/60  #convert to minutes
        if self.user.profile.gender == 'M':
            return (((self.user.profile.age * Decimal('0.2017')) +
                    (self.user.profile.weight * Decimal('0.09036')) +
                    (self.heart_rate * Decimal('0.6309')) - Decimal('55.0969')) *
                   (Decimal(time) / Decimal('4.184')))/60
        else:
            return (((self.user.age * Decimal('0.074')) +
                    (self.user.weight * Decimal('0.05741')) +
                    (self.heart_rate * Decimal('0.6309')) - Decimal('20.4022')) *
                   (Decimal(time) / Decimal('4.184')))/60

    burned_calories = property(get_burned_calories)


class ExerciseForm(ModelForm):
    calendar_widget = forms.widgets.DateInput(attrs={'class': 'date-pick'}, format='%m/%d/%Y')
    valid_time_formats = ['%P', '%H:%M%A', '%H:%M %A', '%H:%M%a', '%H:%M %a']

    class Meta:
        model = Exercise
        exclude = ['user']
        starts = forms.TimeField(required=False, widget=forms.widgets.TimeInput(attrs={'class': 'time-pick'}),
                                 help_text='ex: 10:30AM')
        ends = forms.TimeField(required=False, widget=forms.widgets.TimeInput(attrs={'class': 'time-pick'}),
                               help_text='ex: 11:30AM')
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 8}),
            'date': SelectDateWidget(),
            'heart_rate': NumberInput(),
        }