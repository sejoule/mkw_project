from django.core.exceptions import ValidationError
import magic

def validate_file(file):
    filetype = magic.from_buffer(file.read())
    if not "JPG" or "JPEG" in filetype:
        raise ValidationError("File should be JPEG.")
    return file