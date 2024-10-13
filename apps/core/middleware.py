from django.http import HttpResponsePermanentRedirect
from django.conf import settings
from django.http import HttpResponse
from django_minify_html.middleware import MinifyHtmlMiddleware


class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/kamal/up/":
            # Or perform any "real" health checking, if needed
            response = HttpResponse("OK")
        else:
            response = self.get_response(request)

        return response
