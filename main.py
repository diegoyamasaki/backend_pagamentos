from fastapi import FastAPI
from interface.routes import routes

app = FastAPI()

app.include_router(router=routes)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
