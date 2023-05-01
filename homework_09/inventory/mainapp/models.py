from django.db import models


class Device(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32, unique=True)
    pc_name = models.CharField(max_length=32, unique=True)
    serial = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.type


class User(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=32, unique=True)
    e_mail = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.last_name


class Department(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Plant(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Admin(models.Model):
    objects = models.Manager()
    last_name = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=32, unique=True)
    e_mail = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.last_name


def card_number():
    no = Card.objects.count()
    if no is None:
        return f'Карточка №1'
    else:
        return f'Карточка № {no + 1}'


class Card(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=32, default=card_number, null=True)
    device_type = models.ForeignKey(Device, to_field="id", on_delete=models.CASCADE, blank=True, null=True)
    # device_type = models.CharField(max_length=32, unique=True, blank=True, null=True)
    device_name = models.CharField(max_length=32, unique=True, blank=True, null=True)
    pc_name = models.CharField(max_length=32, unique=True, blank=True, null=True)
    device_serial = models.CharField(max_length=32, unique=True, blank=True, null=True)

    user_last_name = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE, blank=True, null=True)
    # user_last_name = models.CharField(max_length=32, unique=True, blank=True, null=True)
    user_first_name = models.CharField(max_length=32, unique=True, blank=True, null=True)
    user_e_mail = models.CharField(max_length=32, unique=True, blank=True, null=True)

    department_name = models.ForeignKey(Department, to_field="id", on_delete=models.CASCADE, blank=True, null=True)
    # department_name = models.CharField(max_length=32, unique=True, blank=True, null=True)

    plant_name = models.ForeignKey(Plant, to_field="id", on_delete=models.CASCADE, blank=True, null=True)
    # plant_name = models.CharField(max_length=32, unique=True, blank=True, null=True)

    status_name = models.ForeignKey(Status, to_field="id", on_delete=models.CASCADE, blank=True, null=True)
    # status_name = models.CharField(max_length=32, unique=True, blank=True, null=True)

    admin_last_name = models.ForeignKey(Admin, to_field="id", on_delete=models.CASCADE, blank=True, null=True)
    # admin_last_name = models.CharField(max_length=32, unique=True, blank=True, null=True)
    admin_first_name = models.CharField(max_length=32, unique=True, blank=True, null=True)
    admin_e_mail = models.CharField(max_length=32, unique=True, blank=True, null=True)

    comment = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def count_device_types(self):
        return self.device.count()




