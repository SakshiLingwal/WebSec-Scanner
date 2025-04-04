# WebSec Scanner

WebSec Scanner is a security scanning tool designed to detect vulnerabilities in websites, including SQL Injection, XSS, weak passwords, DNS records, and more.

## Prerequisites

Ensure you have the following installed:
- [Node.js](https://nodejs.org/) (for frontend)
- [Python 3.x](https://www.python.org/) (for backend)
- [Git](https://git-scm.com/)

## Setup Instructions

### Clone the Repository
```sh
git clone https://github.com/SakshiLingwal/WebSec-Scanner.git
cd WebSec-Scanner
```

### Running the Project
Since the project consists of both frontend and backend, open two terminal windows/split terminal.

#### 1. Run the Frontend
```sh
cd Frontend_contri
npm install  # Install dependencies
npm start    # Start the frontend
```
This will start the frontend on `http://localhost:3000/`.

#### 2. Run the Backend
```sh
cd Backend_contri
pip install -r requirements.txt  # Install backend dependencies
python api.py   # Start the backend server
```
This will start the backend on `http://localhost:10037/`.

### Additional Instructions
- Refer to `Frontend_contri/README.md` for detailed frontend setup.
- Refer to `Backend_contri/README.md` for backend setup and API usage.

Now, you can use WebSec Scanner to analyze website security effectively!

---


