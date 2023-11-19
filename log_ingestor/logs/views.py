from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Log
import json
from rest_framework import generics
from .models import Log
from .serializers import LogSerializer
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


@csrf_exempt
def ingest_log(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        log = Log.objects.create(**data)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



class LogList(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer