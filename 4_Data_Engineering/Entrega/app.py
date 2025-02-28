from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

# El nombre debe ser 'application' para Elastic Beanstalk
application = FastAPI()
templates = Jinja2Templates(directory="templates")

@application.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@application.post("/", response_class=HTMLResponse)
async def process_form(
    request: Request,
    texto: str
):
    respuesta = f"Recibiste: {texto}"
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "respuesta": respuesta
        }
    )

uvicorn.run(application)