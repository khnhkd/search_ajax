import json
from django.shortcuts import render
from django.http import JsonResponse

from .models import Person


# Create your views here.
def show_info(request):
    return render(request, 'information/info.html', {
        'headers': Person._meta.fields,
        'persons': Person.objects.all().values_list()
    })


def search_ajax(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        data = list(Person.objects.filter(first_name__contains=search_str).values())
        return JsonResponse(data, safe=False)
