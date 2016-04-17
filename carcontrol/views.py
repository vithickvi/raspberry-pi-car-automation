from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import render
import json

@ensure_csrf_cookie
def processit(request):

    if request.is_ajax():
        gvalue = request.POST["gear"]
        try:
			print gvalue

        except Exception as e:
            print e
   
    return HttpResponse(json.dumps({"result" : gvalue }), content_type="application/json")