from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_service_company = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    company_name = models.CharField(verbose_name='Название компании', max_length=150, blank=True)

    def __str__(self):
        return self.company_name if self.is_client or self.is_service_company else self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
