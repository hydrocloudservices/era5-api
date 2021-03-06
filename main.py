import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/salut")
async def getCity():
    return {
        "message": "Hey, salut, test2!"
    }

if __name__ == "__main__" and os.environ.get("ENVIRONMENT") != "PRODUCTION":
    uvicorn.run(app, host="0.0.0.0", port=8000)