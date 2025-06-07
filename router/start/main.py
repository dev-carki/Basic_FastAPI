from fastapi import FastAPI
from router.start.routes import item, user

app = FastAPI()

app.include_router(item.router)
app.include_router(user.router)