from flask_openapi3 import OpenAPI
from asgiref.wsgi import WsgiToAsgi
import uvicorn

from api.users.routes import users_app
from database import db


def register_routes(app):
    pass


def create_app():
    app = OpenAPI(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://test:test@localhost:5432/flask_interview"
    db.init_app(app)
    app.register_api(users_app)
    return app


# === create module-level Flask and ASGI apps so uvicorn can import them ===
flask_app = create_app()
asgi_app = WsgiToAsgi(flask_app)


if __name__ == "__main__":
    # Local dev runner (optional) — still uses asgi_app under the hood
    uvicorn.run(
        asgi_app,
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
