from django.db import models

# Create your models here.
import uuid


def uuid_str():
    return str(uuid.uuid4())


# Create your models here.
class department(models.Model):
    department_id = models.CharField(primary_key=True, default=uuid_str, max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class employee(models.Model):
    employee_id = models.CharField(primary_key=True, default=uuid_str, max_length=100)
    name = models.CharField(max_length=100)
    contract_employee = models.BooleanField(default=True)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name
