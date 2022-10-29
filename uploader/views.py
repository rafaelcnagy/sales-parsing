from uploader.forms import UploadFileForm
from django.views.generic.edit import FormView


class UploadFileView(FormView):
    template_name = 'uploader/form.html'
    form_class = UploadFileForm
    success_url = '/'
