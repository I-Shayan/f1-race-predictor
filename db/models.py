from db.database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy import UniqueConstraint


class RaceSession(Base):

    __tablename__ = "race_sessions"
    __table_args__ = (UniqueConstraint("round_number", "session_type", "year")),

    id = mapped_column(Integer, primary_key = True)
    year = mapped_column(Integer, nullable=False)
    round_number = mapped_column(Integer, nullable=False)
    session_type = mapped_column(String, nullable=False)
    event_name = mapped_column(String, nullable=False)
    location = mapped_column(String)

class SessionResult(Base):

    __tablename__ = "session_results"
    __table_args__ = (UniqueConstraint("race_session_id", "driver")),

    id = mapped_column(Integer, primary_key = True)
    race_session_id = mapped_column(Integer, ForeignKey("race_sessions.id"), nullable=False)
    driver = mapped_column(String, nullable=False)
    team = mapped_column(String, nullable=False)
    position = mapped_column(Integer)
    points = mapped_column(Float)