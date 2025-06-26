import yaml
import argparse
from fastapi import FastAPI, HTTPException
import copy
from openapi_server.main import app

def load_existing_openapi(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as openapi_file:
            existing_openapi = yaml.load(openapi_file, Loader=yaml.CLoader)
        return existing_openapi
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Existing OpenAPI file not found.")

def generate_new_openapi(app: FastAPI) -> dict:
    return app.openapi()

def apply_existing_extensions_updates(new_openapi: dict, existing_openapi: dict) -> dict:
    merged_openapi = copy.deepcopy(new_openapi)
    for key, value in existing_openapi.items():
        if key.startswith("x-"):
            merged_openapi[key] = value
    return merged_openapi

def save_openapi(file_path: str, openapi_data: dict):
    with open(file_path, 'w') as openapi_file:
        yaml.dump(openapi_data, openapi_file, Dumper=yaml.CDumper)

def regenerate_openapi(input_file: str, output_file: str):
    try:
        new_openapi = generate_new_openapi(app)
        existing_openapi = load_existing_openapi(input_file)
        new_openapi['openapi'] = '3.0.0'
        updated_openapi = apply_existing_extensions_updates(new_openapi, existing_openapi)
        save_openapi(output_file, updated_openapi)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
    print(f"OpenAPI schema saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generated Code CLI Tool")

    subparsers = parser.add_subparsers(dest='command')

    # Regenerate Command 
    regenerate_parser = subparsers.add_parser('regenerate', help="Regenerate the OpenAPI schema")
    regenerate_parser.add_argument('-i', '--input-file', type=str, default='./openapi.yaml', help="Input file for existing OpenAPI schema")
    regenerate_parser.add_argument('-o', '--output-file', type=str, default='./regenerated-openapi.yaml', help="Output file to save the updated OpenAPI schema")

    args = parser.parse_args()

    if args.command == 'regenerate':
        regenerate_openapi(args.input_file, args.output_file)
    else:
        print("No command specified. Use 'regenerate' to regenerate the OpenAPI schema.")

if __name__ == "__main__":
    main()
