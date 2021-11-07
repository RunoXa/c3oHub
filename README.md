# C3O-Hub: A website for searching job-repositories

## Bachelor thesis - Onur Arslan - TU-Berlin - Distributed and Operating Systems

- An implemented website to find job-repositories with decision support
- Backend: Python >= 3.6 FastAPI-Framework, JSON
- Fronted: HTML, CSS, JavaScript (JQuery)
- Server: UVICORN

## Steps to run the code

## Install FastAPI and uvicorn
- pip install fastapi[all] (includes both)

## Install multipart for submit form data (if necessary)
- pip install python-multipart

## Start the uvicorn server to run the code
- uvicorn main:app --reload

## Open a Browser and go to the server host
- example: http://127.0.0.1:8000

## For testing open the interactive API docs
- http://localhost:8000/docs

## URLs
- http://localhost:8000/
- http://localhost:8000/submitForm
