import os
from kombu import Queue
from functools import lru_cache


def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name:
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "celery"}


class Config:
    URL_PAYMENT_SERVICE = os.environ.get("URL_PAYMENT_SERVICE",
                                         "https://run.mocky.io/v3/0bca48f0-16db-4726-96a8-d4206306f698")

    CELERY_BROKER_URL: str = "amqp://admin:admin@localhost:5672/pagamentos"

    CELERY_TASK_QUEUES: list = (
        Queue("celery"),
        Queue("bank_payments")
    )
    CELERY_TASK_ROUTES = (route_task,)


class DevelopmentConfig(Config):
    pass


@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
    }
    config_name = os.environ.get("CELERY_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()

