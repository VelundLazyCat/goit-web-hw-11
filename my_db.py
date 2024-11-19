import contextlib
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_ASYNC_DATABASE_URL = "postgresql+asyncpg://postgres:567234@localhost:5432/hw-11"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:567234@localhost:5432/hw-11"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
class DataBaseSessionManager:
    def __init__(self, url: str):
        self._engine: AsyncEngine = create_async_engine(url)
        self._session_maker: async_sessionmaker = async_sessionmaker(autoflush=False,
                                                                     autocommit=False,
                                                                     bind=self._engine)

    @contextlib.asynccontextmanager
    async def session(self):
        if self._session_maker is None:
            raise Exception('Session is not initialized')
        session = self._session_maker()
        try:
            yield session
        except Exception as err:
            print(err)
            await session.rollback()
        finally:
            await session.close()


session_manager = DataBaseSessionManager(SQLALCHEMY_ASYNC_DATABASE_URL)


# Dependency
async def get_async_db():
    async with session_manager.session() as session:
        yield session
'''