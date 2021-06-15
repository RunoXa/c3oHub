from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submitForm")
def handle_form(request: Request, searchJob: str = Form(...)):
    file = open('./data/data.json', )
    data = json.load(file)

    # conditions for different searchJobs
    print(searchJob)
    return templates.TemplateResponse("table.html", {"request": request, "formData": data})

# uvicorn.run(app)
