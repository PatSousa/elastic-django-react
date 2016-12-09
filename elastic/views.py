from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
import requests
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello world")


class searchData(View):

    def post(self, request):
        import ipdb ; ipdb.set_trace()
    
    def get(self, request):
        data = {
            "query": {
                "query_string": { "query": request.GET.get('query') }
                }
            }
        response = requests.post('http://127.0.0.1:9200/my_index/_search', data=json.dumps(data))
        return JsonResponse(response.json())


class IndexPageView(TemplateView):
    
    def get_context_data(self, request=None, **kwargs):
        context = {}
        return context

    def get(self, request):
        context = self.get_context_data(request)

        return TemplateResponse(request, template="elastic/index.html", context=context)
