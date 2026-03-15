from urllib.parse import urlparse


class URLValidator:
    @staticmethod
    def validate(url: str) -> str:
        url = url.strip()
        parse_result = urlparse(url)
        
        if parse_result.scheme not in ("http", "https"):
            raise ValueError("Ссылка должна начинаться с http:// или https://")
        
        if not parse_result.netloc:
            raise ValueError("У ссылки должен быть домен")
        
        return url
