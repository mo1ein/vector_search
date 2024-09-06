import uvicorn
from fastapi import FastAPI

from src.config.config import apply_config, BaseFastAPIConfig
from src.handler.route import routes

base_responses = {
    400: {"description": "Invalid Input Arguments"},
    504: {"description": "Request Process Timed Out"},
    404: {"description": "Requested Resource Not Found"},
    409: {"description": "Requested Entity Already Exists or Faced a conflict"},
    429: {"description": "Too Many Requests Sent"},
    503: {"description": "Service Temporary Unavailable"},
    501: {"description": "Requested Method Not Implemented"},
    500: {"description": "Internal Server Error"},
}


def _add_routes(app):
    dependencies = [
        # TODO: rate limit
    ]
    responses = base_responses | {
        401: {"description": "Invalid Authentication Credentials"},
        403: {"description": "HAVE NOT ENOUGH PRIVILEGES TO PERFORM AN ACTION OR ACCESS A RESOURCE"},
    }
    app.include_router(routes, dependencies=dependencies, responses=responses)


def _add_routers(app):
    _add_routes(app)


def _create_app():
    app = FastAPI()
    _add_routers(app)
    return app


def serve():
    app = _create_app()
    uvicorn.run(
        app,
        host=BaseFastAPIConfig.FASTAPI_SERVE_HOST,
        port=BaseFastAPIConfig.FASTAPI_SERVE_PORT,
    )


if __name__ == '__main__':
    apply_config()
    serve()
