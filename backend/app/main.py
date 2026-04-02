from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --- Safe lazy imports ---
# Import only what’s needed for routes inside startup or inside functions
from app.core.database import Base, engine

app = FastAPI(title="Smart Job Tracker API")

# --- CORS Middleware ---
origins = [
    "http://localhost:5173",  # React app
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Startup Event for DB ---
@app.on_event("startup")
def on_startup():
    try:
        # Force import all models here safely
        import app.models.user
        import app.models.job
        # Create tables
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully")
    except Exception as e:
        print("❌ Failed to initialize database:", e)

# --- Include routers ---
# Import routers here after startup to avoid blocking
from app.api.routes import auth, jobs
app.include_router(auth.router)
app.include_router(jobs.router)

# --- Root endpoint ---
@app.get("/")
def root():
    return {"message": "API running successfully"}