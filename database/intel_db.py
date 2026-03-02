from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///intelligence.db"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Intelligence(Base):
    __tablename__ = "intelligence"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    category = Column(String)
    title = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


def init_db():
    Base.metadata.create_all(bind=engine)


def save_intelligence(items):

    session = SessionLocal()

    for item in items:

        record = Intelligence(
            source=item.get("source"),
            category=item.get("category"),
            title=item.get("title")
        )

        session.add(record)

    session.commit()
    session.close()