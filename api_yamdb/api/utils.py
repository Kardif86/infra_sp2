from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from users.models import User


def confirm_code_generator(username):
    """Генерируем confirmation_code и отправляем Email"""
    user = get_object_or_404(User, username=username)
    confirmation_code = User.objects.make_random_password()
    user.confirmation_code = confirmation_code
    user.save(update_fields=['confirmation_code'])

    send_mail(
        settings.MAIL_SUBJECT,
        confirmation_code,
        settings.FROM_EMAIL,
        [user.email],
        fail_silently=False
    )
