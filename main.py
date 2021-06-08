from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submitform")
def handle_form(request: Request):
    form_data = request.form()
    return templates.TemplateResponse("table.html", {"request": request, "formData": "test 123"})
# uvicorn.run(app)
