import logging
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

logger = logging.getLogger(__name__)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type((requests.exceptions.RequestException,)),
    reraise=True,
)
def fetch_with_retry(url: str, timeout: int = 10, **kwargs) -> requests.Response:
    """
    Выполняет HTTP GET запрос с экспоненциальной задержкой при ошибках.
    """
    logger.info("Fetching URL: %s", url)
    resp = requests.get(url, timeout=timeout, **kwargs)
    resp.raise_for_status()
    return resp