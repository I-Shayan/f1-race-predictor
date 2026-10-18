from db.database import Session
from db.models import RaceSession, SessionResult
from sqlalchemy import select
import pandas as pd

def save_session_results(year, event_name, session_type, round_number, location, results_df):
    session = Session()

    with session:
        existing_session = session.scalar(select(RaceSession).
        where(RaceSession.year == year, 
            RaceSession.session_type == session_type,
            RaceSession.round_number == round_number))
        if existing_session is None:
            existing_session = RaceSession(year=year, event_name=event_name, session_type=session_type, round_number=round_number, location=location)
            session.add(existing_session)
            session.flush()
        print(existing_session.id)

        for _, rows in results_df.iterrows(): 
            existing_result = session.scalar(select(SessionResult).
            where(SessionResult.race_session_id == existing_session.id,
                SessionResult.driver == rows["Abbreviation"]))
            if existing_result is None:
                existing_result = SessionResult(race_session_id=existing_session.id,driver=rows["Abbreviation"])
                session.add(existing_result)
            existing_result.team = rows["TeamName"]
            if pd.isna(rows["Position"]):
                existing_result.position = None
            else:
                existing_result.position = int(rows["Position"])
            if pd.isna(rows["Points"]):
                existing_result.points = None
            else:
                existing_result.points = float(rows["Points"])

        session.commit()
        print("Data has been saved to db")


#if __name__ == "__main__":
#     save_session_results(2025, "Japanese Grand Prix", "R", 4, "Suzuka", None)