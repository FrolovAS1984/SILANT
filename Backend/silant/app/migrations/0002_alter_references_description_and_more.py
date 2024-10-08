# Generated by Django 5.1 on 2024-08-25 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='references',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='references',
            name='directory_name',
            field=models.CharField(max_length=100, verbose_name='Название справочника'),
        ),
        migrations.AlterField(
            model_name='references',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
