# Full-Stack FastAPI, Vite & React Boilerplate

A modern, high-performance web application skeleton utilizing FastAPI for a robust backend and React powered by Vite for a lightning-fast frontend. The entire ecosystem is fully containerized with Docker for seamless development and deployment.

## 🚀 Tech Stack

*   **Backend:** FastAPI (Python 3.11+, Pydantic v2)
*   **Frontend:** React (TypeScript/JavaScript), Vite
*   **Containerization:** Docker, Docker Compose

---

## 🛠️ Prerequisites

Ensure you have the following installed on your local machine:
*   [Docker Desktop](https://docker.com)

---

## 🏃 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com
cd your-repo-name
```

### 3. Spin Up Containers
Launch the application using Docker Compose. This will build the images and start the services.

```bash
docker compose up --build
```

Once the build completes, the application components will be accessible at:
*   **Frontend (Vite + React):** `http://localhost:5173` at frontend folder
*   **Backend API:** `http://localhost:8000/hello` at app folder
*   **Interactive API Docs (Swagger UI):** `http://localhost:8000/docs`

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

## 🔧 Production Deployment

To prepare this application for production:
1. Update production variables inside your `.env` files (e.g., disable `RELOAD` modes, change secret keys).
2. Configure a reverse proxy like Nginx or Traefik to route traffic and handle SSL certificates.
3. Build using production compose profiles if applicable.
