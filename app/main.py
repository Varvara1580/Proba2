from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse(request = request, name = 'index.html')