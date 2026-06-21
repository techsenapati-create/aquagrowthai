from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.predictor import (
    classify_growth,
    forecast_growth
)

app = FastAPI(
    title="Fish Growth Analytics"
)

templates = Jinja2Templates(
    directory="app/templates"
)


@app.get("/", response_class=HTMLResponse)
async def home(
    request: Request
):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@app.get("/classify", response_class=HTMLResponse)
async def classify_page(
    request: Request
):
    return templates.TemplateResponse(
        "classify.html",
        {
            "request": request,
            "result": None
        }
    )


@app.post("/classify", response_class=HTMLResponse)
async def classify_result(
    request: Request,
    sex: int = Form(...),
    length: float = Form(...),
    weight: float = Form(...),
    depth: float = Form(...),
    dpl: float = Form(...),
    perimeter: float = Form(...)
):

    result = classify_growth(
        length,
        weight,
        depth,
        dpl,
        perimeter,
        sex
    )

    return templates.TemplateResponse(
        "classify.html",
        {
            "request": request,
            "result": result
        }
    )


@app.get("/forecast", response_class=HTMLResponse)
async def forecast_page(
    request: Request
):
    return templates.TemplateResponse(
        "forecast.html",
        {
            "request": request,
            "prediction": None
        }
    )


@app.post("/forecast", response_class=HTMLResponse)
async def forecast_result(
    request: Request,
    month_no: int = Form(...),
    sex: int = Form(...),
    length: float = Form(...),
    weight: float = Form(...),
    depth: float = Form(...),
    dpl: float = Form(...),
    perimeter: float = Form(...)
):

    prediction = forecast_growth(
        month_no,
        length,
        weight,
        depth,
        dpl,
        perimeter,
        sex
    )

    return templates.TemplateResponse(
        "forecast.html",
        {
            "request": request,
            "prediction": prediction
        }
    )