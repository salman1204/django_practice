import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try: 
        data = json.loads(body) # string of Json data --> Python Dictionary 
    except: 
        pass
    print(data.keys())
    print(request.headers)
    print(request.GET) #url query params
    return JsonResponse(data)
