# Full-Stack Docker - Python FastAPI - Vite - React

A modern, high-performance web application skeleton utilizing FastAPI for a robust backend and React powered by Vite for a lightning-fast frontend. The entire ecosystem is fully containerized with Docker for seamless development and deployment.

## 🚀 Tech Stack

*   **Backend:**  FastAPI
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
*   **Backend API:** At app folder, `uvicorn main:app --host 0.0.0.0 --port 8080`. Access `http://localhost:8080/hello`.
*   **Frontend (Vite + React):** At frontend folder, `npm run dev`. Access `http://localhost:5173`.


### 3. To run with docker

*   Ensure you have [Docker Desktop](https://docker.com) installed and docker engine running.
*   At root folder, `docker build -f app/Dockerfile -t my-app:1.0 .`
*   At root folder, `docker run -d -p 8080:80 --name my-running-app my-app:1.0`. Access `http://localhost:8080/hello`.
*   At root folder, `docker build -f frontend/Dockerfile -t my-react-app:1.0 ./frontend`
*   At root folder, `docker run -d -p 5173:5173 --name running-frontend my-react-app:1.0`. Access `http://localhost:5173`.

---


### 4. To run with docker compose

*   Ensure you have [Docker Desktop](https://docker.com) installed and docker engine running.
*   At root folder, `docker compose up --build -d`. Access `http://localhost:8080/hello` and `http://localhost:5173`.


## 📂 DOCKER CONTAINER FILESYSTEM

```text
===================================================================================================
                                  🐳 COMPLETE DESKTOP RUNTIME ARCHITECTURE
===================================================================================================

       +---------------------------------------------------------------------------------+

       | 🖥️ YOUR MAC HOST MACHINE (macOS)                                                |
       |                                                                                 |
       |  📁 Project Folder: /python_fastapi/                                            |
       |  🌐 Web Browser   : Opens http://localhost:5173  (Loads Frontend App UI)        |
       |                     Triggers fetch('http://localhost:8080/hello')               |
       +---------------------------------------------------------------------------------+
                                               │
                                               │ [Port Mappings & Volume Synchronizations]
                                               ▼
===================================================================================================
                                    🐳 DOCKER DESKTOP VIRTUAL MACHINE
===================================================================================================
│                                                                                                  │
│  ┌──────────────────────────────────────────┐    ┌──────────────────────────────────────────┐    │
│  │ 📦 CONTAINER: react-frontend             │    │ 📦 CONTAINER: fastapi-backend           │    │
│  ├──────────────────────────────────────────┤    ├──────────────────────────────────────────┤    │
│  │ • OS: Linux (Node 20-alpine)             │    │ • OS: Linux (Python 3.14)                │    │
│  │ • Network Port: 5173                     │    │ • Network Port: 80                       │    │
│  │ • Bound to Mac: http://localhost:5173    │    │ • Bound to Mac: http://localhost:8080    │    │
│  ├──────────────────────────────────────────┤    ├──────────────────────────────────────────┤    │
│  │                                          │    │                                          │    │
│  │  / (Container Root)                      │    │  / (Container Root)                      │    │
│  │  └── 📂 app/              [WORKDIR]      │    │  └── 📂 code/             [WORKDIR]      │    │
│  │      ├── 📂 node_modules/ ──────────┐    │    │      ├── 📄 requirements.txt             │    │
│  │      │   └── [Compiled Packages]    │    │    │      │                                    │    │
│  │      │   (Isolated in Docker Vol) ◄─┘    │    │      └── 📂 app/      ◄────────────────┐  │
│  │      │                                   │    │          ├── 📄 main.py                │  │
│  │      ├── 📄 package.json                 │    │          └── 📄 [Other code files...]  │  │
│  │      ├── 📄 vite.config.js               │    │                                        │  │
│  │      │                                   │    │                                        │  │
│  │      └── 📂 src/          ◄──────────┐   │    │                                        │  │
│  │          ├── ⚛️ App.tsx              │   │    │                                        │  │
│  │          └── ⚛️ main.tsx             │   │    │                                        │  │
│  │                                      │   │    │                                        │  │
│  └──────────────────────────────────────┼───┘    └────────────────────────────────────────┼──┘  │
│                                         │                                                 │     │
==========================================│=================================================│=====│
                                          │ [Real-Time Bi-Directional Hot-Reload Mappings]  │
                                          ▼                                                 ▼
                  +───────────────────────────────+                 +─────────────────────────+

                  | 📁 LOCAL MAC FOLDER:          |                 | 📁 LOCAL MAC FOLDER:   |
                  |    ./frontend/src/            |                 |    ./app/               |
                  +───────────────────────────────+                 +─────────────────────────+


```

---
