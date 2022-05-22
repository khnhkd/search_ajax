from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import show_info, search_ajax

urlpatterns = [
    path('', show_info),
    path('search', csrf_exempt(search_ajax))
]
