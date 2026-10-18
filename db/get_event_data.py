import fastf1
import pandas as pd
from config import CACHE_DIR

fastf1.Cache.enable_cache(CACHE_DIR)

def get_schedule(year):
    schedule = fastf1.get_event_schedule(year, include_testing=False)
    return schedule
    
def get_event_data(year, session_type, event_name=None, round_number= None, location=None):
    if event_name is None and round_number is None and location is None:
        raise ValueError("Please enter atleast one of the following event name, location, round number: ")
    
    schedule = get_schedule(year)
    matches = schedule

    if event_name is not None:
        matches = matches.loc[matches["EventName"].str.casefold() == event_name.casefold()]
    if round_number is not None:
        matches = matches.loc[matches["RoundNumber"] == round_number]
    if location is not None:
        matches = matches.loc[matches["Location"].str.casefold() == location.casefold()]
    
    if len(matches) == 0:
        raise ValueError("No event matches that information")
    if len(matches) > 1:
        raise ValueError("There are 2 events based on your information")
    if len(matches) == 1:
        event = matches.iloc[0]
    return event

def get_basic_info():
    year = int(input("Enter Year (required): "))
    session_type = input("Enter Session Type(FP1, Q, R, SQ, SR) (required): ").strip().upper()

    print("Enter atleast one of the following:")
    event_name = input("Event name (blank to skip): ").strip()
    round_number = (input("Round number (blank to skip): "))
    location = input("Location (blank to skip): ").strip()

    if event_name == "":
        event_name = None
    if round_number == "":
        round_number = None
    else:
        round_number=int(round_number)
    if location == "":
        location = None
    event = get_event_data(year, session_type, event_name, round_number, location)
    return year, session_type, event


if __name__ == "__main__":
    get_basic_info()

