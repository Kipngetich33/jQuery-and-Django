# std lib imports
import json

# core django imports
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.views import View

# local imports apps and models
from . models import Dog,Lion
from . forms import  TestForm

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
    #     return HttpResponse(json.dumps(from_db.data), content_type="application/json"
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

def jquery_test(request):

    return render(request,'jquery.html')


# test views for class based views
class MyView(View):
    greeting = "Good Day"

    def get(self, request):
        # <view logic>
        return HttpResponse(self.greeting) 

class MorningGreetingView(MyView):
    greeting = "Morning to ya"


# handling forms in class based views
class MyFormView(View):
    form_class = TestForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

class SuccessView(View):
    # form_class = TestForm
    # initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        # return render(request, self.template_name, {'form': form})
        print("Self")
        print(request.POST)
        return HttpResponse("Successful")

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect("Successful Post")

# serializers
from .models import Lion
from .serializers import LionSerializer
from rest_framework import generics

class LionList(generics.ListCreateAPIView):
    queryset = Lion.objects.all()
    serializer_class = LionSerializer

class LionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lion.objects.all()
    serializer_class = LionSerializer

# this is a test view function for a sticky navbar
def navbar(request):
    return render(request ,'navbar.html')