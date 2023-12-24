```python
from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import engine, Base
from models import CV
from utilities import validate_cv_data

app = FastAPI()

Base.metadata.create_all(bind=engine)

cv_router = SQLAlchemyCRUDRouter(
    schema=CV,
    create_schema=CV,
    update_schema=CV,
    db_model=CV,
    db=SessionLocal,
    prefix="/cv",
    tags=["cv"],
)

app.include_router(cv_router)

templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def index():
    return templates.TemplateResponse("index.html", {"request": request})
```