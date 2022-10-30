from django import forms

from uploader.validators import validate_file_extension, validate_data_format


class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[validate_file_extension, validate_data_format])