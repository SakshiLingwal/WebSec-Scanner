# WebSec Scanner - Backend

## Introduction
WebSec Scanner is a security scanning tool designed to analyze websites for vulnerabilities such as SQL injection, XSS attacks, weak passwords, DNS misconfigurations, and more.

This document provides instructions on how to set up and run the backend of the WebSec Scanner.

## Prerequisites
Ensure you have the following installed on your system:
- **Python 3.8+**
- **pip** (Python package manager)
- **Git**
- **Flask**
- **Required dependencies** (listed in `requirements.txt`)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/SakshiLingwal/WebSec-Scanner.git
cd WebSec-Scanner/backend
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Backend Server
```bash
python app.py
```

By default, the server runs on **http://127.0.0.1:10037**.

## API Endpoints

| Endpoint          | Method | Description                         |
|------------------|--------|-------------------------------------|
| `/health`        | GET    | Health check of the backend server |
| `/sqlscan`       | POST   | SQL Injection vulnerability scan   |
| `/xss`           | POST   | Cross-Site Scripting (XSS) scan    |
| `/password`      | POST   | Weak password detection            |
| `/webstresser`   | POST   | Website stress test (DDoS test)    |
| `/deface`        | POST   | Detect website defacement          |
| `/dnsrecord`     | POST   | Fetch DNS records                  |
| `/basicscan`     | POST   | Gather general website info        |
| `/scanner/fullscan` | POST | Perform a full security scan      |



## Troubleshooting
- If you encounter **port conflicts**, change the port in `app.py`:
  ```python
  app.run(host='0.0.0.0', port=5000, debug=True)
  ```
- If Flask is not recognized, ensure you activated the virtual environment (`venv`).
- For permission errors, try running commands as an administrator (`sudo` on Linux/macOS).

## Contribution
Feel free to fork the repo, create pull requests, and report issues!

## License
This project is open-source and licensed under the MIT License.

---

