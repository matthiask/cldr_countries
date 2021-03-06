from django.conf import settings
from django.db import models
from django.utils.functional import curry
from django.utils.translation import ugettext_lazy as _


from cldr_countries import data


COUNTRIES = getattr(settings, 'COUNTRIES', ('CH', 'DE', 'FR'))


CountryField = curry(models.CharField, _('country'), max_length=2,
    choices=[(c, data.countries[c]) for c in COUNTRIES])
