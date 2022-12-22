from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here
class HelloWorldView(View):
    def get(self, request):
        return render(
            request, 
            template_name = 'Hello_world.html')
            
class HelloView(View):
    def get(self, request, name='world'):
        context={'name': name}
        return render(
            request=request, template_name='hello_name.html', context=context
            )
