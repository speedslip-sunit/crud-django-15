from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import employee, department
from .serializers import EmployeeSerializer, DepartmentSerializer
from django.http import Http404, JsonResponse


# echo
@api_view(['GET'])
def echo(request):
    return JsonResponse({"status": "live"})


# Create Department
@api_view(['POST'])
def department_create(request):
    '''
    Create department object
    '''
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def department_interact(request, department_id):
    '''
    Update/delete department object
    '''
    try:
        d = department.objects.get(department_id=department)
    except d.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DepartmentSerializer(d)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepartmentSerializer(d, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def department_list(request):
    dlist = department.objects.all()
    serializer = DepartmentSerializer(dlist, many=True)
    return Response(serializer.data)