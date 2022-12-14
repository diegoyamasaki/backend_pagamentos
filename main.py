from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from interface.routes import routes
from infra.message_broker.rabbitmq import RabbitMq

app = FastAPI(
    title="Backend de Pagamentos",
    description="Sistema de pagamentos",
    version="1.0.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=routes)

app.celery_app = RabbitMq().create_celery()
celery = app.celery_app

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
