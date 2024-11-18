from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello from Django!"})

# Option 1: If you want to return JSON response
@api_view(['GET'])
def home(request):
    return Response({"message": "Hello from Django!"})


def home(request):
    return render(request, 'home.html')  # You'll need to create home.html template

# Option 2: If you want to render an HTML template
# def home(request):
#     return render(request, 'home.html')  # You'll need to create home.html template