from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.models import Students
from api.serialzers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            std = Students.objects.get(id = id)
            serializer = StudentSerializer(std)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content_type = 'application/json')
        std = Students.objects.all()
        serializer = StudentSerializer(std,many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data , content_type = 'application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        print(id,'llllllllllll')
        std = Students.objects.get(id=id)
        serializer = StudentSerializer(std ,data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Update'}  
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')  
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')   


    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        std = Students.objects.get(id=id)
        std.delete()
        res = {'msg': 'Data Delete'}  
        return JsonResponse(res,safe=False)
