from fastapi import FastAPI

from .routers import attempts, cases, stats

app = FastAPI(title="Daily Frame API")
app.include_router(cases.router, prefix="/api")
app.include_router(attempts.router, prefix="/api")
app.include_router(stats.router, prefix="/api")
