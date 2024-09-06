import logging
import os
from dotenv import dotenv_values


class ScrapConfig:
    SCRAP_URL: str = ""

class BaseOrmConfig:
    ORM_DATABASE: str = "postgres"
    ORM_ECHO: bool = False
    ORM_ECHO_POOL: bool = False
    ORM_ENABLE_FROM_LINTING: bool = True
    ORM_HIDE_PARAMETERS: bool = False
    ORM_HOST: str = "vector_db"
    ORM_ISOLATION_LEVEL: str = "SERIALIZABLE"
    ORM_PASSWORD: str = "postgres"
    ORM_POLL_MAX_OVERFLOW: int = 1
    ORM_POOL_PRE_PING: bool = True
    ORM_POOL_RECYCLE_SECONDS: int = 10 * 60
    ORM_POOL_RESET_ON_RETURN: str = "rollback"
    ORM_POOL_SIZE: int = 20
    ORM_POOL_TIMEOUT: int = 30
    ORM_POOL_USE_LIFO: bool = True
    ORM_PORT: int = 5432
    ORM_QUERY_CACHE_SIZE: int = 500
    ORM_USERNAME: str = "postgres"


class BaseFastAPIConfig:
    FASTAPI_ACCESS_LOG: bool = True
    FASTAPI_BACKLOG: int = 2048
    FASTAPI_DATE_HEADER: bool = True
    FASTAPI_FORWARDED_ALLOW_IPS: list = None
    FASTAPI_LIMIT_CONCURRENCY: int = None
    FASTAPI_LIMIT_MAX_REQUESTS: int = None
    FASTAPI_PROXY_HEADERS: bool = True
    FASTAPI_RELOAD: bool = False
    FASTAPI_SERVER_HEADER: bool = True
    FASTAPI_SERVE_HOST: str = "0.0.0.0"
    FASTAPI_SERVE_PORT: int = 8500
    FASTAPI_TIMEOUT_GRACEFUL_SHUTDOWN: int = None
    FASTAPI_TIMEOUT_KEEP_ALIVE: int = 5
    FASTAPI_WS_MAX_SIZE: int = 16777216
    FASTAPI_WS_PER_MESSAGE_DEFLATE: bool = True
    FASTAPI_WS_PING_INTERVAL: float = 20.0
    FASTAPI_WS_PING_TIMEOUT: float = 20.0


class BaseConfig(BaseOrmConfig, BaseFastAPIConfig):
    LOGGING_LEVEL: int = logging.INFO


def apply_config():
    getcwd = os.getcwd()
    env = dotenv_values(f"{getcwd}/.env")

    ScrapConfig.SCRAP_URL = env.get("SCRAP_URL")

    BaseOrmConfig.ORM_DATABASE = env.get("ORM_DATABASE")
    BaseOrmConfig.ORM_ECHO = env.get("ORM_ECHO").lower() in ('true', '1', 't')
    BaseOrmConfig.ORM_ECHO_POOL =  env.get("ORM_ECHO_POOL").lower() in ('true', '1', 't')
    BaseOrmConfig.ORM_ENABLE_FROM_LINTING =  env.get("ORM_ENABLE_FROM_LINTING").lower() in ('true', '1', 't')
    BaseOrmConfig.ORM_HIDE_PARAMETERS =  env.get("ORM_HIDE_PARAMETERS").lower() in ('true', '1', 't')
    BaseOrmConfig.ORM_HOST = env.get("ORM_HOST")
    BaseOrmConfig.ORM_ISOLATION_LEVEL = env.get("ORM_ISOLATION_LEVEL")
    BaseOrmConfig.ORM_PASSWORD = env.get("ORM_PASSWORD")
    BaseOrmConfig.ORM_POLL_MAX_OVERFLOW = int(env.get("ORM_POLL_MAX_OVERFLOW"))
    BaseOrmConfig.ORM_POOL_PRE_PING = env.get("ORM_POOL_PRE_PING").lower() in ('true', '1', 't')
    BaseOrmConfig.ORM_POOL_RECYCLE_SECONDS = int(env.get("ORM_POOL_RECYCLE_SECONDS"))
    BaseOrmConfig.ORM_POOL_RESET_ON_RETURN = env.get("ORM_POOL_RESET_ON_RETURN")
    BaseOrmConfig.ORM_POOL_SIZE = int(env.get("ORM_POOL_SIZE"))
    BaseOrmConfig.ORM_POOL_TIMEOUT = int(env.get("ORM_POOL_TIMEOUT"))
    BaseOrmConfig.ORM_POOL_USE_LIFO = env.get("ORM_POOL_USE_LIFO").lower() in ('true', '1', 't')
    BaseOrmConfig.ORM_PORT = int(env.get("ORM_PORT"))
    BaseOrmConfig.ORM_QUERY_CACHE_SIZE = int(env.get("ORM_QUERY_CACHE_SIZE"))
    BaseOrmConfig.ORM_USERNAME = env.get("ORM_USERNAME")

    BaseFastAPIConfig.FASTAPI_ACCESS_LOG = env.get("FASTAPI_ACCESS_LOG").lower() in ('true', '1', 't')
    BaseFastAPIConfig.FASTAPI_BACKLOG = int(env.get("FASTAPI_BACKLOG"))
    BaseFastAPIConfig.FASTAPI_DATE_HEADER = env.get("FASTAPI_DATE_HEADER").lower() in ('true', '1', 't')
    BaseFastAPIConfig.FASTAPI_FORWARDED_ALLOW_IPS = None
    BaseFastAPIConfig.FASTAPI_LIMIT_CONCURRENCY = None
    BaseFastAPIConfig.FASTAPI_LIMIT_MAX_REQUESTS = None
    BaseFastAPIConfig.FASTAPI_PROXY_HEADERS = env.get("FASTAPI_PROXY_HEADERS").lower() in ('true', '1', 't')
    BaseFastAPIConfig.FASTAPI_RELOAD = env.get("FASTAPI_RELOAD").lower() in ('true', '1', 't')
    BaseFastAPIConfig.FASTAPI_SERVER_HEADER = env.get("FASTAPI_SERVER_HEADER").lower() in ('true', '1', 't')
    BaseFastAPIConfig.FASTAPI_SERVE_HOST = env.get("FASTAPI_SERVER_HOST")
    BaseFastAPIConfig.FASTAPI_SERVE_PORT = int(env.get("FASTAPI_SERVE_PORT"))
    BaseFastAPIConfig.FASTAPI_TIMEOUT_GRACEFUL_SHUTDOWN = None
    BaseFastAPIConfig.FASTAPI_TIMEOUT_KEEP_ALIVE = int(env.get("FASTAPI_TIMEOUT_KEEP_ALIVE"))
    BaseFastAPIConfig.FASTAPI_WS_MAX_SIZE = int(env.get("FASTAPI_WS_MAX_SIZE"))
    BaseFastAPIConfig.FASTAPI_WS_PER_MESSAGE_DEFLATE = env.get("FASTAPI_WS_PER_MESSAGE_DEFLATE").lower() in ('true', '1', 't')
    BaseFastAPIConfig.FASTAPI_WS_PING_INTERVAL = float(env.get("FASTAPI_WS_PING_INTERVAL"))
    BaseFastAPIConfig.FASTAPI_WS_PING_TIMEOUT = float(env.get("FASTAPI_WS_PING_TIMEOUT"))
