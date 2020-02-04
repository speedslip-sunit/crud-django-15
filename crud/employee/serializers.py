from rest_framework import serializers
from employee.models import employee, department


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = employee
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = department
        fields = '__all__'
