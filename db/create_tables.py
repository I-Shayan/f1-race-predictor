from db.database import engine, Base
import db.models

Base.metadata.create_all(engine)