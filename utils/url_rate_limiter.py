from collections import defaultdict
from datetime import datetime, timedelta

RATE_LIMIT = 5
RATE_WINDOW_MINUTES = 1

request_log = defaultdict(list)


def is_rate_limited(ip):
    now = datetime.utcnow()

    request_log[ip] = [
        time for time in request_log[ip]
        if now - time < timedelta(minutes=RATE_WINDOW_MINUTES)
    ]

    if len(request_log[ip]) >= RATE_LIMIT:
        return True

    request_log[ip].append(now)

    return False