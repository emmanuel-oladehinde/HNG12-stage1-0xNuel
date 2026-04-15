# HNG12-stage1-0xNuel
# HNG DevOps Stage 1

## Project Overview
This is a high-performance REST API built with **Python and FastAPI**. It is deployed on an **AWS EC2** instance using **Nginx** as a reverse proxy and **Systemd** to ensure the service stays alive 24/7.

## Live API Base URL
https://0xnuel-hng.duckdns.org

## Tech Stack
* **Language:** Python 3.12+
* **Framework:** FastAPI
* **Server:** AWS EC2 (Ubuntu)
* **Reverse Proxy:** Nginx (Port 443 with SSL)
* **Process Management:** Systemd

##  API Endpoints
| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | GET | Basic status message |
| `/health` | GET | API health check |
| `/me` | GET | Developer information (JSON) |

##   Architecture
[Image of Nginx reverse proxy architecture]
Client (HTTPS) → Nginx (Port 443) → FastAPI App (Port 8000) → JSON Response

##  Running Locally
1. **Clone the repository:**
   `git clone https://github.com/emmanuel-oladehinde/hng-stage1-api.git`
2. **Install dependencies:**
   `pip install -r requirements.txt`
3. **Start the server:**
   `uvicorn main:app --reload`
