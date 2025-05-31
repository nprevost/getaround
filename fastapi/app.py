import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.routing import APIRoute
from starlette.requests import Request

tags_metadata = [
    {
        "name": "Predict"
    }
]

app = FastAPI(
    title="Getaround API",
    description="Project GetAround",
    version="0.1",
    contact={
        "name": "Nicolas",
        "url": "https://github.com/nprevost/getaround",
    },
    openapi_tags = tags_metadata)


@app.post("/predict", tags=["Predict"])
async def predict():
    return "Post"

@app.get("/")
async def root(request: Request) -> JSONResponse:
    endpoints = []

    endpoint = {
        "name": "docs",
        "path": "/docs",
        "methods": "GET"
    }
    endpoints.append(endpoint)
    
    for route in app.routes:
        if isinstance(route, APIRoute):
            endpoint = {
                "name": route.name,
                "path": route.path,
                "methods": route.methods
            }
            endpoints.append(endpoint)

    return endpoints


if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=4000)