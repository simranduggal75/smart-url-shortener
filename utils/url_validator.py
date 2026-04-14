
SUSPICIOUS_KEYWORDS = [
    "free-money",
    "hack",
    "phishing",
    "scam",
    "malware",
    "login-free",
    "win-prize"
]

def is_suspicious_url(url: str):
    return any(keyword in url.lower() for keyword in SUSPICIOUS_KEYWORDS)