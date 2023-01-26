from django.core.exceptions import ValidationError


def validate_username(username):
    if username == 'me':
        raise ValidationError('Нельзя использовать username "me" !')
