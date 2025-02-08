import html
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .models import Applicant
from .forms import JobApplicationForm

class JobAppView(CreateView):
    model = Applicant
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')

class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'