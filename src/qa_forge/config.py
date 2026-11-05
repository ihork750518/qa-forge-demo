"""Environment-aware configuration. No production endpoints are contacted by default."""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

ENVIRONMENTS = {
    "dev": "https://dev.example.invalid",
    "stage": "https://stage.example.invalid",
    "prod": "https://example.com",
}

@dataclass(frozen=True)
class Settings:
    environment: str
    base_url: str
    api_token: str | None = None
    api_key: str | None = None


def get_settings(environment: str | None = None) -> Settings:
    env = (environment or os.getenv("QA_ENV", "dev")).lower()
    if env not in ENVIRONMENTS:
        raise ValueError(f"Unknown environment {env!r}. Choose: {', '.join(ENVIRONMENTS)}")
    # An explicit override is useful for local mocks and customer environments.
    url = os.getenv(f"QA_{env.upper()}_BASE_URL") or os.getenv("BASE_URL") or ENVIRONMENTS[env]
    return Settings(env, url.rstrip("/"), os.getenv("QA_API_TOKEN"), os.getenv("QA_API_KEY"))
