import json
import traceback
from .create_id import main
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from IDgenerator.models import Rider
import IDgenerator.models
from random import randint
from datetime import date, datetime


@csrf_exempt
def submit_idcard(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('UTF-8'))
        # validator(data)
        new_rider_id = generate_rider_id()
        print(new_rider_id)
        data.update({'rider_id': new_rider_id})
        insert_successful = insert_db(data)
        #   id_created = main(data)
        if insert_successful:
            return HttpResponse('Inserted into database successfully')
        else:
            return HttpResponse('Insert failed')


def validator(data):
    pass


def generate_rider_id():
    prefix = str(date.today().year)[2:]
    try:
        latest_id = Rider.objects.values('rider_id').latest('created_date')['rider_id']
    except:
        rider_id = prefix + 'CC' + '00001'
        return rider_id
    to_incr = latest_id.split('CC')[-1]
    digits = len(str(int(to_incr))) - 1
    if int(to_incr) % 10 == 0:
        zeros_count = str(to_incr).count('0') + digits -1
    else:
        zeros_count = str(to_incr).count('0') + digits
    next_id = str(int(to_incr) + 1).zfill(zeros_count+1)
    rider_id = prefix + 'CC' + next_id
    return rider_id


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
