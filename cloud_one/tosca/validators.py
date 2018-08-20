from django.core.exceptions import ValidationError
import magic

def validate_file(file):
    filetype = magic.from_buffer(file.read())
    if not "YML" or "YAML" in filetype:
        raise ValidationError("File is not YAML.")
    return file