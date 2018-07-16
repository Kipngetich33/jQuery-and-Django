from django.shortcuts import render
from . models import Dog,Lion
from django.http import HttpResponse,JsonResponse
import json

data  = {
        'point1':{ 'x': 6 ,'y': 'l'},
        'point2':{ 'x': 7 ,'y': 'k'},
    }
# the json data goes here

# *****************************************************************************************************************************************************************

# the view functions goes below
# Create your views here.
def home(request):

    # dog = Dog(name = 'test_json',data = data)
    # dog.save()

    # from_db = Dog.objects.first()
    # if from_db:
    #     return HttpResponse(json.dumps(from_db.data), content_type="application/json")
    
    
    return render(request ,'home.html')

def another(request): 
   return render(request ,'another.html')

def third(request):
    if request.method == 'POST':
        print(request.POST)
        # print('Posting') 
    return render(request ,'third.html') 

def json_response(request):
    my_data = Dog.objects.first()

    return JsonResponse(my_data.data)


