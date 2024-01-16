from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from crm.models import Employees
from api.serializers import EmployeeSerializer
from rest_framework.viewsets import ViewSet
from rest_framework import authentication,permissions
from rest_framework.decorators import action


class EmployeeListCreateView(APIView):

    def get(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        # deserializer
        # reference_name=serializerclass(query_set,many)
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kwargs):
        # serializer
        # reference_name=SerializerClass(data=request.data)
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    
# localhost:8000/api/employees/{id}
# method:get,put,post


class EmpolyeeMixinView(APIView):
    
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(qs,many=False)
        return Response(data=serializer.data)
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        employee_object=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(data=request.data,instance=employee_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors) 
    
    def delete(self,request,*args,**Kwargs):

        return Response(data={"messages":"employee delete"})
    

#                                viewset

class EmployeeViewsetView(ViewSet):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        if "department" in request.query_params:
            value=request.query_params.get("department")
            qs=qs.filter(department=value)
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(qs,many=False)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        employee_object=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(data=request.data,instance=employee_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        return Response(data={"messages":"delete employee"})        

# url: localhost:8000/api/v2/employees/all_departments/
# method:get


    @action(methods={"get"},detail=False)
    def all_departments(self,request,*args,**kwargs):
        qs=Employees.objects.all().values_list("department",flat=True).distinct()
        return Response(data=qs)