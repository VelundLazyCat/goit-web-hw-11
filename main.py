import my_routes
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from my_db import get_db
from models import Contact
from sqlalchemy import select

app = FastAPI()


app.include_router(my_routes.router, prefix='/api')


@app.get('/')
def index():
    return {'message': 'Welcom to Web Assistant'}


@app.get("/api/healthchecker")
async def healthchecker(db: Session = Depends(get_db)):
    try:
        # Make request
        result = db.execute(select(Contact)).all()

        if result is None:
            raise HTTPException(
                status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail="Error connecting to the database")
