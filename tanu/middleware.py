from collections.abc import Callable

from django.http import HttpRequest, HttpResponse


class SecurityHeadersMiddleware:
    """Add a conservative browser policy to every response."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)
        response.headers.setdefault(
            "Content-Security-Policy",
            "; ".join(
                (
                    "default-src 'self'",
                    "base-uri 'self'",
                    "object-src 'none'",
                    "frame-ancestors 'none'",
                    "form-action 'self'",
                    "img-src 'self' data:",
                    "font-src 'self'",
                    "style-src 'self'",
                    "script-src 'self'",
                    "connect-src 'self'",
                )
            ),
        )
        response.headers.setdefault(
            "Permissions-Policy",
            "camera=(), geolocation=(), microphone=(), payment=(), usb=()",
        )
        return response
