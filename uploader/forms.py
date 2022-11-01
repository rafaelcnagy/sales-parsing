from django import forms

from uploader.validators import validate_file_extension, validate_data_format


class UploadFileForm(forms.Form):
    """
    Form for upload of file.

    @file [FileField]: uploaded file, with extension and data format validators
    """
    file = forms.FileField(validators=[validate_file_extension, validate_data_format])