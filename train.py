from features import driver_avg_finish_last5
from prepare_data import join_data, seperate_race_and_quali

if __name__ == "__main__":
    joined_df = join_data()
    merged_df = seperate_race_and_quali(joined_df)
    features_df = driver_avg_finish_last5(merged_df)

    train_df = features_df[features_df["year"] == 2023].copy()
    val_df = features_df[features_df["year"] == 2024].copy()
    test_df = features_df[features_df["year"] == 2025].copy()

    feature_columns = ["qualifying_position", "driver_avg_finish_last5"]

    X_train = train_df[feature_columns]
    y_train = train_df["finish_position"]

    X_val = val_df[feature_columns]
    y_val = val_df["finish_position"]

    print("Training rows:", len(train_df))
    print("Validation rows:", len(val_df))
    print("Test rows:", len(test_df))

    print(
    features_df.groupby("year")["round_number"]
    .agg(["nunique", "min", "max"])
    )