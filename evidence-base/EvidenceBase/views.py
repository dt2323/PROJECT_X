from django.views.generic import TemplateView


#These are tests for logged in and logged out views.
class TestPage(TemplateView):
    template_name = "tests.html"

class ThanksPage(TemplateView):
    template_name = "thanks.html"

#This is a class that inherits from TemplateView
class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
