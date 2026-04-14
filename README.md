# Smart URL Shortener API

A production-inspired backend application built using **FastAPI** that provides intelligent URL shortening with analytics, security checks, rate limiting, and expiration support.

This project goes beyond a simple CRUD URL shortener by implementing **real-world backend engineering concepts** such as request throttling, click analytics, suspicious URL filtering, and metadata tracking.



# Features

## Core URL Management
- Generate shortened URLs from long URLs
- Redirect shortened URLs to original destination
- Support custom aliases for user-defined short links
- Set expiration time for temporary URLs

## Analytics & Tracking
- Track total click count per URL
- Store click history with timestamps
- Capture metadata including:
  - IP Address
  - User-Agent / Browser info
- Trending URLs endpoint based on click frequency

## Security & Validation
- Suspicious / unsafe URL detection before shortening
- IP-based rate limiting to prevent abuse/spam
- Proper HTTP error handling and validation



# Tech Stack

- **Backend Framework:** FastAPI
- **Language:** Python
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Server:** Uvicorn



# Why This Project?

Built to deepen understanding of backend system design by implementing
production-like backend concerns beyond CRUD operations such as analytics,
security filtering, rate limiting, and request validation.



# Project Structure


smart-url-shortener/


├── models/

  ├── url_model.py

  └── click_model.py


├── routes/

   └── url_routes.py

├── schemas/

   └── url_schema.py

│__ Screenshots


├── services/

   └── url_service.py

├── utils/

   ├── generator.py

  ├── rate_limiter.py

  └── url_validator.py

├── main.py

├── database.py

├── requirements.txt

└── README.md




# API Endpoints

## Create Short URL

**POST** `/url/shorten`

Request:

```json
{
  "original_url": "https://google.com",
  "custom_alias": "google123",
  "expires_in_minutes": 60
}
```



## Redirect to Original URL

**GET** `/url/{short_code}`

Redirects user to the original URL.



## URL Analytics

**GET** `/url/analytics/{short_code}`

Returns:
- Total clicks
- Click metadata
- Click timestamps



## Trending URLs

**GET** `/url/trending`

Returns top clicked URLs ranked by popularity.



# Security Features

## Suspicious URL Detection

Rejects malicious-looking URLs containing suspicious keywords such as:
- phishing
- scam
- malware
- hack
- free-money



## Rate Limiting

Restricts excessive requests from the same IP to prevent abuse.

Current limit:
- **5 requests per minute per IP**



# Error Handling

Implemented meaningful HTTP responses:

- **400** → Bad Request / Validation Errors
- **404** → URL Not Found
- **410** → URL Expired
- **429** → Rate Limit Exceeded



# How to Run Locally

## Clone Repository

```bash
git clone https://github.com/simranduggal75/smart-url-shortener.git
cd smart-url-shortener
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Server

```bash
uvicorn main:app --reload
```

## Open Swagger Docs

```bash
http://127.0.0.1:8000/docs
```



# Future Enhancements

Potential future improvements:

- Redis-based distributed rate limiting
- JWT authentication / user accounts
- QR code generation for shortened URLs
- Machine Learning based malicious URL detection
- PostgreSQL migration for production readiness
- Docker containerization



# Key Learning Outcomes

This project demonstrates:

- REST API Design
- Backend Architecture / Layered Design
- Database Modeling
- Aggregation Queries
- Request Validation
- Security & Abuse Prevention
- Real-world Error Handling
- Production-inspired Backend Practices



## Author

**Simran Duggal**

## ⭐ If you found this useful

Give this repo a ⭐ on GitHub!

## 📸 Output Screenshot
  Please refer to screenshots folder for output screenshots
