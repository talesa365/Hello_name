from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here
class HelloWorldView(View):
    def get(self, request):
        return render(request, template_name = 'Hello_world.html')
    
class HelloView(View):
    def get(self, request, name):
        return render(
            request,
            template_name = 'Hello_name.html', 
            context = {'person':name},  
        )  
