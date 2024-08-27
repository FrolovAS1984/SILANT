from django.db import models
from accounts.models import User

"""Модель справочников"""


class References(models.Model):
    directory_name = models.CharField(max_length=100, verbose_name='Название справочника')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        unique_together = ('directory_name', 'name')
        verbose_name = 'Cправочник'
        verbose_name_plural = 'Справочники'

    def __str__(self):
        return f"{self.directory_name}: {self.name}"


"""Базовая модель машины, доступная неавторизованным пользователям"""


class MachineBasicInfo(models.Model):
    serial_number = models.CharField(max_length=10, unique=True, verbose_name='Зав. No машины')
    model = models.ForeignKey(References, on_delete=models.RESTRICT, related_name='machines_model_basic',
                              limit_choices_to={'directory_name': 'Модель техники'}, verbose_name='Модель техники')
    engine_model = models.ForeignKey(References, on_delete=models.RESTRICT, related_name='machines_engine_basic',
                                     limit_choices_to={
                                         'directory_name': 'Модель двигателя'}, verbose_name='Модель двигателя')
    engine_serial_number = models.CharField(max_length=10, verbose_name='Зав. No двигателя')
    transmission_model = models.ForeignKey(References, on_delete=models.RESTRICT,
                                           related_name='machines_transmission_basic',
                                           limit_choices_to={'directory_name': 'Модель трансмиссии'},
                                           verbose_name='Модель трансмиссии')
    transmission_serial_number = models.CharField(max_length=10, verbose_name='Зав. No трансмиссии')
    driving_axle_model = models.ForeignKey(References, on_delete=models.RESTRICT,
                                           related_name='machines_driving_axle_basic',
                                           limit_choices_to={'directory_name': 'Модель ведущего моста'},
                                           verbose_name='Модель ведущего моста')
    driving_axle_serial_number = models.CharField(max_length=10, verbose_name='Зав. No ведущего моста')
    steering_axle_model = models.ForeignKey(References, on_delete=models.RESTRICT,
                                            related_name='machines_steering_axle_basic',
                                            limit_choices_to={'directory_name': 'Модель управляемого моста'},
                                            verbose_name='Модель управляемого моста')
    steering_axle_serial_number = models.CharField(max_length=10, verbose_name='Зав. No управляемого моста')

    def __str__(self):
        return self.serial_number

    class Meta:
        verbose_name = 'Машина базовая информация'
        verbose_name_plural = 'Машины базовая информация'


"""Полная модель машины, доступная авторизованным пользователям"""


class MachineAllInfo(models.Model):
    machine = models.OneToOneField(MachineBasicInfo,
                                   on_delete=models.CASCADE,
                                   related_name='ownership_info',
                                   verbose_name='Машина')
    supply_contract_number = models.CharField(max_length=100, verbose_name='Договор поставки №, дата')
    shipment_date = models.DateField(verbose_name='Дата отгрузки с завода')
    consignee = models.CharField(max_length=100, verbose_name='Грузополучатель (конечный потребитель)')
    operation_address = models.CharField(max_length=200, verbose_name='Адрес поставки (эксплуатации)')
    configuration = models.TextField(verbose_name='Комплектация (доп. опции)')

    client = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, blank=True, related_name='owned_machines',
                               limit_choices_to={'is_client': True},
                               verbose_name='Клиент')
    service_companies = models.ManyToManyField(User, related_name='serviced_machines',
                                               limit_choices_to={'is_service_company': True},
                                               verbose_name='Сервисная компания')

    def __str__(self):
        return f"{self.machine.serial_number}"

    class Meta:
        verbose_name = 'Машина полная информация'
        verbose_name_plural = 'Машины полная информация'


"""Модель ТО машины"""


class Maintenance(models.Model):
    machine = models.ForeignKey(MachineBasicInfo, on_delete=models.CASCADE,
                                related_name='maintenances',
                                verbose_name='Машина')
    maintenance_type = models.ForeignKey(References, on_delete=models.RESTRICT,
                                         related_name='maintenances_type',
                                         limit_choices_to={'directory_name': 'Вид ТО'},
                                         verbose_name='Вид ТО')
    date_performed = models.DateField(verbose_name='Дата проведения ТО')
    hours_worked = models.IntegerField(verbose_name='Наработка, м/час')
    order_number = models.CharField(max_length=50, verbose_name='№ заказ-наряда')
    order_date = models.DateField(verbose_name='Дата заказ-наряда')
    performing_organization = models.ForeignKey(References, null=True, blank=True, on_delete=models.RESTRICT,
                                                related_name='maintenance_service_companies',
                                                limit_choices_to={'directory_name': 'Организация, проводившая ТО'},
                                                verbose_name='Организация, проводившая ТО')

    def __str__(self):
        maintenance_type_name = self.maintenance_type.name if self.maintenance_type else 'Unknown'
        performing_org_name = self.performing_organization.name if self.performing_organization else 'Unknown'
        return f"{maintenance_type_name} on {self.date_performed} by {performing_org_name}"

    class Meta:
        verbose_name = 'ТО машины'
        verbose_name_plural = 'ТО машины'


"""Модель рекламаций"""


class Complaints(models.Model):
    machine = models.ForeignKey(MachineBasicInfo, on_delete=models.CASCADE,
                                related_name='claims',
                                verbose_name='Машина')
    failure_date = models.DateField(verbose_name='Дата отказа')
    operating_hours = models.IntegerField(verbose_name='Наработка, м/час')
    failure_node = models.ForeignKey(References, null=True, blank=True, on_delete=models.RESTRICT,
                                     related_name='claim_failure_nodes',
                                     limit_choices_to={'directory_name': 'Узел отказа'},
                                     verbose_name='Узел отказа')
    failure_description = models.TextField(verbose_name='Описание отказа')
    restoration_method = models.ForeignKey(References, null=True, blank=True, on_delete=models.RESTRICT,
                                           related_name='claim_restoration_methods',
                                           limit_choices_to={'directory_name': 'Способ восстановления'},
                                           verbose_name='Способ восстановления')
    spare_parts_used = models.TextField(blank=True, null=True, verbose_name='Используемые запасные части')
    restoration_date = models.DateField(verbose_name='Дата восстановления')
    downtime = models.IntegerField(editable=False, verbose_name='Время простоя техники')

    def __str__(self):
        return f"{self.failure_node} - {self.failure_date}"

    def save(self, *args, **kwargs):
        if self.restoration_date and self.failure_date:
            self.downtime = (self.restoration_date - self.failure_date).days
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'
