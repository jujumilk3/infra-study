from django.views import View
from django.http import JsonResponse


class CheckIpView(View):
    def get(self, request, *args, **kwargs):
        print(request.__dict__)
        return JsonResponse({
            'hello': 'world'
        })
