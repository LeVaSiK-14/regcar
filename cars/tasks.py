from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_mail_to_worker(email, car_id):
    send_mail(subject='Работай ',
                message=f'Работы валом а ты не делаешь, Id = {car_id}',
                recipient_list=[email, ],
                from_email=None)