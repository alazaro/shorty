from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, View
from django.views.generic.edit import ModelFormMixin

from .models import ShortURL


class InfoView(DetailView):
    template_name = 'info.html'

    def get_object(self):
        return get_object_or_404(ShortURL, short=self.kwargs.get('url_hash'))


class IndexView(CreateView):
    template_name = 'index.html'
    model = ShortURL
    fields = ['original']

    def form_invalid(self, form):
        try:
            self.object = self.model.objects.get(
                original=form.data.get('original'))
            return super(ModelFormMixin, self).form_valid(form)
        except ShortURL.DoesNotExist:
            return super().form_invalid(form)


class RedirectView(View):
    def get(self, *args, **kwargs):
        url_hash = kwargs.get('url_hash')
        url = get_object_or_404(ShortURL, short=url_hash)
        return HttpResponseRedirect(url.original)
