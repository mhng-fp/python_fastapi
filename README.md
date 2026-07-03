# Full-Stack Docker - Python FastAPI - Vite - React

A modern, high-performance web application skeleton utilizing FastAPI for a robust backend and React powered by Vite for a lightning-fast frontend. The entire ecosystem is fully containerized with Docker for seamless development and deployment.

## 🚀 Tech Stack

*   **Backend:** PythonFastAPI 
*   **Frontend:** React, Vite
*   **Containerization:** Docker, Docker Compose

---

## 🏃 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/mhng-fp/python_fastapi.git
```

### 2. To run without docker

The frontend and backend application components will be accessible at:
*   **Frontend (Vite + React):** `npm run dev` at frontend folder. Access `http://localhost:5173`.
*   **Backend API:** `uvicorn main:app --host 0.0.0.0 --port 8080` at app folder. Access `http://localhost:8080/hello`.

### 2. To kill processes

*   lsof -i :5173
*   kill -9 xx

---

### 3. To run with docker

*   Ensure you have [Docker Desktop](https://docker.com) installed and docker engine running.
*   `docker build . -t my-app:1.0` at root folder. `docker images -a` to query.
*   `docker run -d -p 8080:80 --name my-running-container my-app:1.0` at root folder. `docker ps -a` `docker logs -f my-running-container`  to query. Access `http://localhost:8080/hello`.

### 4. To kill docker containers
*   `docker stop fastapi-app my-running-container`
*   `docker rm my-running-container`
*   `docker rmi my-app:1.0`
*   `docker system prune -a --volumes`  

---

Once the build completes, the application components will be accessible at:
*   **Frontend (Vite + React):** `http://localhost:5173`

---

## 📂 Project Structure

```text
├── backend/
│   ├── app/                # Main application package
│   │   ├── api/            # API endpoints/routes
│   │   ├── core/           # Configuration, security, settings
│   │   └── main.py         # FastAPI app initialization
│   ├── Dockerfile          # Backend production build definition
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── src/                # React source code
│   │   ├── components/     # Reusable UI components
│   │   └── App.jsx         # Main application entry component
│   ├── Dockerfile          # Frontend containerization file
│   ├── package.json        # Node.js dependencies
│   └── vite.config.js      # Vite configuration
├── docker-compose.yml      # Multi-container orchestration config
└── README.md
```

---
