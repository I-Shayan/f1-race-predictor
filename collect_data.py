import fastf1
from config import CACHE_DIR, RAW_DATA_DIR
from db.get_event_data import get_basic_info, get_schedule
from db.operations import save_session_results

fastf1.Cache.enable_cache(CACHE_DIR)

def get_session_data(year, event_name, session_type):
    session = fastf1.get_session(year, event_name, session_type)
    session.load()
    return session.results

def get_weekend_data(year, event):
    sessions = ['Q', 'R']
    for session_type in sessions:
        result = get_session_data(year, event["EventName"], session_type)
        save_session_results(year, event["EventName"], session_type, event["RoundNumber"], event["Location"], result)
        print(f"Saved {session_type} for {year}")

def get_season_data(year):
    schedule = get_schedule(year)
    for _, rows in schedule.iterrows():
        print(rows["EventName"])
        get_weekend_data(year, rows)

if __name__== "__main__":
    year, session_type, event = get_basic_info()
    get_season_data(year)