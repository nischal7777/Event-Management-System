from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AdminPanel(TemplateView):
    template_name="base/admin.html"

    def get(self, request):
        return render(request, self.template_name)