# Task API

### Description 
REST API built using FastAPI and PostgreSQL, using Docker to containerise the application, then deployed on AWS EC2.
Traefik acting as a reverse proxy, routing traffic to the API.

### Architecture
```
Online Traffic -> Traefik (Port 80) -> FastAPI (Port 8000) -> PostgreSQL (Port 5432)

                                                           -> Prometheus (Scrape /metrics) 
                                                           -> Grafana (Visualises scraped data)
```
- **Traefik**: Reverse Proxy, routes traffic to the API, keeping the database and API server private.
- **FastAPI**: Handles HTTP requests and business logic, for asynchrous support, automated API documentation, and speed.
- **PostgreSQL**: Data Persistence.
- **Docker**: For containerising the database and application.

### Tech Stack
- **FastAPI**: Acts as the pipeline between the traffic requests and the database.
- **PostgreSQL**: The persistent database for storing data from requests.
- **SQLAlchemy**: An Object-Relational-Mapper (ORM), used for managing database requests, and mapping Python objects to database tables.
- **Docker**: Containerises the application and databases, removing dependency issues, improving reproducibility.
- **Traefik**: Acts as a middleman between public traffic and the API keeping the database and API server private.
- **AWS EC2**: Virtual machine used for online app deployment.
- **GitHub Actions**: Workflow CI/CD pipeline automation tool, ensuring all pushed code is functional before deployment.
- **Prometheus**: Pulls metrics data from app, visualised in Grafana
- **Grafana**: Visualises metric data from Prometheus in user-friendly UI
- **Socket Proxy**: Tecnativa socket proxy, for securing access to docker socket


### Startup
1. Clone the repo
```bash
    git clone https://github.com/IvanKennethBibat/task-api
    cd task-api
```

2. Create the venv
```bash
    python3 -m venv venv
    source venv/bin/activate
```
3. Install required dependencies
```bash
    pip install -r requirements.txt
```

4. Create `.env` in root
```bash
    DATABASE_URL=postgresql://taskuser:taskpassword@db:5432/taskdb
```

5. Start the application
```bash
docker compose up -d
```

### API Endpoints
- **API**: http://localhost/docs
- **Grafana**: http://localhost/grafana
- **Prometheus**: http://localhost/prometheus
- **Traefik**: http://localhost:8080

### CI/CD Pipeline
GitHub Actions tests each API Endpoint after each code commit, ensuring each feature works as expected prior to deployment on the EC2 virtual machine.

### TODO
- ~~JWT Authentication~~ 
- ~~Prometheus, Grafana implementation~~
- ~~Traefik with tecnativa docker socket proxy~~
- Terraform
- Frontend