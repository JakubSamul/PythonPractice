from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engin

models.Base.metadata.create_all(bind=engin)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()