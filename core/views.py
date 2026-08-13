from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "core/home.html"


@require_GET
def health(_request: HttpRequest) -> JsonResponse:
    """Return a cheap liveness response for containers and hosting platforms."""
    return JsonResponse({"service": "tanu", "status": "ok"})


def not_found(request: HttpRequest, exception: Exception) -> HttpResponse:
    """Render the public 404 page without exposing request details."""
    del exception
    return render(request, "404.html", status=404)


def server_error(request: HttpRequest) -> HttpResponse:
    """Render the public 500 page."""
    return render(request, "500.html", status=500)
