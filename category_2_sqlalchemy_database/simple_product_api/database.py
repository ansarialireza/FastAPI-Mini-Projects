from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from typing import Optional

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    age: Mapped[Optional[Integer]] = mapped_column(Integer)

    def __repr__(self) -> str:
        return (
            f"user id{self.id}, firstname {self.first_name}, "
            f"lastname {self.last_name}"
        )


Base.metadata.create_all(engine)

session = SessionLocal()

# alireza = User(first_name="alireza", last_name="ansari", age=26)
# session.add(alireza)
# session.commit()

# retrieve all data
user = session.query(User).filter_by(first_name="alireza").first()

session.delete(user)
session.commit()
