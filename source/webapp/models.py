from django.contrib.auth import get_user_model
from django.db import models


class Message(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='author_message',
                                                on_delete=models.CASCADE, verbose_name='Автор')
    recipient = models.ForeignKey(get_user_model(), related_name='recipient_message',
                                                   on_delete=models.CASCADE, verbose_name='Получатель')
    description = models.TextField(max_length=2000, verbose_name='Текст сообщения')
