import fastapi as fa

from app.routers import router

app = fa.FastAPI(title="Python backend 2023")

app.include_router(router)
