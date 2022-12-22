
from django.urls import path
from hello_site_app.views import HelloWorldView, HelloView

urlpatterns = [
   path('', hello, view = HelloWorldView.as_view()),
   path('<str:name>', view = HelloView.as_view())
]