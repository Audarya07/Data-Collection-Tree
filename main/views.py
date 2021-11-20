from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .tree import Tree

tree = Tree()

@csrf_exempt
def default(request):
    return HttpResponse("Welcome to Data Collection Tree API")

@csrf_exempt
def insert(request):
    if request.method == "POST":
        data = eval(request.body.decode('utf-8'))
        tree.insert(data)
        result = {
            "status": 200,
            "data": tree.data
        }
        return JsonResponse(result)
    elif request.method == "GET":
        return HttpResponse("Invalid method GET. Try with POST")

@csrf_exempt
def query(request):
    if request.method == "GET":
        try:
            query = eval(request.body.decode('utf-8'))
            result = tree.get(query)
            return JsonResponse(result)
        except:
            return HttpResponse("Data Not Found !!")
    elif request.method == "POST":
        return HttpResponse("Invalid method POST. Try with GET")
