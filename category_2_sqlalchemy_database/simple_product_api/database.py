from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase


SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    age = Column(Integer)

    def __repr__(self):
        return (
            f"user id{self.id}, firstname {self.first_name}, "
            f"lastname {self.last_name}"
        )


Base.metadata.create_all(engine)
