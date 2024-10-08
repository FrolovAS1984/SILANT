# Generated by Django 5.1 on 2024-08-25 08:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineBasicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=10, unique=True, verbose_name='Зав. No машины')),
                ('engine_serial_number', models.CharField(max_length=10, verbose_name='Зав. No двигателя')),
                ('transmission_serial_number', models.CharField(max_length=10, verbose_name='Зав. No трансмиссии')),
                ('driving_axle_serial_number', models.CharField(max_length=10, verbose_name='Зав. No ведущего моста')),
                ('steering_axle_serial_number', models.CharField(max_length=10, verbose_name='Зав. No управляемого моста')),
            ],
            options={
                'verbose_name': 'Машина базовая информация',
                'verbose_name_plural': 'Машины базовая информация',
            },
        ),
        migrations.CreateModel(
            name='MachineAllInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supply_contract_number', models.CharField(max_length=100, verbose_name='Договор поставки №, дата')),
                ('shipment_date', models.DateField(verbose_name='Дата отгрузки с завода')),
                ('consignee', models.CharField(max_length=100, verbose_name='Грузополучатель (конечный потребитель)')),
                ('operation_address', models.CharField(max_length=200, verbose_name='Адрес поставки (эксплуатации)')),
                ('configuration', models.TextField(verbose_name='Комплектация (доп. опции)')),
                ('client', models.ForeignKey(blank=True, limit_choices_to={'is_client': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_machines', to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('service_companies', models.ManyToManyField(limit_choices_to={'is_service_company': True}, related_name='serviced_machines', to=settings.AUTH_USER_MODEL, verbose_name='Сервисная компания')),
                ('machine', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ownership_info', to='app.machinebasicinfo', verbose_name='Машина')),
            ],
            options={
                'verbose_name': 'Машина полная информация',
                'verbose_name_plural': 'Машины полная информация',
            },
        ),
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directory_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Cправочник',
                'verbose_name_plural': 'Справочники',
                'unique_together': {('directory_name', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_performed', models.DateField(verbose_name='Дата проведения ТО')),
                ('hours_worked', models.IntegerField(verbose_name='Наработка, м/час')),
                ('order_number', models.CharField(max_length=50, verbose_name='№ заказ-наряда')),
                ('order_date', models.DateField(verbose_name='Дата заказ-наряда')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenances', to='app.machinebasicinfo', verbose_name='Машина')),
                ('maintenance_type', models.ForeignKey(limit_choices_to={'directory_name': 'Вид ТО'}, on_delete=django.db.models.deletion.RESTRICT, related_name='maintenances_type', to='app.references', verbose_name='Вид ТО')),
                ('performing_organization', models.ForeignKey(blank=True, limit_choices_to={'directory_name': 'Организация, проводившая ТО'}, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='maintenance_service_companies', to='app.references', verbose_name='Организация, проводившая ТО')),
            ],
            options={
                'verbose_name': 'ТО машины',
                'verbose_name_plural': 'ТО машины',
            },
        ),
        migrations.AddField(
            model_name='machinebasicinfo',
            name='driving_axle_model',
            field=models.ForeignKey(limit_choices_to={'directory_name': 'Модель ведущего моста'}, on_delete=django.db.models.deletion.RESTRICT, related_name='machines_driving_axle_basic', to='app.references', verbose_name='Модель ведущего моста'),
        ),
        migrations.AddField(
            model_name='machinebasicinfo',
            name='engine_model',
            field=models.ForeignKey(limit_choices_to={'directory_name': 'Модель двигателя'}, on_delete=django.db.models.deletion.RESTRICT, related_name='machines_engine_basic', to='app.references', verbose_name='Модель двигателя'),
        ),
        migrations.AddField(
            model_name='machinebasicinfo',
            name='model',
            field=models.ForeignKey(limit_choices_to={'directory_name': 'Модель техники'}, on_delete=django.db.models.deletion.RESTRICT, related_name='machines_model_basic', to='app.references', verbose_name='Модель техники'),
        ),
        migrations.AddField(
            model_name='machinebasicinfo',
            name='steering_axle_model',
            field=models.ForeignKey(limit_choices_to={'directory_name': 'Модель управляемого моста'}, on_delete=django.db.models.deletion.RESTRICT, related_name='machines_steering_axle_basic', to='app.references', verbose_name='Модель управляемого моста'),
        ),
        migrations.AddField(
            model_name='machinebasicinfo',
            name='transmission_model',
            field=models.ForeignKey(limit_choices_to={'directory_name': 'Модель трансмиссии'}, on_delete=django.db.models.deletion.RESTRICT, related_name='machines_transmission_basic', to='app.references', verbose_name='Модель трансмиссии'),
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failure_date', models.DateField(verbose_name='Дата отказа')),
                ('operating_hours', models.IntegerField(verbose_name='Наработка, м/час')),
                ('failure_description', models.TextField(verbose_name='Описание отказа')),
                ('spare_parts_used', models.TextField(blank=True, null=True, verbose_name='Используемые запасные части')),
                ('restoration_date', models.DateField(verbose_name='Дата восстановления')),
                ('downtime', models.IntegerField(editable=False, verbose_name='Время простоя техники')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='app.machinebasicinfo', verbose_name='Машина')),
                ('failure_node', models.ForeignKey(blank=True, limit_choices_to={'directory_name': 'Узел отказа'}, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='claim_failure_nodes', to='app.references', verbose_name='Узел отказа')),
                ('restoration_method', models.ForeignKey(blank=True, limit_choices_to={'directory_name': 'Способ восстановления'}, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='claim_restoration_methods', to='app.references', verbose_name='Способ восстановления')),
            ],
            options={
                'verbose_name': 'Рекламация',
                'verbose_name_plural': 'Рекламации',
            },
        ),
    ]
