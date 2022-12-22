
from django.urls import path
from hello_site_app.views import HelloWorldView, HelloView

urlpatterns = [
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('<name>', HelloView.as_view(), name='hello_name'),
]