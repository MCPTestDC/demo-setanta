# coding: utf-8

from fastapi import FastAPI

from openapi_server.apis.default_api import router as DefaultApiRouter

app = FastAPI(
    title="Recipe API",
    description="A RESTful API for managing recipes, ingredients, and users.",
    version="1.0.0",
    servers=[
        {"url": "/", "description": "Root Server"},
    ],
)

app.include_router(DefaultApiRouter)
