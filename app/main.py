import fastapi as fa

from app.routers import router

app = fa.FastAPI(title="Deadline schedule")

app.include_router(router)
