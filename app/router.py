"""
Centralized router configuration.
All application routers are registered here and imported into main.py.
"""

from fastapi import FastAPI

from app.auth.adapter.input.web.google_oauth_router import google_oauth_router
from app.data.adapter.input.web.data_router import data_router
from app.data.infrastructure.orm.data_orm import DataORM  # noqa: F401


def setup_routers(app: FastAPI) -> None:
    app.include_router(google_oauth_router, prefix="/auth")
    app.include_router(data_router, prefix="/data")
