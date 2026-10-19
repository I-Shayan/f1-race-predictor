import fastf1
from config import CACHE_DIR, RAW_DATA_DIR
from db.get_event_data import get_basic_info, get_schedule
from db.operations import save_session_results, has_session_results

fastf1.Cache.enable_cache(CACHE_DIR)

def get_session_data(year, event_name, session_type):
    session = fastf1.get_session(year, event_name, session_type)
    session.load()
    return session.results

def get_weekend_data(year, event):
    for session_type in ["Q", "R"]:
        if has_session_results(year, event["RoundNumber"], session_type):
            print(f"Skipping {year} {event['EventName']} {session_type}: already saved")
            continue

        result = get_session_data(year, event["EventName"], session_type)

        if result.empty:
            raise ValueError(
                f"No results for {year} {event['EventName']} {session_type}"
            )

        save_session_results(
            year,
            event["EventName"],
            session_type,
            event["RoundNumber"],
            event["Location"],
            result
        )

def get_season_data(year):
    schedule = get_schedule(year)
    for _, rows in schedule.iterrows():
        print(rows["EventName"])
        get_weekend_data(year, rows)

if __name__ == "__main__":
    for year in [2023, 2024, 2025]:
        get_season_data(year)