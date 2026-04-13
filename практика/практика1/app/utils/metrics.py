from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter("slotkeeper_http_requests_total", "Total HTTP requests", ["method", "path", "status"])
REQUEST_LATENCY = Histogram("slotkeeper_http_request_latency_seconds", "HTTP latency", ["method", "path"])
