from django.shortcuts import HttpResponseRedirect
from uploader.forms import UploadFileForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from uploader.models import Person, Transaction

from uploader.parser import parse_sales


class UploadFileView(FormView):
    template_name = 'uploader/form.html'
    form_class = UploadFileForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            parse_sales(request.FILES['file'])
            return HttpResponseRedirect(self.success_url)


class TransactionListView(ListView):
    template_name = 'uploader/list.html'
    model = Transaction
