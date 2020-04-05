from django.shortcuts import render
from django.views.generic import TemplateView

import random
import time

from przyklad.models import Pomysl


class Widok1(TemplateView):
    template_name = "przyklad/widok1.html"

    def get_context_data(self, **kwargs):
        return {
            "parametr": random.randint(10, 90),
            "czas": time.ctime(),
            "pomysly": Pomysl.objects.all()
        }
