from django.http import JsonResponse


def Home(request):
    info = {'name': 'Aditya Kumar Singh'}
    return JsonResponse(info)
