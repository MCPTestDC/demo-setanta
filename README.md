# API Assistant Codegen Service - README

## Introduction

The API Assistant Codegen Service generates a FastAPI server based on your OpenAPI specification. This service helps you quickly scaffold API endpoints defined in your OpenAPI file, allowing you to focus on implementing business logic rather than boilerplate code.

## Prerequisites

- **python3 (v3.9 - v3.12)**

## Installation

Follow these steps to set up your development environment:

1. In a Terminal window, within the extracted `app-code` folder, create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   # On Unix or MacOS
   source ./venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

To start the FastAPI server, execute the following command:

```bash
  PYTHONPATH=src uvicorn openapi_server.main:app --host 0.0.0.0 --port 8080
```

After running this command, the API server will be accessible at [http://localhost:8080](http://localhost:8080).

### OpenAPI File Regeneration

If you've made changes to your server and want to update the OpenAPI specification to reflect those changes, you can run the `utils.py` script. To do this:

1. Make whatever changes you want to your server
2. To regenerate the OpenAPI schema, use the following command:

```bash
python src/utils.py regenerate --input-file ./openapi.yaml --output-file ./regenerated-openapi.yaml
```

Arguments:

- `regenerate`:
  - -i, --input-file
    Path to the existing OpenAPI schema file (default: ./openapi.yaml).
  - -o, --output-file
    Path where the regenerated OpenAPI schema will be saved (default: ./regenerated-openapi.yaml).

The regeneration process maintains top level extensions (e.g. "x-") from the original OpenAPI file. All other values are created via the FastAPI method `openapi()`. Alongside your code changes, you made need to update endpoint decorators and other related functions. [See here for more information](https://fastapi.tiangolo.com/reference/openapi/)

*Note: Regeneration will only work if your original OpenAPI file is still named `openapi.yaml`. (You can change the naming in the `main()` function in `utils.py`)*

## FAQS

### 1. Why am I receiving 501 errors when calling the generated endpoints?

The default implementation returns a 501 "Not Implemented" error. This is because the server has no logic implemented. For example if you wanted to implement a server
that adds to number's together you might implement the following in the `default_api.py`:

```python
@router.get(
    "/addNumbers",
    responses={
        "201": {"model": AddTwoNumbers, "description": "Successfully created added two numbers"},
        "500": {"description": "Unexpected server error"},
    },
    tags=["default"],
    summary="Add two numbers",
    response_model_by_alias=True
)
async def add_two_numbers(
    response: Response,
    first_number: int = Body(None, description=""),
    second_number: int = Body(None, description=""),
) -> AddTwoNumbers:

    return AddTwoNumbers(first_number, second_number)
```
The model `AddTwoNumbers` would be generated from the openapi.yaml if defined so we just need to implement the logic behind calling and using the model.

### 2. Why is one of my models inheriting from an object that was not generated?

If your OpenAPI schema uses additionalProperties: true, the service generates a placeholder model. Customise this model in your code to define the additional properties.