# DevOps

🗺️ Application Architecture Map

[Frontend (gradio)] 
        |
        | HTTP Requests (REST API)
        ↓
[Backend Application (FastAPI)]
        |
        | MongoDB Driver (pymongo)
        ↓
[MongoDB Database (Docker image)]
        ↑
        |
[Mongo Express (Docker image - Admin Interface)]

🔗 Component Connections Summary:
Frontend ➝ Backend

Frontend makes HTTP calls to your backend to send or retrieve data.

Backend ➝ MongoDB

The backend uses a MongoDB client library to perform database operations.

Mongo Express ➝ MongoDB

Mongo Express provides a web-based admin panel connected directly to the MongoDB database.

## Docker

created saperate docker files for backend and frontend application 

written docker compose file to manage and run both frontend and backend

## Kubernetes

create secret configuration file for maintaining secrets

created configuration files to manage applications

created deployment and service file for frontend, backend, mongodb and mongo-express
