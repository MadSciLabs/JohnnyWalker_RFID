# Cr your views here.
from django.http import HttpResponse
from django.utils import simplejson
from django.template import RequestContext, loader

from jwrfid.models import Drink

def index(request):

  template = loader.get_template('index.html')
  context = RequestContext(request, {
    'a': 1
  })
  return HttpResponse(template.render(context)) 

def station(request, _type):

  template = loader.get_template('station.html')
  context = RequestContext(request, {
    'type': _type
  })
  return HttpResponse(template.render(context)) 

def swipe(request, _rfid, _type):

  sSuccess = "0"

  if Drink.objects.filter(rfid=_rfid,type=_type).count() > 0:
    sSuccess = "1"

  else:
    d = Drink(rfid=_rfid,type=_type,count=1)
    d.save()

  to_json = [{ "r": sSuccess, "rfid": _rfid }]
  return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
