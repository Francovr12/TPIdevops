import sentry_sdk
from fastapi import FastAPI
from app.routes import task_routes
import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

sentry_sdk.init(
    dsn="https://97e3f6da0071d290b3ad05256eed40c2@o4509374230691840.ingest.us.sentry.io/4509374233837568",
    traces_sample_rate=1.0
)

app = FastAPI()
app.include_router(task_routes.router)

@app.get("/")
def healthcheck():
    return {"status": "ok"}
@app.get("/error")
def trigger_error():
    1 / 0
