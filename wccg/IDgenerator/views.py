import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def submit_idcard(request):
    if request.method == 'POST':
        print('inside ID card')
        data = json.loads(request.body.decode('UTF-8'))
        print data
        return HttpResponse('ok')


@csrf_exempt
def ping(request):
    print('inside ID card')
    if request.method == 'GET':
        return HttpResponse('pong')
