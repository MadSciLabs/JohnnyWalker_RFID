from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from jwrfid.models import Drink

class customAuth(Authentication):

  def is_authenticated(self, request, **kwargs):

    api_key = request.GET.get('api_key') or request.POST.get('api_key')

    return True
    #if api_key == "138madsci138":
    #  return True
    #return False

class DrinkResource(ModelResource):
    class Meta:
        queryset = Drink.objects.all()
        resource_name = 'drink'
        filtering = {
          'rfid' : 'exact',
          'type' : 'exact',
        }
        authorization = Authorization() #customAuth()
        allowed_methods = ['get', 'post']
