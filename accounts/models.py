from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

from datetime import date


class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES, default=MALE)
    birth_date = models.DateField(_('Date Of Birth'), blank=True, null=True)
    weight = models.DecimalField(_('Weight in Kg'), max_digits=5, decimal_places=2, default=0)
    height = models.DecimalField(_('Height in cms'), max_digits=5, decimal_places=2, default=0)

    def get_age(self):
        if self.birth_date:
            born = self.birth_date
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        else:
            return 0

    age = property(get_age)
