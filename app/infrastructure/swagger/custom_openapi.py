from app.core.config import settings
from fastapi.openapi.utils import get_openapi


# Custom OpenAPI schema to include only `/api` paths
def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        routes=app.routes,
    )

    # 필터링: `/api`로 시작하는 경로만 포함
    openapi_schema["paths"] = {
        path: path_data
        for path, path_data in openapi_schema["paths"].items()
        if path.startswith("/api")
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema
