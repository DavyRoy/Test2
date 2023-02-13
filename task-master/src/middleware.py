from django.conf import settings
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response


class ProcessExceptionMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        return self._get_response(request)

    def process_exception(self, request: Request, exception: Exception) -> Response:
        if settings.DEBUG:
            return JsonResponse(data={
                str(exception.__class__.__name__): str(exception),

            }, status=500)

        return None
