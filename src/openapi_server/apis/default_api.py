from typing import Dict, List, Any

from fastapi import (
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Request,
    Response,
    Security,
    status,
)

from openapi_server.factories.factory import generic_mock_model
from openapi_server.models.extra_models import TokenModel

from pydantic import StrictStr
from typing import Any
from openapi_server.models.ingredient import Ingredient
from openapi_server.models.recipe import Recipe
from openapi_server.models.user import User

from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()

status_codes = {
    "get": 200,
    "post": 201,
    "put": 200,
    "patch": 200,
    "delete": 200
}

@router.get(
    "/recipes",
    responses={
        "200": {"description": "A list of recipes"},
        "401": {"description": "Unauthorized"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Get a list of recipes",
    response_model_by_alias=True
)
async def recipes_get(
    response: Response,
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.post(
    "/recipes",
    responses={
        "201": {"description": "Recipe created"},
        "400": {"description": "Bad Request"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Create a new recipe",
    response_model_by_alias=True
)
async def recipes_post(
    response: Response,
    recipe: Recipe = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.delete(
    "/recipes/{recipeId}",
    responses={
        "204": {"description": "Recipe deleted"},
        "401": {"description": "Unauthorized"},
        "404": {"description": "Recipe not found"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Delete a recipe by ID",
    response_model_by_alias=True
)
async def recipes_recipe_id_delete(
    response: Response,
    recipeId: StrictStr = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get(
    "/recipes/{recipeId}",
    responses={
        "200": {"description": "A recipe"},
        "401": {"description": "Unauthorized"},
        "404": {"description": "Recipe not found"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Get a recipe by ID",
    response_model_by_alias=True
)
async def recipes_recipe_id_get(
    response: Response,
    recipeId: StrictStr = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.post(
    "/recipes/{recipeId}/ingredients",
    responses={
        "201": {"description": "Ingredient added"},
        "400": {"description": "Bad Request"},
        "404": {"description": "Recipe not found"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Add an ingredient to a recipe",
    response_model_by_alias=True
)
async def recipes_recipe_id_ingredients_post(
    response: Response,
    recipeId: StrictStr = Path(..., description=""),
    ingredient: Ingredient = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.put(
    "/recipes/{recipeId}",
    responses={
        "200": {"description": "Recipe updated"},
        "400": {"description": "Bad Request"},
        "404": {"description": "Recipe not found"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Update a recipe by ID",
    response_model_by_alias=True
)
async def recipes_recipe_id_put(
    response: Response,
    recipeId: StrictStr = Path(..., description=""),
    recipe: Recipe = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get(
    "/users",
    responses={
        "200": {"description": "A list of users"},
        "401": {"description": "Unauthorized"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Get a list of users",
    response_model_by_alias=True
)
async def users_get(
    response: Response,
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.post(
    "/users",
    responses={
        "201": {"description": "User created"},
        "400": {"description": "Bad Request"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Create a new user",
    response_model_by_alias=True
)
async def users_post(
    response: Response,
    user: User = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.delete(
    "/users/{userId}",
    responses={
        "204": {"description": "User deleted"},
        "401": {"description": "Unauthorized"},
        "404": {"description": "User not found"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Delete a user by ID",
    response_model_by_alias=True
)
async def users_user_id_delete(
    response: Response,
    userId: StrictStr = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.get(
    "/users/{userId}",
    responses={
        "200": {"description": "A user"},
        "401": {"description": "Unauthorized"},
        "404": {"description": "User not found"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Get a user by ID",
    response_model_by_alias=True
)
async def users_user_id_get(
    response: Response,
    userId: StrictStr = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

@router.put(
    "/users/{userId}",
    responses={
        "200": {"description": "User updated"},
        "400": {"description": "Bad Request"},
        "404": {"description": "User not found"},
        "500": {"description": "Internal Server Error"},
    },
    tags=["default"],
    summary="Update a user by ID",
    response_model_by_alias=True
)
async def users_user_id_put(
    response: Response,
    userId: StrictStr = Path(..., description=""),
    user: User = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
):
    raise HTTPException(status_code=501, detail="Not implemented")

