from abc import abstractmethod

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.config import config
from src.utils.metaclasses.singleton import Singleton


class SessionPort:
    @abstractmethod
    def get_session(self):
        raise NotImplementedError

    @abstractmethod
    def remove_session(self):
        raise NotImplementedError


class SessionManager(SessionPort, metaclass=Singleton):
    def __init__(self) -> None:
        self._session_generator = self._get_session_generator()

    def get_session(self):
        return self._session_generator()

    def remove_session(self):
        self._session_generator.remove()

    def _get_session_generator(self):
        engine = self._create_engine()
        session_maker = sessionmaker(engine)
        session_generator = scoped_session(session_maker)
        return session_generator

    @staticmethod
    def _create_engine():
        url = URL.create(
            drivername="postgresql+psycopg",
            username=config.BaseOrmConfig.ORM_USERNAME,
            password=config.BaseOrmConfig.ORM_PASSWORD,
            host=config.BaseOrmConfig.ORM_HOST,
            port=config.BaseOrmConfig.ORM_PORT,
            database=config.BaseOrmConfig.ORM_DATABASE,
        )
        return create_engine(
            url,
            isolation_level=config.BaseOrmConfig.ORM_ISOLATION_LEVEL,
            echo=config.BaseOrmConfig.ORM_ECHO,
            echo_pool=config.BaseOrmConfig.ORM_ECHO_POOL,
            enable_from_linting=config.BaseOrmConfig.ORM_ENABLE_FROM_LINTING,
            hide_parameters=config.BaseOrmConfig.ORM_HIDE_PARAMETERS,
            pool_pre_ping=config.BaseOrmConfig.ORM_POOL_PRE_PING,
            pool_size=config.BaseOrmConfig.ORM_POOL_SIZE,
            pool_recycle=config.BaseOrmConfig.ORM_POOL_RECYCLE_SECONDS,
            pool_reset_on_return=config.BaseOrmConfig.ORM_POOL_RESET_ON_RETURN,
            pool_timeout=config.BaseOrmConfig.ORM_POOL_TIMEOUT,
            pool_use_lifo=config.BaseOrmConfig.ORM_POOL_USE_LIFO,
            query_cache_size=config.BaseOrmConfig.ORM_QUERY_CACHE_SIZE,
            max_overflow=config.BaseOrmConfig.ORM_POLL_MAX_OVERFLOW,
        )
