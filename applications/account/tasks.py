from decouple import config
from django.core.mail import send_mail
from config.celery import app


@app.task
def send_activation_code(email, code):

    message = f'Привет, ваш код для активации аккаунта, никому не показывайте его<br><strong style="font-size: 40px;">{code}</strong><br>'

    send_mail(
        'Activation code',
        '',
        f'{config("EMAIL_HOST_USER")}',
        [email],
        html_message=message
    )


@app.task
def send_forgot_password_code(email, code):
    message = f'Ваш код для восстановления пароля, никому не показывайте его: <br><strong style="font-size: 40px;">{code}</strong><br>'
    send_mail(
        'Password change code',
        '',
        f'{config("EMAIL_HOST_USER")}',
        [email],
        html_message=message
    )
