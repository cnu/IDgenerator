import json
import traceback

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from IDgenerator.models import Rider


@csrf_exempt
def submit_idcard(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('UTF-8'))
        validator(data)
        insert_successful = insert_db(data)
        if insert_successful:
            return HttpResponse('Inserted into database successfully')
        else:
            return HttpResponse('Insert failed')


def validator(data):
    pass


def insert_db(data):
    db = Rider(**data)
    try:
        db.save()
        return True
    except:
        print(traceback.format_exc())
        return False


@csrf_exempt
def ping(request):
    if request.method == 'GET':
        return HttpResponse('pong')
