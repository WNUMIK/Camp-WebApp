from django import forms
from django.forms.models import inlineformset_factory
from . import models

ModuleFormSet = inlineformset_factory(models.Camping,
                                      models.Type,
                                      fields=('name', 'description'),
                                      extra=2,
                                      can_delete=True
                                      )
