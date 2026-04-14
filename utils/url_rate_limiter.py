from collections import defaultdict
from datetime import datetime, timedelta

request_log = defaultdict(list)

def is_rate_limited(ip):
    now = datetime.utcnow()

    request_log[ip] = [
        time for time in request_log[ip]
        if now - time < timedelta(minutes=1)
    ]

    if len(request_log[ip]) >= 5:
        return True

    request_log[ip].append(now)
    return False