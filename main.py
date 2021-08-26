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
    data = ''

    # conditions for different searchJobs
    if searchJob.lower().replace(' ', '') == 'sort':
        file = open('data/sort_job_data.json')
        data = json.load(file)
    elif searchJob.lower().replace(' ', '') == 'grep':
        file = open('data/grep_job_data.json')
        data = json.load(file)
    elif searchJob.lower().replace(' ', '') == 'kmeans':
        file = open('data/kmeans_job_data.json')
        data = json.load(file)
    elif searchJob.lower().replace(' ', '') == 'pagerank':
        file = open('data/pagerank_job_data.json')
        data = json.load(file)
    elif searchJob.lower().replace(' ', '') == 'sgdlr':
        file = open('data/sgd_job_data.json')
        data = json.load(file)
    else:
        data = 'Der gesuchte Job konnte nicht gefunden werden !'
        return templates.TemplateResponse("error.html", {"request": request, "formData": data, "searchJob": searchJob})

    print(searchJob)
    return templates.TemplateResponse("table.html", {"request": request, "formData": data, "searchJob": searchJob})

# uvicorn.run(app)
