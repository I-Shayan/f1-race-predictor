from prepare_data import join_data, seperate_race_and_quali

def driver_avg_finish_last5(merged_df):
    df = merged_df.copy()
    df = df.sort_values(by=["driver", "year", "round_number"])
    df["previous_finish"] = df.groupby("driver")["finish_position"].shift(1)
    df["driver_avg_finish_last5"] = (
    df.groupby("driver")["previous_finish"]
    .transform(lambda x: x.rolling(window=5, min_periods=1).mean()))
    return df

if __name__ == "__main__":
    df = join_data()
    df = seperate_race_and_quali(df)
    features_df = driver_avg_finish_last5(df)
    print(features_df.groupby("year")["round_number"].nunique())