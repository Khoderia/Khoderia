from django.shortcuts import render
from django.views import View


class IndexView(View):
    """
    IndexView

    Target template: index.html

    Tasks to do:
        Lists projects and ideas
    """

    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, *args, **kwargs):
        return render(request, self.template_name)
        
