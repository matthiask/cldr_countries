from django.db import models
from django.utils.functional import curry
from django.utils.translation import ugettext_lazy as _


from cldr_countries import data


COUNTRIES = ('CH', 'DE', 'FR')


def get_countries():
    for c in COUNTRIES:
        yield (c, data.countries[c])


CountryField = curry(models.CharField, _('country'), max_length=2, choices=get_countries())
