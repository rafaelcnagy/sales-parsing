import os
import re
from django.core.exceptions import ValidationError
from sqlalchemy import null

def validate_file_extension(file) -> null:
    ''' Check if file extension is .txt '''
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.txt']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_data_format(file) -> null:
    ''' Check data format matchs with pattern '''
    pattern = re.compile('^\d\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}\-\d{2}:\d{2}.{30}\d{10}.+$')
    for line in file:
        if not pattern.match(line.decode('utf-8')) and line != b'\n':
            raise ValidationError('Invalid data.')

