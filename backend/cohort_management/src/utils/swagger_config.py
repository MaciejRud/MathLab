from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI

def get_swagger_config(app: FastAPI):
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Your API Title",
            version="1.0.0",
            description="Your API Description",
            routes=app.routes,
        )
        # Add JWT authentication to the OpenAPI schema
        openapi_schema["components"]["securitySchemes"] = {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        }
        for path in openapi_schema["paths"].values():
            for method in path.values():
                method["security"] = [{"BearerAuth": []}]
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi
