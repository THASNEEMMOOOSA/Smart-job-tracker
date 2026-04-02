# <img src="https://raw.githubusercontent.com/THASNEEMMOOOSA/Vertus-job-tracker/main/frontend/src/assets/vertusf.png" alt="Vertus Logo" width="50" style="vertical-align:middle;"> Vertus - Job Tracker & Analytics Platform

[![GitHub Repo Size](https://img.shields.io/github/repo-size/THASNEEMMOOOSA/Vertus-job-tracker?style=for-the-badge)](https://github.com/THASNEEMMOOOSA/Vertus-job-tracker)
[![GitHub Issues](https://img.shields.io/github/issues/THASNEEMMOOOSA/Vertus-job-tracker?style=for-the-badge)](https://github.com/THASNEEMMOOOSA/Vertus-job-tracker/issues)
[![GitHub License](https://img.shields.io/github/license/THASNEEMMOOOSA/Vertus-job-tracker?style=for-the-badge)](https://github.com/THASNEEMMOOOSA/Vertus-job-tracker/blob/main/LICENSE)
[![React](https://img.shields.io/badge/React-blue?style=for-the-badge&logo=react)](https://reactjs.org/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-green?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

---

## Overview

Vertus is a full-stack SaaS platform that allows users to:

- Track job applications across different stages  
- Manage interview pipelines  
- Monitor application trends and status distribution  
- Access analytics dashboards  
- Perform full CRUD operations  
- Authenticate securely using JWT  
- Deploy and access via AWS EC2  

This project demonstrates **full-stack engineering**, **scalable backend APIs**, **responsive frontend architecture**, and **cloud deployment workflows**.

---

## Technology Stack

**Frontend:** React, TypeScript, Tailwind CSS, Axios, Recharts, React Router DOM  
**Backend:** FastAPI, Python, SQLAlchemy, Pydantic, JWT Authentication, PostgreSQL  
**Cloud & DevOps:** AWS EC2, Nginx, systemd, Linux/Ubuntu, REST APIs

---

## Key Features

### Authentication & Security
- JWT-based login and registration  
- Protected API routes  
- Secure password hashing and token-based session management  

### Job Management
- Add, edit, delete job applications  
- Search and filter by company or status  
- Status pipeline: Applied → Interview → Offer → Rejected  

### Analytics Dashboard
- Total application count  
- Status distribution charts  
- Weekly trends and KPI visualization  

### Cloud Deployment
- Frontend served via AWS EC2 + Nginx  
- Backend deployed with FastAPI + Uvicorn + systemd  
- PostgreSQL database integration  
- Production-style Linux service deployment  

---

## Application Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/THASNEEMMOOOSA/Vertus-job-tracker/main/screenshots/front1.png" alt="Dashboard Screenshot 1" width="300" style="margin-right:10px;" />
  <img src="https://raw.githubusercontent.com/THASNEEMMOOOSA/Vertus-job-tracker/main/screenshots/front2.png" alt="Dashboard Screenshot 2" width="300" style="margin-right:10px;" />
  <img src="https://raw.githubusercontent.com/THASNEEMMOOOSA/Vertus-job-tracker/main/screenshots/front3.png" alt="Dashboard Screenshot 3" width="300" />
</p>

---

## Project Structure

```text
vertus-job-tracker/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── services/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── core/
└── README.md
API Endpoints

Authentication

POST /auth/register
POST /auth/login

Jobs

GET    /jobs
POST   /jobs
PUT    /jobs/{id}
DELETE /jobs/{id}

Analytics

GET /jobs/analytics/summary
Local Setup
Clone Repository
git clone https://github.com/THASNEEMMOOOSA/Vertus-job-tracker.git
cd Vertus-job-tracker
Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
Frontend
cd frontend
npm install
npm run dev
AWS Deployment
EC2 Ubuntu Free Tier provisioning
Nginx reverse proxy configuration
FastAPI backend deployed as systemd service
PostgreSQL integration
Frontend static asset hosting
Why This Project
Demonstrates full-stack development and architecture
Scalable REST API design
Frontend state management and data visualization
Production-style cloud deployment
End-to-end software engineering practices
Author

Your Name
Full Stack Developer | React | FastAPI | Python | AWS | PostgreSQL

LinkedIn
 | Portfolio