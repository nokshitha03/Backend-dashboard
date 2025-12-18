from fastapi import FastAPI
from app.database import Base, engine

from app.auth.router import router as auth_router
from app.dashboard.router import router as dashboard_router
from app.analytics.router import router as analytics_router
from app.leads.router import router as leads_router
from app.sales.router import router as sales_router
from app.content.router import router as content_router
from app.settings.router import router as settings_router

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend Dashboard API")

# Register routers
app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(analytics_router)
app.include_router(leads_router)
app.include_router(sales_router)
app.include_router(content_router)
app.include_router(settings_router)

@app.get("/")
def root():
    return {"message": "Backend Dashboard API is running"}
