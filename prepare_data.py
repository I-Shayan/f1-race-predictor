import pandas as pd
from db.database import engine

def join_data():
    race_df = pd.read_sql("SELECT * from race_sessions", engine)
    session_df = pd.read_sql("SELECT * from session_results", engine)
    merged = session_df.merge(race_df,left_on="race_session_id", right_on="id", validate="many_to_one", how="left")
    return merged

def seperate_race_and_quali(df):
    race_df = df[df["session_type"] == 'R'].copy().rename(columns={'position': 'finish_position'})
    quali_df = df[df["session_type"] == 'Q'].copy().rename(columns={'position': "qualifying_position"})
    quali_df = quali_df[["year", "round_number", "driver", "qualifying_position"]]

    merged = race_df.merge(quali_df, on=["year", "round_number", "driver"], how="left", validate="one_to_one")
    return merged

if __name__ == "__main__":
    df = join_data()   
    print(
    df.groupby("year")["round_number"]
    .nunique()
    )    