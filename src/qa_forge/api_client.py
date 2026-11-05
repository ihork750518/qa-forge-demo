"""Reusable synchronous API client. Tokens are never logged."""
from collections.abc import Callable
import httpx


class APIClient:
    def __init__(self, base_url: str, *, token: str | None = None,
                 api_key: str | None = None, transport: httpx.BaseTransport | None = None,
                 timeout: float = 10.0):
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        if api_key:
            headers["X-API-Key"] = api_key
        self._client = httpx.Client(base_url=base_url, headers=headers,
                                    transport=transport, timeout=timeout)

    def request(self, method: str, path: str, **kwargs) -> httpx.Response:
        return self._client.request(method, path, **kwargs)

    def get(self, path: str, **kwargs) -> httpx.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> httpx.Response:
        return self.request("POST", path, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
