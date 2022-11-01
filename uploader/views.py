from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from uploader.forms import UploadFileForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from uploader.models import Person, Transaction
from django.contrib import messages

from uploader.parser import parse_sales


class UploadFileView(FormView):
    template_name = 'uploader/form.html'
    form_class = UploadFileForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        # This function calls the parsing and redirect with messages
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            try:
                parse_sales(request.FILES['file'])
                messages.success(request, 'Transações adicionadas com sucesso.')
                return HttpResponseRedirect(self.success_url)
            except:
                messages.error(request, 'Erro ao processar o arquivo.')
                return HttpResponseRedirect(reverse_lazy('upload'))
        else:
            messages.error(request, 'Arquivo é invalido.')
            return HttpResponseRedirect(reverse_lazy('upload'))

class TransactionListView(ListView):
    template_name = 'uploader/list.html'
    model = Transaction

    def get_queryset(self):
        transactions = super().get_queryset() 
        persons = Person.objects.all()

        queryset = {
            'transactions': transactions,
            'persons': persons,
        }

        return queryset

class TransactionListPersonView(ListView):
    template_name = 'uploader/list.html'
    model = Transaction

    def get_queryset(self):
        transactions = super().get_queryset() 
        
        person = Person.objects.get(id=self.kwargs['id'])
        transactions = transactions.filter(person=person)

        persons = Person.objects.all()

        queryset = {
            'transactions': transactions,
            'persons': persons,
            'person_selected': person
        }

        return queryset
